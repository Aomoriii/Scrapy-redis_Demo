# Scrapy settings for suningBook project

BOT_NAME = 'suningBook'

SPIDER_MODULES = ['suningBook.spiders']
NEWSPIDER_MODULE = 'suningBook.spiders'

ROBOTSTXT_OBEY = False

# LOG_LEVEL = "WARNING"

DEFAULT_REQUEST_HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# 设置重复过滤器模块
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 设置调取器，scrap_redis中的调度器具备与数据库交互的功能
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 设置当爬虫结束的时候是否保持redis数据库中的去重集合与任务队列，程序结束后不清空redis数据库
SCHEDULER_PERSIST = False

ITEM_PIPELINES = {
    'suningBook.pipelines.SuningbookPipeline': 300,
    # 当开启该管道，该管道将会把数据存到Redis数据库中，也可以自己设置数据库
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
# 设置redis数据库
REDIS_URL = "redis://127.0.0.1:6379"


# 请求间隔时长
DOWNLOAD_DELAY = 1
