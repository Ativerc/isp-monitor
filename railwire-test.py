import os 


import requests
from bs4 import BeautifulSoup as bsoup

railwire_username = os.environ['rw_username']
railwire_password = os.environ['rw_password']
railwire_url = os.environ['rw_url']

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': railwire_url,
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-GPC': '1',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': railwire_url, # /
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}



URL = railwire_url
request = requests.get(URL)


soup = bsoup(request.content, "html.parser")

ci_session_cookie = request.cookies['ci_session']
railwire_cookie_name = request.cookies['railwire_cookie_name']
captcha = soup.find(id="captcha_code").text.strip()
# print(captcha)
# print(ci_session_cookie, railwire_cookie_name)


cookies = {
    'ci_session': ci_session_cookie,
    'railwire_cookie_name': railwire_cookie_name,
}

data = {
  'railwire_test_name': railwire_cookie_name,
  'username': railwire_username,
  'password': railwire_password,
  'code': captcha,
  'baseurl': ''
}

response = requests.post(railwire_url, headers=headers, cookies=cookies, data=data) # /

if response.status_code == requests.codes.ok:
    content = response.content
    response_soup = bsoup(content, "html.parser")
    print(response.status_code)
    print(response_soup.prettify())