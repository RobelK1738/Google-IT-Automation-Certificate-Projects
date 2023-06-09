#!/usr/bin/env python3

import os
import requests

files = "/data/feedback/"
mylink = "http://34.136.55.30/feedback/"
myFiles = os.listdir(files)

for file in myFiles:
    
        with open(files+file) as infile:
                f = {}
                f["title"] = infile.readline().removesuffix("\n")
                f["name"] = infile.readline().removesuffix("\n")
                f["date"] = infile.readline().removesuffix("\n")
                f["feedback"] = infile.readline().removesuffix("\n")
                response = requests.post(mylink, json=f)
                print(response.status_code)