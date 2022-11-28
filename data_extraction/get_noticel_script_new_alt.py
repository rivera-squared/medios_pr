# Load necessary libraries
from scrapy import Selector
import requests
import pandas as pd
import numpy as np
import os
import datetime as dt
import locale
import time
import re
from datetime import datetime

noticel = pd.read_csv('noticel_alt.csv')

noticel_url ='https://www.noticel.com/'

def get_noticel(noticel_url):
    sel=Selector(text=requests.get(noticel_url).content)
    title=sel.xpath('//div[@class="entry-title"]/a/h2[@class="teaser__headline"]/span[@class="teaser__headline-marker"]/text()').extract()
    #topic_messy=sel.xpath('//div[@class="teaser-image col-md-4"]/div[@class="category_overlay"]/text()').extract()
    #summary_strip=sel.xpath('//div[@class="teaser-content image col-md-8"]/div[@class="teaser-body"]/text()').extract()
    date_messy=sel.xpath('//div[@class="teaser-content image col-md-8"]/div[@class="teaser-article-date"]/div[@class="teaser-article-pubdate"]/text()').extract()
    link=sel.xpath('//div[@class="entry-title"]/a/@href').extract()
    noticel_dict = {'fecha':date_messy,
                    'titulo':title,
                    'periodico':'Noticel',
                    #'tema':topic_messy,
                    #'resumen':summary_strip,
                    'enlace':link}
    noticel_df = pd.DataFrame(noticel_dict)
    noticel_new.append(noticel_df)
    return noticel_new


noticel_new = []
get_noticel(noticel_url)
noticel_new = pd.concat(noticel_new)
noticel = noticel.append(noticel_new).drop_duplicates(subset=['enlace'])

noticel.to_csv('noticel_alt.csv', index = False)
