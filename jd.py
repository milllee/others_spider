#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: jingdong.py
# Create Time: 2017年04月14日 星期五 14时52分12秒
# Author: Miller Lee
# Email: 252343465@qq.com
# ##############################################

import scrapy
from scrapy.http import Request
from jingdong.items import JingdongItem

class JdSpider(scrapy.Spider):
    name = "jd"
    allow_domains = ["jd.com"]
    start_urls = ['http://jd.com/']

    search_url1 = 'https://search.jd.com/Search?keyword={key}&enc=utf-8&page={page}'
    search_url2 = 'https://search.jd.com/s_new.php?keyword={key}&enc=utf-8&page={page}&s=26&scrolling=y&pos=30&tpl=3_L&show_items={goods_items}'
    shop_url = 'http://mall.jd.com/index-{shop_id}.html'

    def start_requests(self):
        key = "裤子"
        for num in range(1, 100):
            page1 = str(2 * num - 1)
            page2 = str(2 * num)
            yield scrapy.Request(url=self.search_url1.format(key=key, page=page1),callback=self.parse,dont_filter = True)
            yield scrapy.Request(url=self.search_url1.format(key=key, page=page1),callback=self.get_next_half,meta={'page2': page2, 'key': key},dont_filter = True)

    def get_next_half(self, response):
        try:
            items = response.xpath('//*[@id="J_goodsList"]/ul/li/@data-pid').extract()
            key = response.meta['key']
            page2 = response.meta['page2']
            goods_items = ','.join(items)
            yield scrapy.Request(url=self.search_url2.format(key=key, page=page2, goods_items=goods_items), callback = self.next_parse, dont_filter = True)
        except Exception as e:
            print('没有数据')

    def parse(self, response):
        all_goods = response.xpath('//div[@id="J_goodsList"]/ul/li')
        for one_good in all_goods:
            item = JingdongItem()
            try:
                data = one_good.xpath('div/div/a/em')
                item['title'] = data.xpath('string(.)').extract()[0]
                item['comment_count'] = one_good.xpath('div/div[@class="p-commit"]/strong/a/text()').extract()[0]
                item['goods_url'] = 'http:' + one_good.xpath('div/div[4]/a/@href').extract()[0]
                item['shops_id'] = one_good.xpath('div/div[@class="p-shop"]/@data-shopid').extract()[0]
                item['shop_url'] = self.shop_url.format(shop_id=item['shops_id'])
                goods_id = one_good.xpath('div/div[2]/div/ul/li/[1]/a/img/@data-sku').extract()[0]
                if goods_id:
                    item['good_id'] = goods_id
                price = one_good.xpath('div/div[3]/strong/i/text()').extract()
                if price:
                    item['price'] = price[0]

                yield item
            except Exception as e:
                pass

    def next_parse(self, response):
        all_goods = response.xpath('/html/body/li')
        for one_good in all_goods:
            item = JingdongItem()
            try:
                data = one_good.xpath('div/div/a/em')
                item['title'] = data.xpath('string(.)').extract()[0]
                item['comment_count'] = one_good.xpath('div/div[@class="p-commit"]/strong/a/text()').extract()[0]
                item['good_url'] = 'http' + one_good.xpath('div/div[4]/a/@href').extract()[0]
                item['shops_id'] = one_good.xpath('div/div[@class="p-shop"]/@data-shopid').extract()[0]
                item['shop_url'] = self.shop_url.format(shop_id-item['shop_id'])
                goods_id = one_good.xpath('div/div[2]/div/ul/li[1]/a/img/@data-sku').extract()[0]
                if goods_id:
                    item['goods_id'] = goods_id
                price = one_good.xpath('div/div[3]/strong/i/text()').extract()
                if price:
                    item['price'] = price[0]
                yield item
            except Exception as e:
                pass
            
