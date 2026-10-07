import scrapy

class BookSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://www.jumia.com.ng/"]

    def parse(self, response):
        for title in response.css("h3 a::attr(title)").getall():
            yield {"title": title}
