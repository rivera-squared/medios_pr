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

endi = pd.read_csv('endi_alt.csv')

endi_url ='https://www.elnuevodia.com'


def get_endi(url):
    sel = Selector(text=requests.get(url).content)
    title=sel.xpath('//h1[@class="story-tease-title"]/*/text()').extract()[0:10] #Titulo
    #topic=sel.xpath('//div[@class="story-tease-body"]/span[@class="story-tease-category"]/a/text()').extract() #Topic
    date_messy=sel.xpath('//p[@class="story-tease-date"]/text()').extract()
    link_path = sel.xpath('//h1[@class="story-tease-title"]/a/@href').extract()[0:10]
    endi_dict = {'fecha':date_messy, 
                 'titulo':title,
                 'periodico':'El Nuevo Dia',
                 #'tema':topic,
                 'enlace':link_path}
    endi_df = pd.DataFrame(endi_dict)
    endi_new.append(endi_df)
    return endi_new


def get_complete_link(x):
    complete_link = endi_url+x
    return complete_link


endi_new = [] 
get_endi('https://www.elnuevodia.com/ultimas-noticias/')
endi_new = pd.concat(endi_new)
endi_new['enlace'] = endi_new['enlace'].apply(get_complete_link)

endi = endi.append(endi_new).drop_duplicates(subset =['enlace'])

endi.to_csv('endi_alt.csv', index = False)

