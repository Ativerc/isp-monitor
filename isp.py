#!/bin/python

import requests, argparse, getpass, os
from isp_printer import print_this, print_verbose
from isps.jetspot.jetspot import jetspot_main, responser

isp_options = {1: "Jetspot"}

def isp_selector(): # Asks user for their ISP
  for i, j in isp_options.items():
    print(f"{i}. {j}")
  confirm=""
  selected=""
  while confirm != "Y": 
    selected = input("Enter the corresponding number for the ISP.\n")
    confirm = input(f"Selected Option: {selected} which is for: " +
    f"{isp_options[int(selected)]} \nConfirm your ISP is {isp_options[int(selected)]} ? Y/N: ") 
  return selected

#Argument Parser Code
parser = argparse.ArgumentParser(description="Get data from ISP's Account Page.")
parser.add_argument('-i', '--interactive', action='store_true')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()

#ifelse for credentials handling in "interactive" vs "normal" mode of operation

if args.interactive == True: # If "interactive" option is chosen; instant_creds_fetcher() is called; output mode is set to verbose
  selected_isp = isp_selector()
  args.verbose = True  
else: # for "normal" mode, the credentials are fetched from the environment variables
  selected_isp = os.environ['ISP']

def response_dict_return(selected_isp, username, password): # For use by other CLI tools
  if selected_isp == 1 or "JETSPOT":
    isp_dict = responser(username, password)
  return isp_dict

if __name__ == '__main__':
  if (selected_isp == 1 or "JETSPOT"):
      jetspot_main(args.verbose, args.interactive)
  # if args.verbose == True:
  #   print_verbose(responser())
  # else:
  #   print_this(responser())