# import scrapy
# from ..items import TgddtutorialItem
# class TgddSpider(scrapy.Spider):
#     name = 'a'
#     page_number = 1
#     start_urls = ['https://www.thegioididong.com/dtdd']
#
#     def parse(self, response):
#         #all_product = response.css('li.item')
#         all_product = response.xpath('//li[contains(@class, "item")]')
#
#         for product in all_product:
#             item = TgddtutorialItem()
#             # product_name  = product.css('h3::text').extract()
#             # product_price = product.css('strong::text').extract()
#             # product_img   = product.css('div.heightlabel img::attr(src)').get()
#
#             product_name = product.xpath('.//h3/text()').extract_first()
#             product_price = product.xpath('.//strong/text()').extract_first()
#             product_img = product.xpath('.//div[@class = "heghtlabel"]/img[@class = "lazyloaded"]/@alt').extract()
#             #
#             item['product_name'] = product_name
#             item['product_price'] = product_price
#
#             # yield {
#             #     'name' : product_name,
#             #     'price' : product_price
#             # }
#             yield item
#
#         next_page = 'https://www.thegioididong.com/dtdd#i:' + str(TgddSpider.page_number)
#         if TgddSpider.page_number < 11:
#             TgddSpider.page_number += 1
#             yield scrapy.Request(next_page, callback= self.parse)