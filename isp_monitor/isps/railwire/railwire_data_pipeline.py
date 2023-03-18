from yaml import load
from yaml.loader import Loader
from railwire import perform_login


def remove_xa0(text):
    """
    Removes any \xa0 character from a given string and returns the santitised string.

    Args:
        text (string): Unsanitised string

    Returns:
        string: The text from a given selector without the xa0 character.
    """
    sanitised_from_xa0 = text.replace('\xa0', '')
    stripped_text = strip_spaces(sanitised_from_xa0) # ' \xa0 02-02-21' ' \xa0 100'
    return stripped_text

def strip_spaces(text):
    """Strips spaces from before and after a given string

    Args:
        text (string): A text which has some spaces before and after it 

    Returns:
        (string): A text sanitised off preceding and tailing spaces. 
    """
    stripped_text = text.strip()
    return stripped_text

def get_text_from_soup(soup, selector):
    """_summary_

    Args:
        selector (_type_): _description_

    Returns:
        _type_: _description_
    """
    return soup.select(selector)[0].get_text()


data_dict = {}

with open("railwire.yml", 'r', encoding="utf-8") as stream:
    dictionary = load(stream, Loader=Loader) 



def find_data_usage_unit(dicti):
    unit_tag_value = dicti['Data_Used_Unit']
    dicti['Data_Used_Unit'] = unit_tag_value.split("/")[0][-3:-1]
    return dicti

def main(soup=perform_login()):
    keys = [x for x in dictionary["scraped_data"].keys()]
    target_soup = soup
    for key in keys:
        if dictionary["scraped_data"][key]["tag"] != "none":
            unsanitised_data = get_text_from_soup(target_soup, dictionary["scraped_data"][key]["tag"]["selector"])
            data = remove_xa0(unsanitised_data)
            if ":" in data:
                key_value_pair = data.split(":")
                dict_key = strip_spaces(key_value_pair[0])
                dict_value = strip_spaces(key_value_pair[1])
                data_dict[dict_key] = dict_value
            else:
                data_dict[key] = data
    DATA_DICT = find_data_usage_unit(data_dict)
    return DATA_DICT







if __name__ == "__main__":
    for keys,values in main().items():
        print(f"{keys}: {values}")