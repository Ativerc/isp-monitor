from colorama import Fore, Back, Style


def print_this(response_dict):
    for keys,values in response_dict.items():
        print(keys + ": " + values)
    
    if int(response_dict['Pending Amount']) > 0:
        print("Pending Amount: " + Fore.RED + Style.BRIGHT + response_dict['Pending Amount'] + Style.RESET_ALL)