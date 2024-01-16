from concurrent import futures
import logging

import json
import csv

# 1. Create the Merchant class
class Merchant:
    def __init__(self, id, name, customer_id, transact_amount, check_fraud, age, gender, zipcode_ori, zipcode_dest, category):
        self.id = id
        self.name = name
        self.customer_id = customer_id
        self.transact_amount = transact_amount 
        self.check_fraud = check_fraud 
        self.age = age 
        self.gender = gender 
        self.zipcode_ori = zipcode_ori
        self.zipcode_dest = zipcode_dest
        self.category = category
   
merchants_dict={}


# 2. Read the file and create a dictionary of merchants
def load_merchants(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                merchants_dict[row[1]]=Merchant(id=row[1],name=row[5],customer_id=row[9], transact_amount=row[8], check_fraud=row[5], age=row[5], gender=row[5], zipcode_ori=row[4], zipcode_dest=row[6], category=row[7])
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
    print(f'Processed {line_count} lines.')

# 3. Method to return merchant details
def get_merchant_details(merchant_id, merchants_dict):
    return merchants_dict.get(merchant_id)
