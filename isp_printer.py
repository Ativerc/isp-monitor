from colorama import Fore, Back, Style


def print_this(response_dict):
    pass
    if response_dict['Status'] != 'Active' or int(response_dict['Pending Amount']) > 0:
        print('Status: ' + Fore.RED + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print('Pending Amount: ' + Fore.RED + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)
        
    else:
        print('Status: ' + Fore.GREEN + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print('Pending Amount: ' + response_dict['Pending Amount'])

def print_verbose(response_dict): #TODO make verbose give 'Status'/'Pending Amount' in red and green depending on Status
    for keys,values in response_dict.items():
        print(keys + ": " + values) 
    
    if response_dict['Status'] != 'Active' or int(response_dict['Pending Amount']) > 0:
        print('Status: ' + Fore.RED + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print('Pending Amount: ' + Fore.RED + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)
        