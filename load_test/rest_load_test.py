# import json
# from locust import task, between
# from locust.contrib.fasthttp import FastHttpUser

# class ApiUser(FastHttpUser):
#     wait_time = between(0.9, 1.1)

#     @task
#     def get_predictions(self):
#         self.client.get(url="/merchantdetails/getfullmerchant/%27C2054744914%27")


import json
from locust import task, between
from locust.contrib.fasthttp import FastHttpUser
import read_loadfile
import constants
import random

class ApiUser(FastHttpUser):
    wait_time = between(0.9, 1.1)

    @task
    def get_merchantdetails(self):
        self.client.get(url="/merchantdetails/getfullmerchant/" +random.choice(list(read_loadfile.merchants_dict.keys())))

    read_loadfile.load_merchants(constants.filename)
