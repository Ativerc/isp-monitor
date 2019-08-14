from colorama import Fore, Back, Style
from datetime_proxy import months as dtproxy_months

def print_this(response_dict):
    if response_dict['Status'] != 'Active' or int(response_dict['Pending Amount']) > 0: #When Status != Active or Pending Amount > 0
        print(Fore.WHITE + Style.BRIGHT + '\nStatus: ' + Fore.RED + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Pending Amount: ' + Fore.RED + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Last Date for Payment: ' + Fore.RED + Style.BRIGHT + month_name(response_dict["Plan Expiry Date"]) + Style.RESET_ALL)      
    else: 
        print(Fore.WHITE + Style.BRIGHT + '\nStatus: ' + Fore.GREEN + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Pending Amount: ' + Fore.GREEN + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Plan Expiry Date: ' + Fore.GREEN + Style.BRIGHT + month_name(response_dict["Plan Expiry Date"]) + Style.RESET_ALL)

def print_verbose(response_dict):
    
    if response_dict['Status'] != 'Active' or int(response_dict['Pending Amount']) > 0: #When Status != Active or Pending Amount > 0
        print_this(response_dict)
        print("\n:-------Details-------:\n")
        for keys,values in response_dict.items():
            print(Fore.WHITE + Style.BRIGHT + keys + Style.RESET_ALL + ": " + values) 
    else:
        print_this(response_dict)
        print("\n:-------Details-------:\n")
        for keys,values in response_dict.items():
            print(Fore.WHITE + Style.BRIGHT + keys + Style.RESET_ALL + ": " + values) 

def month_name(last_date):
    month = last_date.split("-")[1]
    month_name = dtproxy_months[month]
    return (last_date.split("-")[0] + " " + month_name + " " + last_date.split("-")[2])