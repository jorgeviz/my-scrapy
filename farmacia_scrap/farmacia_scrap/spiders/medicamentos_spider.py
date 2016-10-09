#!/usr/bin/python3
import scrapy
import pymysql as mdb
import re
import sys
#import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
from farmacia_scrap.items import FarmaciaScrapItem

class MedicamentoSpider(scrapy.Spider):
    name = "medicamento"


    
    def start_requests(self):
        urls = [
          'http://www.chedraui.com.mx/index.php/ajusco/catalog/category/view/s/farmacia/id/457/',
        ]
        # Configure the parameters to use your own database
        self.conn = mdb.connect(user='testuser', passwd = 'test623', db = 'testdb', host = 'localhost')#, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        for medicamento in response.css('div.item'):
            img_tmp = medicamento.css("a.product-image img::attr(src)").extract_first()
            upc_tmp = re.findall(r'\d{9,13}', img_tmp)
            if(len(upc_tmp)>0):
                item = FarmaciaScrapItem()
                item['nombre'] = medicamento.css("a::attr(title)").extract_first()
                item['imagen'] = medicamento.css("a.product-image img::attr(src)").extract_first()
                item['upc'] = medicamento.css("a.product-image img::attr(src)").re(r'\d{9,13}')
                item['precio'] = medicamento.css("div.price-box span.price::text").extract_first()
                tmp_nombre = item['nombre']
                try: 
                    revision = self.cursor.execute("SELECT * FROM item WHERE NOMBRE = '%s' " %tmp_nombre)
                except mdb.Error as e:
                     print ("Error %d: %s" %(e.args[0], e.args[1]))
                if(revision == 0):
                    try:
                        self.cursor.execute("INSERT INTO item (upc, nombre, imagen, precio) VALUES (%s, %s, %s, %s)", 
                                           (item['upc'],
                                            item['nombre'],
                                            item['imagen'],
                                            item['precio']))
                        print('Just added an item to the db')
                        self.conn.commit()

                    except mdb.Error as e:
                        print ("Error %d: %s" %(e.args[0], e.args[1]))
                else:
                    print('Item already added before')
                #print('Will return item')
                #return item
        

        #Recursevely look for more links
        # follow links to Farmacia pages 
        next_page = response.css('div.pages a.next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print('Crawling to next page')
            yield scrapy.Request(next_page, callback=self.parse)

        
        
            
            

        

