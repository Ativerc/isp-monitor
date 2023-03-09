import os 

import requests
from bs4 import BeautifulSoup as bsoup

railwire_username = os.environ['rw_username']
railwire_password = os.environ['rw_password']
RAILWIRE_URL = os.environ['rw_url']

session = requests.Session()

def perform_login(username=railwire_username, password=railwire_password):
    """
    Attempts to make a GET request to Railwire and on success,
    makes a POST request to login.

    Returns:
        BeautifulSoup object: A BS object of the response from 
        server post login.
    """
    request = session.get(RAILWIRE_URL)
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
    'Origin': RAILWIRE_URL,
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/Gecko/Firefox/65.0',
    'Referer': RAILWIRE_URL, # /
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    login_response = session.post(RAILWIRE_URL, headers=headers, cookies=cookiejar, data=data) 
    if login_response.status_code == 200:
        return bsoup(login_response.content, "html.parser")