import scrapy


class CoinSpider(scrapy.Spider):
    name = 'coin'

    def start_requests(self):
        url = 'https://coinmarketcap.com/all/views/all/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for row in response.css('tbody tr'):
            yield {
                "name": row.css("a.cmc-link::text").extract_first(),
                "symbol": row.css("td.cmc-table__cell.cmc-table__cell--sortable.cmc-table__cell--left.cmc-table__cell--sort-by__symbol > div::text").extract_first(),
                # "market_cap": row.css("td.market-cap::text").extract_first(),
                "price": row.css("td.cmc-table__cell.cmc-table__cell--sortable.cmc-table__cell--right.cmc-table__cell--sort-by__price > div > a::text").extract_first(),
                # "circulating_supply": row.css("td.circulating-supply span::attr(data-supply)").extract_first(),
                # "volume": row.css("a.volume::attr(data-usd)").extract_first()

            }
