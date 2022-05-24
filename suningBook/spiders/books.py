from copy import deepcopy

import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['suning.com']
    start_urls = ['http://book.suning.com/']

    def parse(self, response):
        # 一级分类（L1表示Lecel 1）
        L1_list = response.xpath('//div[@class="menu-list"]/div/dl')
        # 获取大分类
        for L1 in L1_list:
            item = {}
            item['L1_cate'] = L1.xpath('./dt/h3/a/text()').extract_first()

            # 获取二级分类
            L2_list = L1.xpath('./dd/a')
            for L2 in L2_list:
                # 二级分类url
                item['L2_href'] = L2.xpath('./@href').extract_first()
                # 二级分类名称
                item['L2_name'] = L2.xpath('./text()').extract_first()
                # 获取ci
                item['ci'] = item['L2_href'][26:32]
                # 翻页url
                item['next_url'] = 'https://list.suning.com/emall/showProductList.do?ci=' + item['ci'] + '&pg=03&cp={}'
                yield scrapy.Request(
                    url=item['L2_href'],
                    callback=self.parse_book_list,
                    meta={'item': deepcopy(item)}
                )

                return item

    def parse_book_list(self, response):
        item = response.meta.get('item')
        #获取每一本书的信息
        books_list = response.xpath('//ul[@class="clearfix"]/li')
        for book in books_list:
            #书籍详情URL
            item['book_href'] = 'https:' + book.xpath('//div[@class="res-img"]/div/a/@href').extract_first()
            # 书籍名字
            item['book_name'] = book.xpath('//div[@class="res-img"]/div/a/img/@alt').extract_first()
            # 书籍图片
            item['src'] = 'https:' + book.xpath('//div[@class="res-img"]/div/a/img/@src2').extract_first()

            yield scrapy.Request(
                url=item['book_href'],
                callback=self.parse_book_detail,
                meta={'item': deepcopy(item)}
            )
        # 翻页
        for i in range(5):
            next_url = item['next_url'].format(i+1)
            yield scrapy.Request(
                url=next_url,
                callback=self.parse_book_list,
                meta={'item': deepcopy(item)}
            )

    def parse_book_detail(self, response):
        item = response.meta.get('item')
        # 作者
        item['author'] = response.xpath('//ul[@class="bk-publish clearfix"]/li[1]/text()').extract_first()
        # 出版社
        item['publish'] = response.xpath('//ul[@class="bk-publish clearfix"]/li[2]/text()').extract_first()
        # # 数据处理，采集到的数据有些多余的空格，需要去除
        # item['author'] = item['author'].replace('\n', '').replace('\t', '').replace('</span>', '')
        # item['publish'] = item['publish'].replace('\n', '').replace('\t', '').replace('</span>', '')
        print(item)
        yield item




