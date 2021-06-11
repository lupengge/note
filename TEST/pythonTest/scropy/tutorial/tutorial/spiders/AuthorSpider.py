from email.policy import default
from scrapy import http
import scrapy

# ---------------------------------------------------------------------------- #
#           命令：scrapy crawl author -O quotes-humor.json -a tag=humor         #
# ---------------------------------------------------------------------------- #


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response: http.Response, **kwargs):
        author_page_links = response.css('.author + a')

        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response: http.Response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
