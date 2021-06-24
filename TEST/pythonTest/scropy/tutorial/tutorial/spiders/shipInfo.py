import json
import scrapy
from scrapy import http


class shipsSpider(scrapy.Spider):
    name = "ships"
    cookies = {
        'Human_Search': '1',
        '_ga': 'GA1.2.1186340523.1623822921',
        '_gid': 'GA1.2.1960302639.1623822921',
        '_pk_id.1.bb70': '72d0077eb1021b8e.1623822921.',
        '_pk_ses.1.bb70': '1',
        'TLCOOKIE': '7e6ccc989ee1c1e7d0471ce1714c2b88',
        'TS01280c6f': '01d4e8f3f5eb7e4c2be95dee6b8e6424da0b02a9d2675f4b073f6bfe2c53a84950d2f3a54bd1560f0ca3aefba1d9aab04566b9ba9a8832426155aeee6222bc02bb8c95693c0e8e5456bf59564ad0a086e5ad88dc3d',
        'TS01121815_28': '01d045bf444d2908624040f8a1238b5c8ac97d2acfd8ca23ad3c65288db439be8ba38907340a7fc03cae3cba55a85ad1044fa9a691',
        'f5avrbbbbbbbbbbbbbbbb': 'CCPDCGJOKDDMEGGLMBIIJPOKOPGNNDHEFAFDPCOEDKENCDAKAKJHPFPENAOPFLIEFJKDLLIFIFIDOBHGKLFAOJINBJHAKLGEHDKHFILIDPFFDFHMMEJMJJAGKOGPKOMD',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Jun+16+2021+14^%^3A28^%^3A50+GMT^%^2B0800+(^%^E4^%^B8^%^AD^%^E5^%^9B^%^BD^%^E6^%^A0^%^87^%^E5^%^87^%^86^%^E6^%^97^%^B6^%^E9^%^97^%^B4)&version=6.18.0&isIABGlobal=false&hosts=&consentId=04ef3a48-ff21-405e-b30a-46219fc8e29f&interactionCount=1&landingPath=NotLandingPage&groups=C0001^%^3A1^%^2CC0002^%^3A1^%^2CC0003^%^3A1^%^2CC0004^%^3A1&AwaitingReconsent=false',
        'TS01121815': '01d4e8f3f5069bc2f52c97f6b0fbda2cc5c31203567ed9606e1fa233b6bf63b7d3913d0209d579aabd556e90e9a9abff2eaed4ebb4',
        '_gat_UA-43050752-19': '1',
        }
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://www.cma-cgm.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'Accept': '*/*',
        'Referer': 'http://www.cma-cgm.com/ebusiness/tracking/search',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'authority': 'ec.walkme.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'accept': 'text/html, */*; q=0.01',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'http://www.cma-cgm.com/ebusiness/tracking/search',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '0',
        'content-type': 'text/plain',
        'origin': 'http://www.cma-cgm.com',
        'upgrade-insecure-requests': '1',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Length': '0',
    }

    data = {
        '2': '',
        'g-recaptcha-response':'03AGdBq26lWJhB9FZkZUf7fuH5HYOvwdRYqUdIiRvjpei5qoTjvBP6-Ht1mNeiZh_vX5qqMRiPBetRV5vcrEXlCVNZLQDQM2w1y-ijIMMjDFPK7SmdKra69Qzr2aws15LQbAZRDeCe05kjWXAGudv697pmrA-GcOSzqEX4ya7E6KUfiIInhAOpDTzWwGnNWJ2oPQcOA3k6dvZ3YUl-n9MiECwJiiou9g0FcclEwoDJtx-ZrKrz6jp6YxM5vXCBIWKyrjW_iuNsNRhCY2Yz8-VqLVquctBSOCwj_hFZU55C5MNs3ePijKGT0dMvAZI6NnYZ6PC5txWxh1W9znuOr97ZNfGBNvYexrqltZ8OCrFrOCM7RDoRDfqozjUf8NaQ-aTQ5Frpf93qHWEJjLMM__en7nUn558nqP0PKsq5xzE1pPwaa-gOneH-cUEZG8tlnmQG1HpT6SJJunGivQhjWqJdE7l7TcuJQX0Po9Y9cXb8HLSUt0D-LKCcyFn-k7bDXVrzzBUSjjsJWa7nBKIFZpzHHI87uXbnJe9CvRdjZz0iKDDVGZ8xb6wGpha5eMkYCf72msgydVHdFWdwgmjO_6cQhqkWM15HrHdKSj4IdAyaDjY6Dd71k2i9ko7OkggvbZuBQS4ZLlGAamESBjIi_x6gN5xJIwSTuVrG9WgAT6Rhd-jP3m1X2RSHgryzbvQjC5_ujBQgwgOpaQd4t0CgdxuhxTO3L91cMm93aTIdThElq1lgLPtselcatdoE1H9O9uwiAuYIHvznnGdQaWrX_VTXSUeqPMU5FJ0UCv5nmBmqku4UWUJx5EnSIHei_M1T_IV7KZwpDEKqZOdoy0eEzOufjNPr48pb_9NVU5yS1OHQRMFf2nCdaoPzaaePNUa8L_QUX2juDYPnIivvr_Y2osjmaX5UH0YNiSFocdclxT53VPQEoHm5p4KzMnGsJ8-jbNEtqOznd33Sqo_wPu5hxq9P294TXJyj36At8hyq0FGpkUDGX1a5Q_h_-BpkiWKpEQ0ThNPN3wGY7hNs2XbUXDFSAR21LpQJXvcQKQDIB0ZjlLjdMPsuI309sIKBkD7KsNUODJaBdqEsInd96TKgY5TZU-Nt70RPSCvw2k7Xf1SWpUzi5y2natyxmqWtyaayrhN9C3BGpF_BOraTAQ1qxKi6xhkoEOmSCg3tzsVMo5SMX85hbB7nXDGR98EQEj2jpQqtZwVdRwiMMGN9tVGKJuCU81tI6gtKRyh8WrfslcUZrzW1t7JJkRO_dwV0968vP4m4-KA1oYil-pqH6PBTpnTElcB87cExckNIqCMuiCSIwoYZGmpRRJRMGwbRlwkRWquODF4I-LbI0ZGFDGzd95voA7tJSGmxiVxi3YxICG8VHZ9Evq6vcXHktMQ9CojxsSKvETZD22Gyp09OY3ksYosEjeO7R6pFVw9QbVXm_bN_Wfy1btP-9cLUWwWWY7nqcibZRHaFfZs66J-eYp4ing5YahBBSTnIDvmfjwjzsI2oiWGHfCFAc0u1UUJCBfdclE3LqqqqJAi1RBSLIkvsjCuN0k2yOT-Sn2dLdj6_Hncx_SgWeZfk2khBpzc',
        'SearchBy': 'Container',
        'Reference': 'SHZ3692018',
        'FromHome': 'true',
        '^^{^\\^_static^\\^:true,^\\^Wm-Client-Timestamp^\\^:1623825168532^}^ ^{^\\^_enc^\\^:^\\^bbd^%': 'rk^|=3b/ 2^%=zqpezrvk=3zls~y^%=zsv^}pr=3b/-',
        '.^%': 'wk^{vh=3//.^%=kwxvzw=d^%=qzzm^|l=3b=/.=^%=qpvlmzi=3=lhp^{qvH=^%=zr~q=d^%=lp=3b= 1 )1/1.',
        '': '^%=qpvlmzi=3=zx^{Z=^%=zr~q=d^%=mzlhpm^}=d^%=iqz=3b=( .--zzyy^{-z2)^{',
        '^{/ 2/^|-^{2(.z),* -': '^%=^{Vjzl^|=3.^%=rmpyk~so=3/^%=iqz=3.2^%=^{Vrmzo=3=zw^|~^\\^\\^\\^\\=^%=z^|mjpL^{Vjz=3= ~)',
        'y() *^}y2()': '',
        '2.,^} 2-***2^|)': '',
        '^|)^{^}': '^%=^{Vjz=3=/,* .z.~~y)-(z^}z,z /^{)y ^|*^|,~^{=^%=^{Vj=d^%=rh=3=^}*.-^{*^})^{-*/2 ),2(',
        '* 2^} ~2/^} * ^{.(': '^%=^{Vl=3b=-1/1*=^%=zo=3=)/. (^|',
        'y2': '',
        '-': '',
        ',/.2-*/.-/-': '^%=^}vs=3= *1/1*=^%=~m^}~=d^%=qpvlmzi=3b=xqvt^|~mk0llzqvlj^}z0rp^|1rx^|2~r^|1hhh00^%^okkw=^%=mzmmzyzm=3=xqvt^|~mK?kqzrovwL?c?RX^\\^\\^\\^\\?^^R^\\^\\^\\^\\=^%=zskvk=3=',
        '^}z^|()^{~-': '',
        ',((z': '',
        '*': '',
        ', y - ^{)../': '',
        ',': '^%=^{Vkvlvi=3zls~y^%=zr~myVlv=3b=xqvt^|~mk0llzqvlj^}z0=^%=zr~qwk~o=3=rp^|1rx^|2~r^|1hhh=^%=zr~qklpw=3=^%^okkw=^%=sp^|pkpmo=d^%=qpvk~^|ps=3=.^{z^|/-y^{/y^|-/y^}^{^}~ ^{/))/^|-y^{^}',
        ')': '^%=^{Vqvh=3b*,-^%=zrvK^{~ps=3/*( -',
        ' -,-).^%': 'km~kLi~q=d^%=xqvrvk=d^%=gk^|=3,/  .*-,-).^%=zrvk=3b=w^|m~zL=^%=kgzk=3=B=Cxqvt^|~mKqk^}=C^\\^\\^\\^^{vDQPKKJ^]=^%=fmzjNpkj~=3=kvr^}jl^\\^\\^\\^zofk9w^|m~zl^\\^\\^\\^zr~q9fm~rvmo1qpkkj^}2p1xqvt^|~mKqk^}^<B.Dqpkkj^}0qpvk^|~1B-Do0qztpKzk~mzqzX^<B.Drmpy0B.Dkzl^{szvy0kqzkqp^|2kyzs1B.Div^{0mzoo~mh2qv~r1B.Div^{0mzoo~mh2w^|m~zl1B.Dqpvk^|zl0qv~r^@^@zqpe2s1xqvt^|~mkkqzrovwl^<B.Dqv~r0qv~r^@^@zqpe2s1B-Div^{0f^{p^}^<B.Df^{p^}0B.Dsrkw=^%=wk~og=d^%=kqzrzsz=3=qhp^{zljpr=^%=zofk=d^\\^^}^ ^ --compressed ',
        ' curl https://monitor-china1.cma-cgm.com/cedexis/r20.gif?rnd': '1-1-14542-1-14542-33798-2693375613-_CgJqMRAUGHsiBQgBEM5xKP3MpoQKMPu1poYGOPi1poYGQNuBgtQFShAIBBAsGK_JAyAAKIuDgKAEUABaCggAEAAYACAAKABgAWoTYnV0dG9uMi5oa2cuaHYucHJvZIIBDwgEECwYpiAgACiLg4CgBIgB-caQgwWQAQCYAQA ^ -H Connection:'
    }

    def start_requests(self):
        urls = ['http://www.cma-cgm.com/ebusiness/tracking/search']
        for url in urls:
            yield scrapy.Request(url=url, method='POST',
                                    callback=self.parse,
                                    headers=self.headers,
                                    cookies=self.cookies,
                                    body=json.dumps(self.data))

    def parse(self, response: http.HtmlResponse, **kwargs):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # next_page =response.urljoin(next_page)
            # yield scrapy.Request(next_page,callback=self.parse)
            yield response.follow(next_page, callback=self.parse)
