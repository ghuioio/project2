import scrapy
from ..items import TgddtutorialItem
class TgddSpider(scrapy.Spider):
    name = 'a' #
    page_number = 1
    base_url = 'https://www.thegioididong.com/'
    start_urls = ['https://www.thegioididong.com/dtdd#i:5']

    def parse(self, response):
        all_product = response.xpath('//li[contains(@class, "item")]')

        for product in all_product:
            product_url = product.xpath('.//a/@href').extract_first()

            if 'thegioididong.com' not in product_url:
                product_url = self.base_url + product_url

            yield scrapy.Request(product_url, callback= self.parse_product)

        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_product(self,response):
        name = response.xpath('//div/h1/text()').extract_first()
        price = response.xpath('//strong/text()').extract_first()
        image = response.xpath('//img/@src').extract_first()
        ram = response.xpath('//li[contains(@class, "g50")]//div/text()').extract_first()
        memory = response.xpath('//li[contains(@class, "g49")]//div/text()').extract_first()
        battery = response.xpath('//li[contains(@class, "g84")]//div/text()').extract_first()
        star = response.xpath('//div[contains(@class, "lcrt")]//b/text()').extract_first()

        item = TgddtutorialItem()

        item['name'] = name
        item['price'] = price
        item['image'] = image
        item['ram'] = ram
        item['memory'] = memory
        item['battery'] = battery
        item['star'] = star

        yield item





