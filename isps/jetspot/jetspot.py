import requests, os, getpass
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


def formatter(table_data):
    """
    maps each list item to tag_to_string function
    converts the returned data to list
    """
    data_list = list(map(tag_to_string, table_data)) 
    print(data_list) #test
    for i in data_list:
        print(i)
    counter = 0
    while "" in data_list and counter<6: #removes empty "" from data_list 
        data_list.remove("")
        counter +=1
    print("Data List 2") #test
    print(data_list)
    non_empty_data_list = list(map(str.strip, data_list))
    print("nedl 1") #test
    for i in non_empty_data_list: 
        print(i)
    # non_empty_data_list.append("") 
    print("nedl 2") #test
    for i in non_empty_data_list:
        print(i)
    data_dict = {}
    for i in range(0, len(non_empty_data_list)-2, 2):
        data_dict[non_empty_data_list[i]] = non_empty_data_list[i+1]
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
    for key, value in data.items(): # delete post testing :TODO:
        print(f"{key}: {value}")    # delete post testing :TODO:
    return data