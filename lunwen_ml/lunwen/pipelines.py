# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

#item返回字典
class LunwenPipeline(object):

    def process_item(self, item, spider):
        item["text"] = self.process_text(item["text"])
        fh = open("D:/Test/lunwenv2/" + item["topic"] + ".txt", "w")
        fh.write(item["link"])
        fh.write(item["text"])
        fh.close()
        #print(item)
        return item

    def process_text(self, text):
        #text = [re.sub(r'\\t|\\r\\n|\\r\\n\\t', "", i) for i in text]
        #text = [i for i in text if len(i) > 0]  #去除列表中的空字符串
        text = "".join(text)
        return text

    # fh = open("D:/Test/lunwenv2/" + item["topic"] + ".txt", "w")
    # fh.write(item["link"])
    # fh.write(item["text"])
    # fh.close()
