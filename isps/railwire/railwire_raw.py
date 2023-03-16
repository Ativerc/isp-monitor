from railwire import perform_login
from railwire_data_pipeline import main as start_pipeline
from railwire_datacontrol import return_dict

def raw_input(username, password, url, dict_type):
    response_soup = perform_login(username, password, url)
    data_dict = start_pipeline()
    return return_dict(dict_type)