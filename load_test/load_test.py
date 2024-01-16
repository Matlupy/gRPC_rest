import time
from locust import User, task, between
# noinspection PyPackageRequirements
import grpc
import random 
import constants
import read_loadfile

from transaction_pb2_grpc import MerchantDetailsStub
from transaction_pb2 import MerchantId

class GrpcUser(User):
    abstract = True

    def __init__(self, *args, **kwargs):
        super(GrpcUser, self).__init__(*args, **kwargs)
        target = self.host.lstrip('http://')        
        channel = grpc.insecure_channel(target)
        self.stub = MerchantDetailsStub(channel=channel)


class ApiUser(GrpcUser):
    wait_time = between(0.9, 1.1)

    @task
    def get_prediction(self):
        input_data = MerchantId(id=random.choice(list(read_loadfile.merchants_dict.keys())))     
        start_time = time.time()
        try:
            self.stub.GetMerchantName(input_data)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            print(e)
            self.environment.events.request_failure.fire(request_type="grpc",
                                                         name=self.host,
                                                         response_time=total_time,
                                                         exception=e,
                                                         response_length=0)
        else:
            total_time = int((time.time() - start_time) * 1000)
            self.environment.events.request.fire(request_type="grpc",
                                                         name=self.host,
                                                         response_time=total_time,
                                                         response_length=0)
    
    read_loadfile.load_merchants(constants.filename)