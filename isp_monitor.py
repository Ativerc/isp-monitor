import requests, argparse, getpass
from ignore.credentials import credentials_dict
from ignore.defaults import headers
from isp_parser import page_parser
from isp_printer import print_this, print_verbose
from datetime_proxy import months as dtproxy_months

def passwordFetcher():
  password = getpass.getpass(prompt="Enter your password: ")
  password_confirm = getpass.getpass(prompt="Confirm password: ")
  while password != password_confirm:
    print("Passwords didn't match! Please re-enter your passwords again!")
    password = getpass.getpass(prompt="Enter your password: ")
    password_confirm = getpass.getpass(prompt="Confirm password: ")
  else:
    print("Password confirmed!")
  return password


def instant_credentials_fetch():
  fetched_creds = {}
  username = input("Enter your Username/UserID: ")
  password = passwordFetcher()
  fetched_creds = {'username': username, 'password': password}
  return fetched_creds 


parser = argparse.ArgumentParser(description="Get data from Jetspot's Account Page.")
parser.add_argument('-i', '--instant', action='store_true')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

s = requests.session()
login_url = credentials_dict['login_url']


if args.instant == True:
  instant_creds = instant_credentials_fetch()
  username = instant_creds['username']
  password = instant_creds['password']
  args.verbose = True
else:
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

print("Fetching data....")
response = s.post(login_url, cookies=cookiejar, data=data, headers= headers, verify=False)

response_dict = (page_parser(response))
# Add datetime module
# can't find datetime module's docs at the moment. 
# Let's implement some of my own stuff
# heck I hope response_dict has a key named "Last Date"
date = response_dict["Plan Expiry Date"]
month = date.split("-")[1]
month_name = dtproxy_months[month]
print(date.split("-")[0] + " " + month_name + " " + date.split("-")[2])

if args.verbose == True:
  print_verbose(response_dict)
else:
  print_this(response_dict)