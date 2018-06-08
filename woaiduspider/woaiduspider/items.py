# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field 


class WoaiduspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mongodb_id = Field()
    book_name = Field()
    alias_name = Field()
    author = Field()
    book_description = Field()
    book_covor_image_path = Field()
    book_covor_iamge_url = Field()
    book_download = Field()
    book_file_url = Field()
    book_file = Field()
    book_file_id = Field()
    original_url = Field()
