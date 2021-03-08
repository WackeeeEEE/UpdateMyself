import os
from os import path

import pycurl
import re

import json

dir_path = path.dirname(path.realpath(__file__))
current_version = open("version.txt", "r").readline()
print(f"Version {current_version}")


#check for updates
git_token = open("git-token", "r")










#program that does things, intent is to update this primarily

#create persistent files if !exist
if path.exists(path.join(dir_path, "persistent")):
    print("persistent directory exists")
    records_file_path = path.join(dir_path, "persistent", "records.json")
    if path.exists(records_file_path):
        print("records file exists")
        records = json.load(open(records_file_path, "r"))
        print(records["names"])
else:
    print("persistent directory does not exist, attempting to create...")
    try:
        os.makedir("persistent")
        records_file = os.open("records.json", "w+")
        json.dumps("{}", records_file)
        records_file.close()
        print("Successfully created persistent files")
    except Exception as e:
        print(f"Failed to create persistent files\n ERRORSTR: {e}")
    
if path.exists(path.join(dir_path, "data")):
    print("data directory exists")
    number_of_data_files = len(os.listdir(path.join(dir_path, "data")))
    print(f"{number_of_data_files} file(s) present in data folder")
else:
    print("data directory does not exist")

print("this is a print statement that exists only in version 1.1")