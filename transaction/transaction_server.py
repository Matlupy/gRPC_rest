from concurrent import futures
import logging

import grpc
import transaction_pb2
import transaction_pb2_grpc
import read_loadfile
import constants

class MerchantDet(transaction_pb2_grpc.MerchantDetailsServicer):

    def GetMerchantName(self, request, context):
        db_merchant=read_loadfile.get_merchant_details(request.id,read_loadfile.merchants_dict)
        #Here I will connect to the database, pass the request.id and get the response values which then I will
        return transaction_pb2.Merchant(id=request.id,name=db_merchant.name)

    def GetFullMerchant(self, request, context):
        db_merchant=read_loadfile.get_merchant_details(request.id,read_loadfile.merchants_dict)
        return transaction_pb2.FullMerchant(id=request.id,name=db_merchant.name)                    #add remaining 
    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))         #OPTIMISE THIS LINE FOR PERFORMANCE
    transaction_pb2_grpc.add_MerchantDetailsServicer_to_server(MerchantDet(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    read_loadfile.load_merchants(constants.filename)
    # print (read_loadfile.get_merchant_details("'C105845174'",read_loadfile.merchants_dict).name)
    serve()
