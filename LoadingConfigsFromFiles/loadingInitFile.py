import os
import configparser


"""
testing : load a ini config file
"""
# import xlrd  # module for working with SpreedSheets

__author__ = "naporium"
__EMAIL__ = "nm.10000.testes@gmail.com"

print("The script working directory is {}" .format(os.path.dirname(__file__)))
script_dir = os.path.dirname(__file__)

def _get_configDict():
    # instantiate
    config = configparser.ConfigParser()

    # parse existing file
    config.read('ServerSetting.INI')

    # read values from a section
    # server_name = config.get('DhcpServer', 'name')
    # print(server_name)

    sections_in_config_file = config.sections()
    print(f"sections_in_config_file: {sections_in_config_file}")

    # WE expect this values in config File for each server
    expect_sections_are = ("name", "cpu", "memory", "interface_adapter", "interface_type", "interface_name")

    config_data = {}

    for section in sections_in_config_file:
        print(f"For server: {section}")
        for key in config[section]:
            # TODO
            #  WE also may want to validate values
            if key not in expect_sections_are:
                raise RuntimeError(f"Expected {key} in {section}")
            print(f"{key}: {config[section][key]}")
            config_data[key] = [config[section][key]]
        print("-------------------")

    import json
    print(json.dumps(config_data, indent=4))
    return config_data

_get_configDict()



# read values from a section
#string_val = config.get('section_a', 'string_val')
# bool_val = config.getboolean('section_a', 'bool_val')
# int_val = config.getint('section_a', 'int_val')
#float_val = config.getfloat('section_a', 'pi_val')

# update existing value
# config.set('section_a', 'string_val', 'world')

# add a new section and some values
# config.add_section('section_b')
# config.set('section_b', 'meal_val', 'spam')
# config.set('section_b', 'not_found_val', '404')