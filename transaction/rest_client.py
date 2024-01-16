from __future__ import print_function

import logging

import random
import read_loadfile

import datetime
import constants
import plot
import requests
import json



def run(count, keys_to_iterate):
    print("starting transaction with client ...")
    for key in range(count):     
        url = 'http://localhost:5000/merchantdetails/getmerchantname/'+random.choice(keys_to_iterate)
        response = requests.get(url)

if __name__ == "__main__":
    logging.basicConfig()
    read_loadfile.load_merchants(constants.filename)
    for key in constants.volume:
        starttimestamp = datetime.datetime.now().timestamp()
        run(key, list(read_loadfile.merchants_dict.keys()))
        endtimestamp = datetime.datetime.now().timestamp()  
        print("Running for " +str(key)+ " entries: " + str(endtimestamp-starttimestamp))
        constants.performance_dict[key]=endtimestamp-starttimestamp
    plot.plot_graph(constants.performance_dict, 'RESTful API')
    