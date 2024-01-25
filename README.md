# grpc_vs_rest
A project to test and compare the performance of RESTful against gRPC communication protocols in a controlled environment simulating a payments transfer system of a bank.

## Authors

- [@Matlupy](https://www.github.com/Matlupy)

## Installation and Setup:

## Clone the Repository:
Open the command Terminal and change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL from the code option in the repository.
```
git clone https://github.com/Matlupy/grpc_vs_rest.git
```
Install and if necessary upgrade the version of your pip using the below command:
```
$ python -m pip install --upgrade pip
```

## Install gRPC:
```
$ python -m pip install grpcio
```
Or, to install it system wide:
```
$ sudo python -m pip install grpcio
```
## gRPC tools
To install gRPC tools, run:
```
$ python -m pip install grpcio-tools
```

## Install REST API:
Let's begin byinstalling Flask in a virtual environment. If you don't have virtualenv installed in your system, you can download it from https://pypi.python.org/pypi/virtualenv and install.
```
$ pip install virtualenv
```
Next is to install flask in the virtual environmen:
```
$ virtualenv flask
$ flask/bin/pip install flask
```
# Deployment:

## Testing the gRPC service: 

Run the proto file command in the terminal from the path containing the proto file:
```
python -m grpc_tools.protoc -I../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/transaction.proto
```
#### To Run the gRPC server
Run the transaction_server.py file using the command

``` 
python3 -m transaction_server run
```

## Testing the RESTful API service: 

#### To Run the rest server
Run the rest_server.py file in git bash or cmd 

```
python3 -m rest_server run
```

# Run the locust performance Tests:

## Performance Testing gRPC Service:
Navigate to the load_test.py file and execute the command:
```		
python -m locust -f load_test.py --host=http://localhost:50051
``` 
## Performance Testing RESTful API:
Navigate to the rest_load_test.py file and execute the command:
```
python -m locust -f rest_load_test.py --host=http://localhost:5000
```

Navigate to the url generated in the termnal to view the performance test results:  
http://localhost:8089
