from colorama import Fore, Back, Style
from datetime_proxy import months as dtproxy_months

# When Status == Active or Status == Disabled 
    # Values = 'Status', 'Name', 'Plan Name', 'Plan Renewal Date', 'Plan Expiry Date', 'Pending Amount',
        #  'Current Complaint Status', 'Service Provider Details'
    # Short Version Values = 'Status', 'Pending Amount', 'Plan Expiry Date'
# When Status == 'InActive'
    # Values = 'Status', 'Name', 'Plan Name', 'Plan Renewal Date', 'Plan Expired On', 'Pending Amount',
        #  'Current Complaint Status', 'Service Provider Details'
    # Short Version Values = 'Status', 'Pending Amount', 'Plan Expired On'
# RED States:
    # Active but Pending Amount > 0
    # Inactive 
    # Disable
# GREEN Status:
    # Active with Pending Amount == 0
def print_this(response_dict):
    
    if response_dict['Status'] == 'Disable' or response_dict['Status'] == 'InActive' or int(response_dict['Pending Amount']) > 0: 
        # For RED States:
            # (Active but Pending Amount > 0) or Disable
            # InActive
        print(Fore.WHITE + Style.BRIGHT + '\nStatus: ' + Fore.RED + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Pending Amount: ' + Fore.RED + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)
        if response_dict['Status'] == 'InActive':
            print(Fore.WHITE + Style.BRIGHT + 'Last Date for Payment: ' + Fore.RED + Style.BRIGHT + month_name(response_dict["Plan Expired On"]) + Style.RESET_ALL)
        else:
            print(Fore.WHITE + Style.BRIGHT + 'Last Date for Payment: ' + Fore.RED + Style.BRIGHT + month_name(response_dict["Plan Expiry Date"]) + Style.RESET_ALL)  
    elif ( response_dict['Status'] == 'Active' and int(response_dict['Pending Amount']) == 0 ): 
        # For GREEN States:
            # Active with Pending Amount == 0
        print(Fore.WHITE + Style.BRIGHT + '\nStatus: ' + Fore.GREEN + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Pending Amount: ' + Fore.GREEN + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Plan Expired On: ' + Fore.GREEN + Style.BRIGHT + month_name(response_dict["Plan Expiry Date"]) + Style.RESET_ALL)

def print_verbose(response_dict):
    
    if response_dict['Status'] != 'Active' or int(response_dict['Pending Amount']) > 0: #When Status != Active or Pending Amount > 0
        print_this(response_dict)
        print("\n:-------Details-------:\n")
        for key,value in response_dict.items():
            print(Fore.WHITE + Style.BRIGHT + key + Style.RESET_ALL + ": " + value) 
    else:
        print_this(response_dict)
        print("\n:-------Details-------:\n")
        for key,value in response_dict.items():
            print(Fore.WHITE + Style.BRIGHT + key + Style.RESET_ALL + ": " + value) 

def month_name(last_date):
    month = last_date.split("-")[1]
    month_name = dtproxy_months[month]
    return (last_date.split("-")[0] + " " + month_name + " " + last_date.split("-")[2])
