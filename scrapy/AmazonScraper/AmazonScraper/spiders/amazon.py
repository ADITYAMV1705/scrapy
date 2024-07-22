import scrapy
from ..items import AmazonscraperItem

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.in/s?k=iphone+15+pro&i=electronics"
    ]

    def parse(self, response):
        for product in response.css('.s-main-slot .s-result-item'):
            item = AmazonscraperItem()
            
            item['product_name'] = product.css('.a-color-base.a-text-normal::text').get()
            item['product_price'] = product.css('.a-price-whole::text').get()
            
            yield item
