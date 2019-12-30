#!/bin/python

import requests, argparse, getpass, os
from ignore.defaults import headers
from isp_parser import page_parser
from isp_printer import print_this, print_verbose


def passwordFetcher():
  password = getpass.getpass(prompt="Enter your password: ")
  # password_confirm = getpass.getpass(prompt="Confirm password: ")
  # while password != password_confirm:
  #   print("Passwords didn't match! Please re-enter your passwords again!")
  #   password = getpass.getpass(prompt="Enter your password: ")
  #   password_confirm = getpass.getpass(prompt="Confirm password: ")
  # else:
  #   print("Password confirmed!")
  return password


def instant_creds_fetcher():
  username = input("Enter your Username/UserID: ")
  password = passwordFetcher()
  instant_fetched_creds = {'username': username, 'password': password}
  return instant_fetched_creds 

#Argument Parser Code
parser = argparse.ArgumentParser(description="Get data from Jetspot's Account Page.")
parser.add_argument('-i', '--instant', action='store_true')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

#ifelse for credentials handling in "instant" vs "non-instant" mode of operation
if args.instant == True:
  instant_creds = instant_creds_fetcher()
  username = instant_creds['username']
  password = instant_creds['password']
  args.verbose = True  # If Instant option is chosen, then output mode is immediately set to verbose
else:
  username = os.environ['USERNAME'] 
  password = os.environ['PASSWORD']




def responser():
  #Start Session with ISP's Login Page
  s = requests.session()
  login_url = os.environ['URL']
  #initial_response = s.get(login_url, verify=False)
  cookiejar = s.cookies
  data = {
    'LoginForm[username]': username,
    'LoginForm[password]': password,
    'yt0': 'Log In'
  }
  response = s.post(login_url, cookies=cookiejar, data=data, headers=headers, verify=False)  #ssl_certificate verification fails for some reason; hence set verify=False
  response_dict = (page_parser(response))
  return response_dict

if __name__ == '__main__':

  if args.verbose == True:
    print_verbose(responser())
  else:
    print_this(responser())