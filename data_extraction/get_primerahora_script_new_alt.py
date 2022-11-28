# Load necessary libraries
from scrapy import Selector
import requests
import pandas as pd
#import numpy as np
#import os
#import datetime as dt
#import locale
#import time
#import re
#from datetime import datetime

primerahora = pd.read_csv('primerahora_alt.csv')

url = 'https://www.primerahora.com/ultimas-noticias/'
ph = 'http://www.primerahora.com'
def get_primera_hora(primerahora_url):
    sel=Selector(text=requests.get(primerahora_url).content)
    title = sel.xpath('//h3/text()').extract()
    #topic = sel.xpath('//h4[@class="ListItemTeaser__meta"]/a/text()').extract()
    #summary = sel.xpath('//p[@class="ListItemTeaser__lede"]/text()').extract()
    date = sel.xpath('//div[@class="ListItemTeaser__date"]/text()').extract()
    link_extension = sel.xpath('//div[@class="ListItemTeaser__column"]/a/@href').extract()
    primerahora_dict = {'fecha':date,
                        'titulo':title,
                        'periodico':'Primera Hora',
                        #'tema':topic,
                        #'resumen':summary,
                        'enlace':link_extension}
    primerahora_df = pd.DataFrame(primerahora_dict)
    primerahora_new.append(primerahora_df)
    return primerahora_new

def get_complete_link(link):
    complete_link = ph + link
    return complete_link

primerahora_new = []

get_primera_hora(url)
primerahora_new = pd.concat(primerahora_new)
primerahora_new['enlace'] = primerahora_new.enlace.apply(get_complete_link)

primerahora = primerahora.append(primerahora_new).drop_duplicates(subset = ['enlace'])

primerahora.to_csv('primerahora_alt.csv', index=False)
