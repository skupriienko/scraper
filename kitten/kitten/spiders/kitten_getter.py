import scrapy


class KittensSpider(scrapy.Spider):
    # can be any string, will be used to call from the console
    name = 'kitten_getter'

    # This method must be in the spider,
    # and will be automatically called by the crawl command.
    def start_requests(self):
        self.index = 0
        urls = [
            'http://reddit.com/r/cats',
        ]
        for url in urls:
        # We make a request to each url and call
        # the parse function on the http response.
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        filename = "kitten_response_"+str(self.index)+'.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
