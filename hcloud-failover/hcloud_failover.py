#!/usr/bin/env python3
# (c) 2018 Maximilian Siegl 
# Edited 2019 by chris2k20

import sys
import json
import os
import requests
from multiprocessing import Process

CONFIG_PATH = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "config.json")



def change_request(endstate, url, header, payload):
    if endstate == "MASTER":
        print("Post request to: " + url)
        print("Header: " + str(header))
        print("Data: " + str(payload))
        r = requests.post(url, data=payload, headers=header)
        print("Response:")
        print(r.status_code, r.reason)
        print(r.text)
    else:
        print("Error: Endstate not defined!")


def main(arg_type, arg_name, arg_endstate):
    with open(CONFIG_PATH, "r") as config_file:
        config = json.load(config_file)

    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + config["api-token"]
    }

    payload = '''{"server": ''' + str(config["server-id"]) + "}"

    print("Perform action for transition to " + arg_endstate + " state")

    for ips in config["ips"]:
        url = config["url"].format(ips["floating-ip-id"])
        Process(target=change_request, args=(arg_endstate, url, header, payload)).start()


if __name__ == "__main__":
    main(arg_type=sys.argv[1], arg_name=sys.argv[2], arg_endstate=sys.argv[3])
