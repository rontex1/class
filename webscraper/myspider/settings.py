BOT_NAME = "myspider"

SPIDER_MODULES = ["myspider.spiders"]
NEWSPIDER_MODULE = "myspider.spiders"

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 0.25

DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
}

ITEM_PIPELINES = {
    "myspider.pipelines.MyspiderPipeline": 300,
}

FEED_EXPORT_ENCODING = "utf-8"
