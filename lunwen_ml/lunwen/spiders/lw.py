# -*- coding: utf-8 -*-
import scrapy
from lunwen_m.lunwen_ml.lunwen.items import LunwenItem

class LwSpider(scrapy.Spider):
    name = 'lw'
    #allowed_domains = ['21ks.net']
    start_urls = ['https://www.21ks.net/lunwen/shsjlw/']
    #https://www.21ks.net/lunwen/shsjlw/List_1.html缺


    def parse(self, response):
        titles = response.xpath("//*[@id='div08']/div[3]//div[@class='title']")
        for title in titles:
            item = LunwenItem()
            item["topic"] = title.xpath(".//a[@target='_blank']/text()").get()
            item["link"] = title.xpath(".//a[@target='_blank']/@href").get()
            #print(item)
            yield scrapy.Request(item["link"], callback=self.parse_link, meta={"item": item})


        #翻页
        #.// *[ @ id = 'gform'] / div / table / tbody / tr / td / div / table / tbody / tr / td / div / div[2] / a[
        #   contains(text(), "下一页")]
        #next_url = response.xpath("//*[@id='divliebiao']/div/a[4]/@href").get()
        next_url = response.xpath("//*[@id='divliebiao']/div/a[contains(text(), '下一页')]/@href").get()
        print("address"+next_url)
        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)

            #useless
            #//*[@id="divliebiao"]/div/a[4]
            #item = LunwenItem(topic=topic, link=link)
            #yield item
            #yield scrapy.Request(url=link, meta={'links': link}, callback=self.parse_links, dont_filter=True)

    def parse_link(self, response):
        #item = LunwenItem()
        item = response.meta['item']
        item['text'] = response.xpath("//div[@class='left']/div[@id='div16']//p//text()").getall()
        print(item)
        yield item



'''
    def parse_html(self, response):
        link = response.meta['link']
        text = response.xpath("//p//text()").getall()
        item = LunwenItem(text=text)
        yield item

'''
'''
    def parse(self, response):
        topic = response.xpath("//div/a[@target='_blank']/text()").getall()
        links = response.xpath("//div/a[@target='_blank']/@href").getall()
        # 变为一行文字topic = "".join(links)
        # print(topic,link)
        item = LunwenItem(topic=topic, links=links)
        for link in links:
            yield scrapy.Request(url=link, meta={'link':link},callback=self.parse_link)
        yield item


    def parse_link(self, response):
        print("executing...")
        link = response.meta['link']
        #print(type(link)) url str
        yield scrapy.Request(url=link, meta={'link': link}, callback=self.parse_html, dont_filter=True)
        #print(type(html))

    def parse_html(self, response):
        print("parsing...")
        text = response.xpath("//div[@id='div16']").get()
        text = response.xpath(".//p//text()").getall()
        #split()分割字符串
        text = "".join(text).strip()
        print(type(text))
        #print(text)
        item = LunwenItem(text=text)
        yield item
'''


