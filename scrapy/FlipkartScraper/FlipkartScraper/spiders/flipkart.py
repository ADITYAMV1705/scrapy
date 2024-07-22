import scrapy
from ..items import FlipkartscraperItem

class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    start_urls = [
        "https://www.flipkart.com/search?q=iphone%2015%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
]


    def parse(self, response):
        item = FlipkartscraperItem()
        
        product_name = response.css('.KzDlHZ')
        product_price = response.css('._4b5DiR')
        
        item['product_name'] = product_name
        item['product_price'] = product_price
        
        yield item

# import scrapy
# from ..items import FlipkartscraperItem

# class FlipkartSpider(scrapy.Spider):
#     name = "flipkart"
#     allowed_domains = ["flipkart.com"]
#     start_urls = [
#         "https://www.flipkart.com/search?q=iphone%2015%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
#     ]

#     def parse(self, response):
#         for product in response.css('._1AtVbE'):
#             item = FlipkartscraperItem()

#             product_name = product.css('._4rR01T::text').get()
#             product_price = product.css('._30jeq3._1_WHN1::text').get()

#             item['product_name'] = product_name
#             item['product_price'] = product_price

#             yield item