import scrapy
from scrapy.http import Response


class CompanySpider(scrapy.Spider):
    name = "company"
    allowed_domains = ["forbes.com"]
    start_urls = ["https://www.forbes.com/lists/global2000/?sh=2f25e87d5ac0"]

    def parse(self, response: Response, **kwargs):

        for group in response.css(".table-row-group"):
            for company in group.css(".table-row"):
                yield {
                    "rank": company.css('.rank::text').get(),
                    "name": company.css('.organizationName::text').get(),
                    "link": company.css('.table-row::attr(href)').get()
                }
