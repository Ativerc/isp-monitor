from railwire_data_pipeline import FINAL_DICT

from yaml import load
from yaml.loader import Loader

with open("railwire.yml", 'r', encoding="utf-8") as stream:
    dictionary = load(stream, Loader=Loader)

data_dict = FINAL_DICT

data_dict_keys = list(data_dict.keys())
yaml_keys = list(dictionary["scraped_data"].keys())

keys_to_keys_dict = {}

keycount = 0
for y_key in yaml_keys:
    keys_to_keys_dict[y_key] = data_dict_keys[keycount]
    keycount += 1


core_data_dict = {}
private_data_dict = {}
for y_key in yaml_keys:
    if dictionary["scraped_data"][y_key]["property"]["core-data"] == True:
        core_data_dict[y_key] = data_dict[keys_to_keys_dict[y_key]]
    elif dictionary["scraped_data"][y_key]["property"]["private"] == True:
        private_data_dict[y_key] = data_dict[keys_to_keys_dict[y_key]]

def dict_print(diction):
    for key, value in diction.items():
        print(f"{key}: {value}")


# dict_print(private_data_dict)
dict_print(core_data_dict)