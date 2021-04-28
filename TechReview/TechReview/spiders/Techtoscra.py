import scrapy
from ..items import TechreviewItem

class TechSpider(scrapy.Spider):
    name = 'a'
    page_number = 1
    base_url = 'https://dantri.com.vn'
    start_urls = ['https://dantri.com.vn/']

    def _parse(self, response):
        all_news = response.xpath('//h3[contains(@class, "news-item")]')
        for new in all_news:
            new_url = new.xpath('.//a/@href').extract_first()

            if 'dantri.com' not in new_url:
                new_url = self.base_url + new_url
            yield scrapy.Request(new_url, callback= self.parse_new)

    def parse_new(self, response):
        title = response.xpath('//h1[contains(@class,"dt-news")]/text()').extract_first().replace('\r\n       ', '')
        abstract = response.xpath('//div[@class = "dt-news__sapo"]/h2/text()').extract()
        content = response.xpath('//div[@class = "dt-news__content"]//p/text()').extract()
        image = response.xpath('//div[@class = "dt-news__content"]//img/@src').extract()

        item = TechreviewItem()
        item['title'] = title
        item['abstract'] = abstract
        item['content'] = content
        item['image'] = image

        yield item
