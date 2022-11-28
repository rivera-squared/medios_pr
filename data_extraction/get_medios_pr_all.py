from scrapy import Selector
import requests
import pandas as pd

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


def get_complete_link_endi(x):
    complete_link = endi_url+x
    return complete_link

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

def get_complete_link_primerahora(link):
    complete_link = ph + link
    return complete_link        

endi = pd.read_csv('endi_alt.csv')
endi_url ='https://www.elnuevodia.com'
endi_new = [] 
get_endi('https://www.elnuevodia.com/ultimas-noticias/')
endi_new = pd.concat(endi_new)
endi_new['enlace'] = endi_new['enlace'].apply(get_complete_link_endi)
endi = endi.append(endi_new).drop_duplicates(subset =['enlace'])
endi.to_csv('endi_alt.csv', index = False)

noticel = pd.read_csv('noticel_alt.csv')
noticel_url ='https://www.noticel.com/'
noticel_new = []
get_noticel(noticel_url)
noticel_new = pd.concat(noticel_new)
noticel = noticel.append(noticel_new).drop_duplicates(subset=['enlace'])
noticel.to_csv('noticel_alt.csv', index = False)

primerahora = pd.read_csv('primerahora_alt.csv')
url = 'https://www.primerahora.com/ultimas-noticias/'
ph = 'http://www.primerahora.com'
primerahora_new = []
get_primera_hora(url)
primerahora_new = pd.concat(primerahora_new)
primerahora_new['enlace'] = primerahora_new.enlace.apply(get_complete_link_primerahora)
primerahora = primerahora.append(primerahora_new).drop_duplicates(subset = ['enlace'])
primerahora.to_csv('primerahora_alt.csv', index=False)




