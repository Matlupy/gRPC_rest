# grpc_vs_rest
A project to test and compare the performance of RESTful against gRPC communication protocols in a controlled environment simulating a payments transfer system of a bank.

## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Authors

- [@Matlupy](https://www.github.com/Matlupy)


Run the requirements.txt file

# DEPLOYMENT

## Testing the gRPC service: 

Run the proto file command:
python -m grpc_tools.protoc -I../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/transaction.proto

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

Navigate to the url generated in the termnal http://localhost:8089
