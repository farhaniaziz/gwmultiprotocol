import grpc
from lib import config_manager_pb2
from lib import config_manager_pb2_grpc
from concurrent import futures


def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = config_manager_pb2_grpc.ConfigurationServiceStub(channel)
        stub.SetConfig(config_manager_pb2.ConfigurationSet(bloc="mqtt", config="broker", value="blabla"))
        response = stub.GetConfig(config_manager_pb2.Configuration(bloc="mqtt", config="broker"))
        print("Value = %s" %response.value)
        
run()