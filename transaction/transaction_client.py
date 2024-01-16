from __future__ import print_function

import logging

import grpc
import transaction_pb2
import transaction_pb2_grpc
import read_loadfile
import random
import datetime
import constants
import plot

def run(count, keys_to_iterate):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("starting transaction with client ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = transaction_pb2_grpc.MerchantDetailsStub(channel)
        for key in range(count):
            response = stub.GetMerchantName(transaction_pb2.MerchantId(id=random.choice(keys_to_iterate)))
            #print("Merchant details received: " + response.name)

if __name__ == "__main__":
    logging.basicConfig()
    read_loadfile.load_merchants(constants.filename)
    for key in constants.volume:
        starttimestamp = datetime.datetime.now().timestamp()
        run(key, list(read_loadfile.merchants_dict.keys()))
        endtimestamp = datetime.datetime.now().timestamp()  
        print("Running for " +str(key)+ " entries: " + str(endtimestamp-starttimestamp))
        constants.performance_dict[key]=endtimestamp-starttimestamp
    plot.plot_graph(constants.performance_dict, 'gRPC')
    