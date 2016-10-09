#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import pymysql as mdb
import scrapy


class FarmaciaScrapItem(scrapy.Item):
    # define the fields for your item here like:
    nombre = scrapy.Field()
    upc = scrapy.Field()
    imagen = scrapy.Field()
    precio = scrapy.Field()
    pass
