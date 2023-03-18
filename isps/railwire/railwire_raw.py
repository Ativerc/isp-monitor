import os

from railwire import perform_login
from railwire_data_pipeline import main as start_pipeline
from railwire_datacontrol import return_dict



def raw_input(username, password, url, dict_type):
    response_soup = perform_login(username, password, url)
    data_dict = start_pipeline(response_soup)
    print(return_dict(dict_type, data_dict))

if __name__ == "__main__":
    raw_input(os.environ['rw_username'], os.environ['rw_password'], os.environ['rw_url'], "core")
    