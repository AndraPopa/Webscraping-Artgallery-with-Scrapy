#Art gallery spider

The purpose of this application is to scrape data for all the artworks in
a specific category from a museum website.

In order to do this, and to be able to retrieve the output, you need 
Scrapy installed. For this, you can run <code>pip install scrapy</code>
in your virtual environment folder.

The name of the spider is _**art_spider**_ and you can find the scrape logic
in _art_gallery_spider.py_ file, in the specific _spiders_ folder.

The fields that are about to be scraped, are declared in _ArtworksItem_ class, specific to
_items.py_ file.

This repository already contains the output in a json file. It was created by running
<code>scrapy crawl art_spider -o output.json</code>. You can obtain the result in other
formats as well, by replacing the ".json" extension with ".xml" and ".csv" and running the
command again.