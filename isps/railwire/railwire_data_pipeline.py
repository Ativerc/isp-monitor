from yaml import load
from yaml.loader import Loader
from railwire import perform_login

response_soup = perform_login()


def remove_xa0(text):
    """
    This function takes in a CSS selector and gets the text from 
    the soup via get_text_from_selector(). But every data tag/value pair
    has a \xa0 character.
    
    This function removes any \xa0 character and returns the santitised string.

    Args:
        selector (string): _description_

    Returns:
        string: The text from a given selector without the xa0 character.
    """
    sanitised_from_xa0 = text.replace('\xa0', '')
    stripped_text = strip_spaces(sanitised_from_xa0) # ' \xa0 02-02-21' ' \xa0 100'
    return stripped_text

def strip_spaces(text):
    """_summary_

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    stripped_text = text.strip()
    return stripped_text

def get_text_from_soup(selector):
    """_summary_

    Args:
        selector (_type_): _description_

    Returns:
        _type_: _description_
    """
    return response_soup.select(selector)[0].get_text()


data_dict = {}

with open("railwire.yml", 'r', encoding="utf-8") as stream:
    dictionary = load(stream, Loader=Loader)
    keys = [x for x in dictionary["scraped_data"].keys()]
    for key in keys:
        if dictionary["scraped_data"][key]["tag"] != "none":
            unsanitised_data = get_text_from_soup(dictionary["scraped_data"][key]["tag"]["selector"])
            data = remove_xa0(unsanitised_data)
            if ":" in data:
                key_value_pair = data.split(":")
                dict_key = strip_spaces(key_value_pair[0])
                dict_value = strip_spaces(key_value_pair[1])
                data_dict[dict_key] = dict_value
            else:
                data_dict[key] = data




def get_railwire_dict():
    return data_dict


def privacy_warning():
    pass
    # Warn users about their PII being displayed
    # with a list of PII that will be shown.
    # if user accepts then print



def find_data_usage_unit(dicti):
    unit_tag_value = dicti['Data_Used_Unit']
    dicti['Data_Used_Unit'] = unit_tag_value.split("/")[0][-3:-1]
    return dicti

FINAL_DICT = find_data_usage_unit(data_dict)

if __name__ == "__main__":
    for key, value in FINAL_DICT.items():
        print(f"{key}: {value}")