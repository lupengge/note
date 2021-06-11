from ast import Num
from math import floor
from scrapy import http
import scrapy
import pandas as pd
from alive_progress import alive_bar


class companySpider(scrapy.Spider):
    name = "companyInfo"
    compantNames=[]
    headers={
            'authority': 'tongji.qichacha.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '^\\^',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
            'accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'image',
            'referer': 'https://www.qcc.com/',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'QCCSESSID=qhn8edlkm1lpm6in90su0ed8l1; zg_did=%7B%22did%22%3A%20%22179f3fac04d704-0184697e730c5b-51361542-1fa400-179f3fac04ecef%22%7D; _uab_collina=162329596795598557878097; acw_tc=71606d2116233854728326494e8d13f8b19397ad8a2fed4fa4c2db2669; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201623385477354%2C%22updated%22%3A%201623385480295%2C%22info%22%3A%201623295967314%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E4%BC%81%E6%9F%A5%E6%9F%A5%E7%BD%91%E7%AB%99%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22undefined%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D',
            'origin': 'https://www.qcc.com',
            'Referer': '',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
        }
    def start_requests(self):
        table = pd.read_excel(r'C:\Users\lpg\Desktop\myNotes\TEST\pythonTest\scropy\tutorial\tutorial\法人.xls')
        self.compantNames = list(table['name'])
        with alive_bar(len(self.compantNames)) as bar:
            for name in self.compantNames:
                bar()
                yield scrapy.Request(url='https://www.qcc.com/web/search?key='+name,headers=self.headers,callback=self.parse,method='GET')

    def parse(self, response: http.Response, **kwargs):
        response.request
        companyLinks = response.css('a.title::attr(href)').extract()
        
        yield scrapy.Request(url=companyLinks[0],headers=self.headers,callback=self.parse_company)


    def parse_company(self,response:http.Response):

        def extract_with_css():
            trs=response.css('table.ntable tr')
            out={}
            for trSelector in trs:
                tds =trSelector.css('td::text').extract()
                name=""
                for index,td in enumerate(tds):
                    if (index+1)%2==0:
                        out[name]=td.rstrip().lstrip()
                    else:
                        name=td.rstrip().lstrip()

            return out
        out=extract_with_css()
        
        
        yield out
