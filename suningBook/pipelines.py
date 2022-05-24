# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime

class SuningbookPipeline(object):
    # 下面注释的代码是books.py这个spider所执行并将数据存储到MySQl上。

    # server = sshtunnel.SSHTunnelForwarder(
    #     ('xxx.xxx.xxx.xxx', 22), # 填写你服务器的IP
    #     ssh_username='xxx',       # 连接的用户名
    #     ssh_password='xxxx',      # 密码
    #     remote_bind_address=('xx.xx.xx.xx', 3306), #也是服务器IP
    #     local_bind_address=('127.0.0.1', 3306)
    # )
    # server.start()
    #
    # print('SSH连接成功')
    #
    # def __init__(self):
    #     self.connect = pymysql.connect(
    #         host='127.0.0.1',
    #         port=3306, #MySQL端口
    #         user='xxx',   #数据库用户名
    #         database='xxx',   #数据库名
    #         password='xxx',   #数据库密码
    #         charset='utf8'
    #     )
    #     print('mysql数据库连接成功')
    #     self.cursor = self.connect.cursor()
    #     print('游标获取成功')
    #
    # def process_item(self, item, spider):
    #     info = """INSERT INTO Book(BookcName,Author,Publish) VALUES ('%s','%s','%s')""" \
    #            % (
    #                item['book_name'],
    #                item['author'],
    #                item['publish'],
    #            )
    #     self.cursor.execute(info)
    #     self.connect.commit()
    #     print('insert succeed')
    #     return item
    #
    # def close_spider(self, spider):
    #     self.cursor.close()
    #     self.connect.close()


    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item
