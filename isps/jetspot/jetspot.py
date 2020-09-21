import requests, os, getpass, sys
from bs4 import BeautifulSoup as bs


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
# too many confirmations. Need to rewrite the whole input mechanism.

def instant_creds_fetcher(): # Should change its name probably? :TODO:
    username = input("Enter your Username/UserID: ")
    password = passwordFetcher()
    instant_fetched_creds = {'username': username, 'password': password}
    return instant_fetched_creds 



# PARSING PART

def page_parser(response): 
    """
    parses the html response
    passes data (list of td bs4.element.tag) to formatter function for formatting
    """
    soup = bs(response.content, features="html.parser")
    table_datas = soup.select('td')
    return formatter(table_datas)


def tag_to_string(tag_item):
    """
    converts bs4.element.tag datatype to string datatype
    """
    string = tag_item.get_text()
    return string

usual_key_values = ["Status", "Name", "Plan Name", 
    "Plan Renewal Date", "Plan Expired On", "Pending Amount",
    "Current Complaint Status", "Service Provider Details"]

def key_checker(td_string_list):
    """
    Checks if the values from the td_string_list to be used as keys 
    in the table_data_dict have been changed and if changed, 
    raise an Error!
    """
    # key_position_match_dict usual_key_value position : td_string_list position
    # key_position_match_dict = {0: 0, 1:2, 2:4, 3:6, 4:8, 5:10, 6:12, 7:14}
    failed_keys = []
    for i in range(len(usual_key_values)):
        if usual_key_values[i] not in td_string_list:
            failed_keys.append(i)
            # Raise here or later?
    if len(failed_keys) != 0:
        print("KeyNotFoundError by key_checker(). Keys not found are:", end="") # :TODO: Raise Error!
        for i in range(len(failed_keys)):
            print(f"\"{usual_key_values[i]}\" ", end="")
        print("Exiting!")
        sys.exit()
    return td_string_list

    
def value_data_extractor(td_data_list):
    string_data_list = []
    for i in range(len(usual_key_values)):
        if usual_key_values[i] in td_data_list:
            string_data_list.append(td_data_list[td_data_list.index(usual_key_values[i]) + 1])
        else:
            print("Key not found! by list_data_extractor! Exiting!") # :TODO: Raise Error!
            sys.exit()
    stripped_string_data_list = list(map(str.strip, string_data_list))
    return stripped_string_data_list


def data_dict_maker(key_list, value_list):
    data_dict = {}
    key_list_len = len(key_list)
    value_list_len = len(value_list)
    if key_list_len != value_list_len:
        print("KeyValueListLengthMismatchError: by data_dict_maker") # :TODO: Raise Error!
        print(f"Key List Length {key_list_len} != Value List Length {value_list_len}") 
        print("Exiting!")
        sys.exit()
    else:
        for i in range(key_list_len):
            data_dict[key_list[i]] = value_list[i]
    return data_dict


def formatter(td_tags_list):
    """
    Main function for formatting. 
    Individual jobs are done by other functions: key_checker(), value_data_extractor(), data_dict_maker()
    """
    td_string_list = list(map(tag_to_string, td_tags_list))
    key_present_list = key_checker(td_string_list) # Check if key is not present
    value_data_list = value_data_extractor(key_present_list)
    data_dict = data_dict_maker(usual_key_values, value_data_list)
    return data_dict

# REQUEST/RESPONSE PART

def responser(username, password):
    # Start Session with ISP's Login Page
    session = requests.session()
    login_url = 'https://login.jetspot.in/synnefoclient/'
    #initial_response = s.get(login_url, verify=False)
    cookiejar = session.cookies
    data = {
        'LoginForm[username]': username,
        'LoginForm[password]': password,
        'yt0': 'Log In'
        }
    print("Fetching Data!")
    response = session.post(login_url, cookies=cookiejar, data=data, verify=False)  #ssl_certificate verification fails for some reason; hence set verify=False
    response_dict = (page_parser(response)) # Calls Page Parser here to parse the page
    return response_dict


def jetspot_main(verbosity=False, interactive=False):
    if interactive == False:
        username = os.environ['USERNAME'] 
        password = os.environ['PASSWORD']
    else:
        fetched_creds = instant_creds_fetcher()
        username = fetched_creds['username']
        password = fetched_creds['password']
    data = responser(username, password)
    # for key, value in data.items(): # delete post testing :TODO:
    #     print(f"{key}: {value}")    # delete post testing :TODO:
    if args.verbose == True:
        print_verbose(responser())
    else:
        print_this(responser())