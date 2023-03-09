from yaml import load
from yaml.loader import Loader
from railwire import perform_login

response_soup = perform_login()


def get_text(selector):
    text = from_soup(selector)
    removingxa0 = text.replace('\xa0', ' ')
    stripped_text = strip_text(removingxa0) # ' \xa0 02-02-21' ' \xa0 100'
    return stripped_text

def strip_text(text):
    stripped_text = text.strip()
    return stripped_text

def from_soup(selector):
    return response_soup.select(selector)[0].get_text()


data_dict = {}
# with open("railwire.yml", 'r', encoding="utf-8") as stream:
#     dictionary = load(stream, Loader=Loader)
#     keys = [x for x in dictionary["scraping_data"].keys()] 
#     for key in keys:
#         if dictionary["scraping_data"][key]["tag"]  != "none":
#             print(f'{get_text(dictionary["scraping_data"][key]["tag"]["selector"])}')

with open("railwire.yml", 'r', encoding="utf-8") as stream:
    dictionary = load(stream, Loader=Loader)
    keys = [x for x in dictionary["scraping_data"].keys()]
    for key in keys:
        if dictionary["scraping_data"][key]["tag"]  != "none":
            data = get_text(dictionary["scraping_data"][key]["tag"]["selector"])
            if ":" in data:
                dict_item = data.split(":")
                dict_key = strip_text(dict_item[0])
                dict_value = strip_text(dict_item[1])
                # print(f"{dict_key}: {dict_value}")
                data_dict[dict_key] = dict_value
            else:
                data_dict[key] = data




def get_railwire_dict():
    return data_dict


if __name__ == "__main__":
    for key, value in data_dict.items():
        print(f"{key}: {value}")