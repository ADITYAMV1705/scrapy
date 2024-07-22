import scrapy
from ..items import ReliancescraperItem

class RelianceSpider(scrapy.Spider):
    name = "reliance"
    allowed_domains = ["www.reliancedigital.in"]
    start_urls = [
        "https://www.reliancedigital.in/page/apple-iphone-15-mobiles"
    ]

    def parse(self, response):
        item = ReliancescraperItem()

        item['product_name'] = response.css('p.sp__name::text').get()
        item['product_price'] = response.css('.gimCrs span::text').get()

        yield item