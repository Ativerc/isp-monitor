from railwire_data_pipeline import main as pipeline_main

from yaml import load
from yaml.loader import Loader

with open("railwire.yml", 'r', encoding="utf-8") as stream:
    yml_dict = load(stream, Loader=Loader)

data_dict = pipeline_main()

data_dict_keys = list(data_dict.keys())
yml_keys = list(yml_dict["scraped_data"].keys())

yml_to_data_dict = {}

keycount = 0
for key in yml_keys:
    yml_to_data_dict[key] = data_dict_keys[keycount]
    keycount += 1


def core_data():
    core_data_dict = {}
    for key in yml_keys:
        if yml_dict["scraped_data"][key]["property"]["core-data"] == True:
            core_data_dict[key] = data_dict[yml_to_data_dict[key]]
    return core_data_dict

def private_data():
    private_data_dict = {}
    for key in yml_keys:
        if yml_dict["scraped_data"][key]["property"]["private"] == True:
            private_data_dict[key] = data_dict[yml_to_data_dict[key]]


def return_dict(oftype):
    """_summary_

    Args:
        oftype (string): "core-data" / "private" / "all"

    Returns:
        _type_: _description_
    """
    if oftype == "core-data":
        return core_data()
    elif oftype == "private":
        return private_data()
    elif oftype == "all":
        all_data_dict = {}
        all_data_dict.update(core_data())
        all_data_dict.update(private_data())
        return all_data_dict



def dict_print(diction):
    for key, value in diction.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    print("Printing core-data dict....\n\n")
    dict_print(core_data())