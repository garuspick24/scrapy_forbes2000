import scrapy


class CompanySpider(scrapy.Spider):
    name = "company"
    allowed_domains = ["forbes,com"]
    start_urls = ["https://forbes,com"]

    def parse(self, response):
        pass
