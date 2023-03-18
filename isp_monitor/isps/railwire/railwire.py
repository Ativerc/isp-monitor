import os 

import requests
from bs4 import BeautifulSoup as bsoup

SAVED_USERNAME = os.environ['rw_username']
SAVED_PASSWORD = os.environ['rw_password']
SAVED_URL = os.environ['rw_url']



def perform_login(username=SAVED_USERNAME, password=SAVED_PASSWORD, railwire_url=SAVED_URL):
    """Attempts to make a GET request to Railwire and on success,
    makes a POST request to login.

    Args:
        username (string, optional): Railwire Login Username. Defaults to SAVED_USERNAME.
        password (string, optional): Railwire Login Password. Defaults to SAVED_PASSWORD.
        railwire_url (string, optional): Railwire Login URL. Defaults to SAVED_URL.

    Returns:
        BeautifulSoupObject: A BS object of the response from 
        server post login.
    """
    session = requests.Session()
    request = session.get(railwire_url)
    soup = bsoup(request.content, "html.parser")
    ci_session_cookie = request.cookies['ci_session']
    railwire_cookie_name = request.cookies['railwire_cookie_name']
    captcha = soup.find(id="captcha_code").text.strip()

    cookiejar = {
        'ci_session': ci_session_cookie,
        'railwire_cookie_name': railwire_cookie_name,
    }

    data = {
    'railwire_test_name': railwire_cookie_name,
    'username': username,
    'password': password,
    'code': captcha,
    'baseurl': ''
    }

    headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': railwire_url,
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/Gecko/Firefox/65.0',
    'Referer': railwire_url, # /
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    login_response = session.post(railwire_url, headers=headers, cookies=cookiejar, data=data) 
    if login_response.status_code == 200:
        return bsoup(login_response.content, "html.parser")