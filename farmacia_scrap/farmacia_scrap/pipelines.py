#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import pymysql as mdb
#import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
from farmacia_scrap.items import FarmaciaScrapItem

class FarmaciaScrapPipeline(object):

	#def __init__(self):
	#	self.conn = mdb.connect(user='testuser', passwd = 'test623', db = 'testdb', host = 'localhost')#, charset="utf8", use_unicode=True)
	#	self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		#print('Entered to process item')
		#self.cursor.execute("SELECT * FROM item WHERE UPC = '%s' " %item['upc'])
		#revision =self.cursor.fetchone()
		#if(revision == 0):
		#try:
		#	self.cursor.execute("INSERT INTO item (upc, nombre, imagen, precio) VALUES (%s, %s, %s, %s)", 
	    #                   (item['upc'],#.encode('utf-8'), 
	    #                    item['nombre'],#.encode('utf-8'),
	    #                    item['imagen'],#.encode('utf-8'),
	    #                    item['precio']))  #.encode('utf-8')))
			#print('Just added a value to the db')
		#	self.conn.commit()

		#except mdb.Error as e:
		#	print ("Error %d: %s" %(e.args[0], e.args[1]))

		return item
		#else:
		#	return item
	
	