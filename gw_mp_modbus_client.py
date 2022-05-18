"""Modbus TCP Client"""

__author__ = "Farhani Mouhamed Aziz, Aymen Majoul"
__license__ = "MIT"
__email__ = "farhaniaziz285@gmail.com, aimen.majoul@gmail.com"

# Modbus library
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

import grpc

# MQTT gRPC library
import mqtt_service_pb2_grpc
import mqtt_service_pb2

# Configuration Manager gRPC library
import config_manager_pb2 as pb2
import config_manager_pb2_grpc as pb2_grpc

# Tools
from utils import log_info

# Default modbus server
MODBUS_SERVER_HOST = "localhost"
MODBUS_SERVER_PORT = 5020

# Connect to Config Manager
with grpc.insecure_channel('127.0.0.1:50050') as config_channel:
    CONFIG_STUB = pb2_grpc.ConfigurationServiceStub(config_channel)
    MODBUS_SERVER_HOST = CONFIG_STUB.GetConfig(pb2.Configuration(bloc="modbustcp", config="server")).value
    MODBUS_SERVER_PORT = CONFIG_STUB.GetConfig(pb2.Configuration(bloc="modbustcp", config="port")).value
    log_info("[ModbusClient] Connecting to modbus server: {}:{}".format(MODBUS_SERVER_HOST, MODBUS_SERVER_PORT))

MODBUS_CLIENT = ModbusClient(MODBUS_SERVER_HOST, port=MODBUS_SERVER_PORT)
MODBUS_CLIENT.connect()

UNIT = 0x1

def run():
    """Main modbus client method"""
    with grpc.insecure_channel('0.0.0.0:50051') as mqtt_channel:
        mqtt_stub = mqtt_service_pb2_grpc.mqttStub(mqtt_channel)
        modbus_data = MODBUS_CLIENT.read_holding_registers(0, 1, unit=UNIT)
        for mdata in modbus_data.registers:
            mqtt_stub.publish(mqtt_service_pb2.mqtt_msg(data=str(mdata), topic="modbustcp"))

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        log_info("[ModbusClient] Shutting down ..")