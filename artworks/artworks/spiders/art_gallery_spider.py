import scrapy
from ..items import ArtworksItem
from ..utils import date_format, get_item_price


class TrialSpider(scrapy.Spider):
    name = 'art_spider'
    page_number = 1
    start_urls = ["http://pstrial-2022-05-20.toscrape.com/browse/insunsh"]

    def parse(self, response):
        artwork_page_links = response.css("#body div a[href^='/item']::attr(href)")
        yield from response.follow_all(artwork_page_links, self.parse_artwork)

        next_page = f"http://pstrial-2022-05-20.toscrape.com/browse/insunsh?page={self.page_number}"

        if self.page_number < 115:
            self.page_number += 1
            yield response.follow(next_page, callback=self.parse)

    def parse_artwork(self, response):
        items = ArtworksItem()

        def extract_with_css(query):
            return response.css(query).get()

        title = extract_with_css("div h1::text")
        artist = extract_with_css("div h2::text")
        description = extract_with_css("div p::text")
        dated = extract_with_css(r'.date-value\"::text')
        medium = extract_with_css("dd:nth-child(10)::text")
        url = response.url
        price = get_item_price(url)
        listing_url = response.headers.get('response')

        if title:
            items["title"] = title
        if description:
            items["description"] = description
        if medium:
            items["medium"] = medium
        if dated:
            items["dated"] = date_format(dated)
        if artist:
            items["artist"] = artist
        if url:
            items["url"] = url
        if price:
            items["price"] = price
        if listing_url:
            items["listing_url"] = listing_url

        yield items
