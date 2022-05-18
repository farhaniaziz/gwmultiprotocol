"""
    Gateway Multiprotocol MQTT gRPC Server
"""

__author__ = "Farhani Mouhamed Aziz, Aymen Majoul"
__license__ = "MIT"
__email__ = "farhaniaziz285@gmail.com, aimen.majoul@gmail.com"

from concurrent import futures

# MQTT library
import paho.mqtt.client as mqtt

# MQTT gRPC library
import grpc
import mqtt_service_pb2
import mqtt_service_pb2_grpc

# Config Manager gRPC library
import config_manager_pb2 as cm_pb2
import config_manager_pb2_grpc as cm_pb2_grpc

# Tools
from utils import log_info

# Default MQTT configuration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883

# Connect to Config Manager
with grpc.insecure_channel('127.0.0.1:50050') as channel:
    CONFIG_STUB = cm_pb2_grpc.ConfigurationServiceStub(channel)
    MQTT_BROKER = CONFIG_STUB.GetConfig(cm_pb2.Configuration(bloc="mqtt", config="broker")).value
    MQTT_PORT = CONFIG_STUB.GetConfig(cm_pb2.Configuration(bloc="mqtt", config="port")).value
    log_info("[MQTTServer] Got broker configuration: {}:{}".format(MQTT_BROKER, MQTT_PORT))

# Connect to MQTT broker
MQTT_CLIENT = mqtt.Client()

class MQTTService(mqtt_service_pb2_grpc.mqttServicer):
    """MQTT Server gRPC class Implementation"""

    def publish(self, request, context):
        log_info("[MQTTServer] Data to publish: {} , to topic: {}".format(\
            request.data, request.topic))
        if MQTT_CLIENT:
            MQTT_CLIENT.connect(MQTT_BROKER, int(MQTT_PORT))
            MQTT_CLIENT.publish(topic=request.topic, payload=request.data)
            MQTT_CLIENT.disconnect()
        return mqtt_service_pb2.Empty()

def main_mqtt_server():
    """MQTT Manager Main Method"""
    mqtt_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mqtt_service_pb2_grpc.add_mqttServicer_to_server(MQTTService(), mqtt_server)
    log_info("[MQTTServer] Server started!")
    mqtt_server.add_insecure_port('[::]:50051')
    mqtt_server.start()
    mqtt_server.wait_for_termination()

if __name__ == '__main__':
    try:
        main_mqtt_server()
    except KeyboardInterrupt:
        log_info("[MQTTServer] Shutting down ...")