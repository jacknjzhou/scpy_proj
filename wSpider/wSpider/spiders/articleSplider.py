#!-*-encoding:utf8-*-
import re
import scrapy
from wSpider.items import Article
#from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(scrapy.Spider):
    name="article"
    allowed_domains =["jd.com"]

    #a_item = "https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page={0}&s={1}&click=1"

    #start_urls = ["https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=1&s=1&click=1"]

    start_urls = ["https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=1&s=1&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=3&s=61&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=5&s=121&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=7&s=181&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=9&s=241&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=11&s=301&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=13&s=361&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=15&s=421&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=17&s=481&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=19&s=541&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=21&s=601&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=23&s=661&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=25&s=721&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=27&s=781&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=29&s=841&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=31&s=901&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=33&s=961&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=35&s=1021&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=37&s=1081&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=39&s=1141&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=41&s=1201&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=43&s=1261&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=45&s=1321&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=47&s=1381&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=49&s=1441&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=51&s=1501&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=53&s=1561&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=55&s=1621&click=1",
"https://search.jd.com/Search?keyword=Python&enc=utf-8&qrst=1&rt=1&stop=1&book=y&vt=2&stock=1&page=57&s=1681&click=1"]
    #rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'),), callback="parse_item", follow=True)]
    #rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),), callback="parse_item", follow=True)]
    
    def parse(self,response):
        #r_info =[]
        #a_item = Article()
        f= open('result.txt','a')
        #print response.body
        #title = response.xpath('//body/div/text()')[0].extract()
        info = response.css('#J_goodsList').xpath('//ul/li/div')
        #print info
        for item in info:
            tt = item.css('div[class*=p-name] > a > em').extract()
            if tt:
                print tt[0].encode('utf-8')
                att = tt[0].encode('utf-8')
                dr = re.compile(r'<[^>]+>',re.S)
                dd = dr.sub('',att)

                f.write(dd+'\t')
                #a_item['title'] = tt[0].encode('utf-8')
            else:
                pass
                #a_item['title']=""
                #print len(tt) 
            pp = item.css('div[class*=p-price] > strong > i').extract()
            if pp:
                #a_item['price'] = pp[0].encode('utf-8')
                print pp[0].encode('utf-8')
                att = pp[0].encode('utf-8')
                dr = re.compile(r'<[^>]+>',re.S)
                dd = dr.sub('',att)

                f.write(dd+'\t')
                #f.write('********************************\n')
                print "*"*30
            else:
                pass
                #a_item['price']=0
            cc = item.css('div[class*=p-market]>').extract()
            if cc:
                #a_item['price'] = pp[0].encode('utf-8')
                print cc[0].encode('utf-8')
                att = cc[0].encode('utf-8')
                dr = re.compile(r'<[^>]+>',re.S)
                dd = dr.sub('',att)

                f.write(dd)
                #f.write('********************************\n')
                print "*"*30
            else:
                pass
            f.write('\n')
            #r_info.append(a_item)
        f.close()
        #print "Title is:"+title
        #print dir(response)
        #print response.selector

        #item['title'] = title
        #print r_info
        #return r_info

    def demo(self):
        pass
