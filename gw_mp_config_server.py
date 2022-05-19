"""
    Gateway Multiprotocol Configuration Manager gRPC Server
"""

__author__ = "Farhani Mouhamed Aziz, Aymen Majoul"
__license__ = "MIT"
__email__ = "farhaniaziz285@gmail.com, aimen.majoul@gmail.com"

from concurrent import futures
import json
import grpc
import time

import config_manager_pb2_grpc as pb2_grpc
import config_manager_pb2 as pb2

# Import tools
from utils import log_info, log_error

# Configuration file
GW_MP_CONFIGURATION = json.load(open('/etc/gwmp/config.json'))

def get_config(base, config):
    """Base configuration key load method"""
    try:
        return GW_MP_CONFIGURATION[base][config]
    except KeyError:
        log_error("[Tools] Cannot load key ({})".format(config))
    return None

def set_config(bloc, config, value):
    """Write config in a JSON file"""
    try:
        with open(GW_MP_CONFIGURATION, 'r+') as gw_mp_config_file:
            data = json.load(gw_mp_config_file)
            data[bloc][config] = value
            gw_mp_config_file.seek(0)
            json.dump(data, gw_mp_config_file, indent=4)
            gw_mp_config_file.truncate()
    except FileNotFoundError:
        print("[Tools] Config file not found")

class ConfigurationService(pb2_grpc.ConfigurationServiceServicer):
    """Configuration Server gRPC class Implementation"""

    def GetConfig(self, request, context):
        log_info("[ConfigManager] Request to get config[{}][{}]".format(\
            request.bloc, request.config))
        val = get_config(request.bloc, request.config)
        log_info("[CongiManager] Returning value : {}".format(val))
        return pb2.ConfigurationValue(value=str(val))

    def SetConfig(self, request, context):
        log_info("[ConfigManager] Setting config[{}][{}] to ({})".format(\
            request.bloc, request.config, request.value))
        set_config(request.bloc, request.config, request.value)
        return pb2.EMPTY()


def main_config_manager():
    """Configuration Manager Main Method"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ConfigurationServiceServicer_to_server(ConfigurationService(), server)
    print('Started')
    server.add_insecure_port('[::]:50050')
    server.start()
    while 1:
        time.sleep(10)
    #mqtt_server.wait_for_termination()

if __name__ == '__main__':
    try:
        log_info("[ConfigManager] Starting server ...")
        main_config_manager()
    except KeyboardInterrupt:
        log_info("[ConfigManager] Shutting down ...")