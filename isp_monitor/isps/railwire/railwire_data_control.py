from isp_monitor.isps.railwire.railwire_data_pipeline import main as pipeline_main

from yaml import load
from yaml.loader import Loader

with open("isp_monitor/isps/railwire/railwire.yml", 'r', encoding="utf-8") as stream:
    yml_dict = load(stream, Loader=Loader)




def core_data(yml_keys, data_dict, yml_to_data_dict):
    core_data_dict = {}
    for key in yml_keys:
        if yml_dict["scraped_data"][key]["property"]["core-data"] == True:
            core_data_dict[key] = data_dict[yml_to_data_dict[key]]
    return core_data_dict

def private_data(yml_keys, data_dict, yml_to_data_dict):
    private_data_dict = {}
    for key in yml_keys:
        if yml_dict["scraped_data"][key]["property"]["private"] == True:
            private_data_dict[key] = data_dict[yml_to_data_dict[key]]
    return private_data_dict


def return_dict(dict_type, dictionary=None):
    """_summary_

    Args:
        oftype (string): "core" / "private" / "all"

    Returns:
        _type_: _description_
    """

    if dictionary is None:
        data_dict = pipeline_main()
    else:
        data_dict = dictionary

    data_dict_keys = list(data_dict.keys())
    yml_keys = list(yml_dict["scraped_data"].keys())

    yml_to_data_dict = {}

    keycount = 0
    for key in yml_keys:
        yml_to_data_dict[key] = data_dict_keys[keycount]
        keycount += 1

    if dict_type == "core":
        return core_data(yml_keys, data_dict, yml_to_data_dict)
    elif dict_type == "private":
        return private_data(yml_keys, data_dict, yml_to_data_dict)
    elif dict_type == "all":
        all_data_dict = {}
        all_data_dict.update(core_data(yml_keys, data_dict, yml_to_data_dict))
        all_data_dict.update(private_data(yml_keys, data_dict, yml_to_data_dict))
        return all_data_dict



def dict_print(diction):
    for key, value in diction.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    print("Printing 'core' dict....\n\n")
    print(return_dict("core"))