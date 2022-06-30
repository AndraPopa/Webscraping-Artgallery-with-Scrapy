import scrapy


class ArtworksItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    artist = scrapy.Field()
    medium = scrapy.Field()
    listing_url = scrapy.Field()
    dated = scrapy.Field()
    price = scrapy.Field()
