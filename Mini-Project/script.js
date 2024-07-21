document.addEventListener("DOMContentLoaded", function() {
    Papa.parse("final_price.csv", {
        download: true,
        header: true,
        complete: function(results) {
            console.log('CSV data:', results.data); 
            updatePrices(results.data);
        },
        error: function(error) {
            console.error('Error parsing CSV:', error);
        }
    });
});

function updatePrices(data) {
    const pricesMap = {};
    data.forEach(row => {
        const productName = row.product_name.trim();
        pricesMap[productName] = {
            amazon: row.amazon.trim(),
            flipkart: row.flipkart.trim(),
            reliance: row.reliance.trim(),
            chroma: row.chroma.trim()
        };
    });

    console.log('Prices Map:', pricesMap); 

    document.querySelectorAll('.product-card').forEach(card => {
        const productName = card.querySelector('.product-name').textContent.trim();
        const prices = pricesMap[productName];

        if (prices) {
            let minPrice = Infinity;
            let minPriceRetailer = null;
            
            // Find the minimum price that is not 'SOLD OUT'
            Object.keys(prices).forEach(retailer => {
                const price = prices[retailer];
                if (price !== 'SOLD OUT' && parseFloat(price.replace(/[^\d.]/g, '')) < minPrice) {
                    minPrice = parseFloat(price.replace(/[^\d.]/g, ''));
                    minPriceRetailer = retailer;
                }
            });

            const rows = card.querySelectorAll('.product-description table tr');
            rows.forEach(row => {
                const retailerLink = row.querySelector('a');
                if (retailerLink) {
                    const retailerText = retailerLink.textContent.trim().toLowerCase();
                    const priceCell = row.querySelector('td:last-child');

                    const retailerMap = {
                        'amazon': 'amazon',
                        'flipkart': 'flipkart',
                        'reliance': 'reliance',
                        'croma': 'chroma'
                    };

                    const retailerKey = retailerMap[retailerText];
                    if (retailerKey) {
                        let price = prices[retailerKey] || 'SOLD OUT';
                        if (retailerKey === minPriceRetailer) {
                            priceCell.style.color = '#e74c3c'; // Color for lowest price
                        } else {
                            priceCell.style.color = '#333'; // Default color for other prices
                        }
                        if(price != 'SOLD OUT'){
                            priceCell.textContent = "₹"+price;
                        }
                        else{
                            priceCell.textContent = 'SOLD OUT';
                        }
                    }
                }
            });
        } else {
            console.warn('No price data for product:', productName);
        }
    });
}
