# -*- coding:utf-8 -*-
import urllib.request
import re

page = 1
url = 'https://www.qiushibaike.com/hot/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MISE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as eu:
    print(eu.code)
print(content)