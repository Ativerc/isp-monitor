from colorama import Fore, Back, Style


def print_this(response_dict):
    pass
    if response_dict['Status'] != 'Active' or int(response_dict['Pending Amount']) > 0: #When Status != Active or Pending Amount > 0
        print(Fore.WHITE + Style.BRIGHT + '\nStatus: ' + Fore.RED + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Pending Amount: ' + Fore.RED + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)       
    else: 
        print(Fore.WHITE + Style.BRIGHT + '\nStatus: ' + Fore.GREEN + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Pending Amount: ' + Fore.GREEN + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)

def print_verbose(response_dict): #TODO make verbose give 'Status'/'Pending Amount' in red and green depending on Status
    
    if response_dict['Status'] != 'Active' or int(response_dict['Pending Amount']) > 0: #When Status != Active or Pending Amount > 0
        print(Fore.WHITE + Style.BRIGHT + '\nStatus: ' + Fore.RED + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Pending Amount: ' + Fore.RED + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)
        print("\n:-------Details-------:\n")
        for keys,values in response_dict.items():
            print(Fore.WHITE + Style.BRIGHT + keys + Style.RESET_ALL + ": " + values) 
    else:
        print(Fore.WHITE + Style.BRIGHT + '\nStatus: ' + Fore.GREEN + Style.BRIGHT + response_dict['Status'] + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Pending Amount: ' + Fore.GREEN + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)
        print("\n:-------Details-------:\n")
        for keys,values in response_dict.items():
            print(Fore.WHITE + Style.BRIGHT + keys + Style.RESET_ALL + ": " + values) 