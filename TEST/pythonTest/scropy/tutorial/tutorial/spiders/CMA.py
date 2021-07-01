# from scrapy import http
# import scrapy


# class CmaSpider(scrapy.Spider):
#     name = 'CMA'
#     allowed_domains = ['cma-cgm.com/']
#     start_urls = ['http://cma-cgm.com//']

#     def start_requests(self):
#         return super().start_requests()


#     def parse(self, response:http.Response):
#         print(response.body)

import requests
import 

cookies = {
    'Human_Search': '1',
    'webCookiePreference': 'analytics=true^%^2Cbrainsonic=true^%^2Celoqua=true',
    'TLCOOKIE': 'd871ed2b910a9317216061470f55a1a6',
    'TS01121815': '01d4e8f3f5e9a711dd616a688d800261a02c02e81d1c2734c5db9b82e6102152fac040b33774878f3ea1cd12c7a4f319420d52aef6',
    'TS01121815_28': '01d045bf449921538d494b8bdf223e01229aeee79d12200b6a545b882e6131d826d6b6bb20d48b772d96baf8023c2af77705d4b581',
    'TS01280c6f': '01d4e8f3f54ed81f23774a4e705fda30d438d521a11c2734c5db9b82e6102152fac040b337b9086d6f26754fa941a64ba498cc60a510dc731763d69ff4f9a163f7d8afb5c44b883b90d613f6a6f89e7f58a785619c',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://www.cma-cgm.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
    'Accept': '*/*',
    'Referer': '',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'sec-ch-ua': '^\\^',
    'sec-ch-ua-mobile': '?0',
    'authority': 'cdn.walkme.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'http://www.cma-cgm.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'origin': 'http://www.cma-cgm.com',
    'upgrade-insecure-requests': '1',
    'content-type': 'text/plain;charset=UTF-8',
}

data = {
  'g-recaptcha-response': '03AGdBq270LMFA-nmOJNAfX-B-zGLQvlZr3PvGvGfYmQwsbSeAVz3J9L4MnZFkN0DifZzZrDCfBaq7fbQZE5DQgD_5_j6aegpSs7DHaC6iB99tXjl8DuYkA2LSWmG8rM5vvraoBknwJ5qn_wsgH-RWNRae0T0QO56zf0Z_O0YF2_tbM3CYKvn8Q7zSsubQ1BCE1EuEuAdWl52hrrmi82F9UNM1DojbpcqtGFtuaro-kIcECI7tI6AF2J1KPljNK6t4g_7kK5wMXOGR5zaIjXjP7iqUaPSmkJH1JnIWVyZCRiENaMW9oIpL1teHiV78ybN6DbuRt9cviXDS6nkfRwfinLQyzeqCtPGSROWaFXW8pEQJozstVfmhfkXMOnkF0gmpsJtNa75vooNt2o8-EFmg37jbEP6FTkyKAfuoGivfkmAYgjRnCeWgC2kjxrdrwnjZewtu4RuQ55rcYTZHu83wyDCnzubXLD-sBUX0V0Jm00lhXSQBLR_NxYZjT8AnAJ8VUeBt5sPIebmZauIMPxe7dINoWUaTc7NhKQkiLbIMMGTGJEx0rH_kRdlt2AOvm9uj2k7h_mPXMDAiUep4qKoTgyCISy91es_jY4VHLdSCk9NBGxXSiEwfklVdmPBquvbFOsxFqHLHIJbsWN_0d2o_w6nfmKhxyV0iW5Z2ftfvidDIQhmfMEhRGHQ6rU_Uxbjr89ymuTnhDaIhL7Mze-usx8GNreFm9jN98Uhn0-dI3gwsq3JtbnyFZ0ehTzCcLTdWiAqYEhTKzG21xwH2OhotToeoog-X0Ed1Ha6G9SxMXZAD-G7bSI01HwTLqzubZep11wzonGeMv5fQlWyQpFN7c3KGVXjTdGLac2RjamtAjR7qlPxtq8cLbD7KnCf4Z6sjjSq3GjM-6Zd8jPcFMDYW2d-Gk3KcmsQDOsHUVrpy63DSi_4RVQN7HlA76CfawNPGMcl1xG9WghKIkKG_ss1KNOjNflCn4kfYwXFoY9cg6FDTzkV-5Zjhqd4Uah9IL-xYp9wffdC34u0ZNfcd4p3i41cWn3lzycRPesfNxrzXhysuXpILLitP-S8xUVz0faQ_P60HZ6A8nNC4ikElCKEYuSsl9Y3SkESAxbBd_TdgVsKkxUGkDBGVdiDJwT49FXZjiZXgLSaq0NVNNjZKEibGzTVDlKW7oU3hqxhWnyE-7kyMARIuKxFq0Gtov8nmS94SsuWU_j5U6_efehs9EHSiGRjCFRMdWDzHPF_xlnFyB0PPwPeBqMbFAPhiyXFMjgbmo5A04MH-qvifAPn1OtX0L-gdlnx1j48LNL_PP1HvpJYZel5CTWkjcsoCK6hf4WEBSfXFEtoTusWCkavuUywhi57j0EtDA2mC6HSkBr8N5UcCXLAVN2hqjb99nQ2I75fgWGnC5WwWRiblKMahloMbTxus89FyjBpUeQ3Og4G2nXcEQwsW-BALtp9Yu_lIvJjCokP28gT46ydNjrMbrzwJ6t08ONJA3Bgbvr9q_sgqIcJjcqRY_yo2pmY1EicsYhnPmcIFTNQbuT7AlWIVOCkOdmmZA_JWXb1PUqyP8yPBN1fkxOIt-uSiqeI',
  'SearchBy': 'Container',
  'Reference': 'NAM3142099',
  '^{^\\^apiToken^\\^:^\\^da3c5c4f68d04e3ebe7826faa1e14530__0^\\^,^\\^sessionId^\\^:^\\^97254065-432e-45b7-be60-2f0a3ff75cda^\\^,^\\^isManualStart^\\^:false,^\\^uid^\\^:^\\^d0c343f4-c2e7-40d7-ab37-e14f62e9f7d0^\\^,^\\^clientVersion^\\^:^\\^1.104.6^\\^,^\\^viewportWidth^\\^:879,^\\^viewportHeight^\\^:763,^\\^screenWidth^\\^:1536,^\\^screenHeight^\\^:864,^\\^timestamp^\\^:1623422712606700,^\\^hostname^\\^:^\\^www.cma-cgm.com^\\^,^\\^referer^\\^:^\\^http://www.cma-cgm.com/ebusiness/tracking^\\^^}': '',
  '^^{^\\^_static^\\^:true,^\\^Wm-Client-Timestamp^\\^:1623422712890^}^ ^{^\\^time^\\^:1623422712634,^\\^type^\\^:^\\^pageChange^\\^,^\\^sId^\\^:^\\^97254065-432e-45b7-be60-2f0a3ff75cda^\\^,^\\^wm^\\^:^{^\\^uId^\\^:^\\^da3c5c4f68d04e3ebe7826faa1e14530^\\^,^\\^euId^\\^:^\\^21a2236b-7e2b-4064-b8c6-d56f38e992dd^\\^,^\\^euIdSource^\\^:^\\^Cache^\\^,^\\^permId^\\^:-1,^\\^env^\\^:0,^\\^platform^\\^:1,^\\^cseuId^\\^:^\\^c9f96eb1-f280-420c-bf1d-4521adfbd43e^\\^^},^\\^env^\\^:^{^\\^browser^\\^:^{^\\^name^\\^:^\\^Edge^\\^,^\\^version^\\^:^\\^91.0.864.41^\\^^},^\\^os^\\^:^{^\\^name^\\^:^\\^Windows^\\^,^\\^version^\\^:^\\^10^\\^^},^\\^screen^\\^:^{^\\^height^\\^:864,^\\^width^\\^:1536^},^\\^mobile^\\^:false,^\\^timezone^\\^:-480^},^\\^ctx^\\^:^{^\\^location^\\^:^{^\\^protocol^\\^:^\\^http:^\\^,^\\^hostname^\\^:^\\^www.cma-cgm.com^\\^,^\\^pathname^\\^:^\\^/ebusiness/tracking/search^\\^^},^\\^isIframe^\\^:false,^\\^visitId^\\^:^\\^a4b50e52ad484b5b99e84558f308d913^\\^,^\\^title^\\^:^\\^CMA': '',
  '^^{^\\^_static^\\^:true,^\\^Wm-Eu-Data^\\^:^{^\\^d^\\^:^\\^Edge^\\^,^\\^e^\\^:^\\^91.0.864.41^\\^,^\\^w^\\^:false,^\\^y^\\^:^\\^Windows^\\^,^\\^h^\\^:0,^\\^euId^\\^:^\\^21a2236b-7e2b-4064-b8c6-d56f38e992dd^\\^,^\\^j^\\^:^\\^Cache^\\^,^\\^aa^\\^:-1,^\\^ab^\\^:1,^\\^uId^\\^:^\\^da3c5c4f68d04e3ebe7826faa1e14530^\\^,^\\^s^\\^:^\\^20210509-112115-e5083ee6^\\^,^\\^ac^\\^:1621590684025,^\\^bc^\\^:^[^\\^ConditionOrderOptimizer_fast^\\^,^\\^^!4^\\^,^\\^jsonDataFile^\\^,^\\^^!5^\\^,^\\^^!2^\\^,^\\^^!1^\\^,^\\^^!3^\\^,^\\^^!6^\\^^]^},^\\^Wm-Client-Timestamp^\\^:1623422717566^}^ ^{^\\^ns^\\^:^\\^feperf^\\^,^\\^data^\\^:^{^\\^q^\\^:9,^\\^g^\\^:25117,^\\^timestamp^\\^:1623422712551^}^}^ ^{^\\^ns^\\^:^\\^feperf^\\^,^\\^data^\\^:^{^\\^q^\\^:11,^\\^g^\\^:2761,^\\^ai^\\^:0,^\\^al^\\^:^\\^none^\\^,^\\^ak^\\^:0,^\\^timestamp^\\^:1623422712630^}^}^ ^{^\\^ns^\\^:^\\^feperf^\\^,^\\^data^\\^:^{^\\^q^\\^:12,^\\^g^\\^:22807,^\\^ai^\\^:67,^\\^al^\\^:^\\^none^\\^,^\\^ak^\\^:20046,^\\^timestamp^\\^:1623422712631^}^}^ ^{^\\^ns^\\^:^\\^feperf^\\^,^\\^data^\\^:^{^\\^q^\\^:13,^\\^g^\\^:25082,^\\^ai^\\^:1649,^\\^al^\\^:^\\^none^\\^,^\\^ak^\\^:22321,^\\^timestamp^\\^:1623422712632^}^}^ ^{^\\^ns^\\^:^\\^feperf^\\^,^\\^data^\\^:^{^\\^q^\\^:14,^\\^g^\\^:25981,^\\^ai^\\^:3174,^\\^al^\\^:^\\^none^\\^,^\\^ak^\\^:23220,^\\^timestamp^\\^:1623422712633^}^}^': ''
}

response = requests.post('http://www.cma-cgm.com/ebusiness/tracking/search', headers=headers, cookies=cookies, data=data, verify=False)

print(response)