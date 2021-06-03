import scrapy

class QuotesSpider(scrapy.Spider):
  name = "quotes"

  def start_requests(self):
      urls=[
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
      ]
      for url in urls:
        yield scrapy.Request(url=url,callback=self.parse)

  def parse(self, response, **kwargs):
      page = response.url.split("/")[-2]
      fileName=f'quotes-{page}.html'
      with open(fileName,'wb') as f:
        f.write(response.body)
      self.log(f'\x1b[33mSave file {fileName}\x1b[0m')