import requests
from ignore.credentials import credentials_dict
from ignore.defaults import headers
from isp_parser import parser
from isp_printer import print_this


s = requests.session()
login_url = credentials_dict['login_url'] 
username = credentials_dict['username'] 
password = credentials_dict['password']  

initial_response = s.get(login_url, verify=False)


cookiejar = s.cookies

data = {
  'LoginForm[username]': username,
  'LoginForm[password]': password,
  'yt0': 'Log In'
}

headers = headers

response = s.post(login_url, cookies=cookiejar, data=data, headers= headers, verify=False)

response_dict = (parser(response))

print_this(response_dict)