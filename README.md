# Scrapy爬虫Demo
## 使用方式

> 普通scrapy爬虫

```python
scrapy crawl books
```

> 分布式爬虫

1. 打开redis-server.exe
2. 打开redis-cli.exe
3. 进入spiders文件后执行命令: scrapy runspider bookPro.py
4. 在redis-cli中输入： lpush urls http://book.suning.com