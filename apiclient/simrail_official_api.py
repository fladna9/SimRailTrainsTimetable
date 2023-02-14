import requests
from __main__ import app
from routes.error_handlers import error_catcher

BASE_SIMRAIL_API = "https://panel.simrail.eu:8084/"
BASE_SIMRAIL_DISPATCH_API = "https://panel.simrail.eu:8091/"
GET_SERVERS_LIST = "servers-open"
GET_STATIONS_LIST = "stations-open?serverCode="
GET_TRAINS_LIST = "trains-open?serverCode="


def get_servers_list():
    try:
        response = requests.get(BASE_SIMRAIL_API + GET_SERVERS_LIST)
        if response.status_code != 200 or response is None:
            raise Exception("No response from Simrail API")
    except:
        app.error_catcher()
    return response.json()


def get_stations_list(server_name=None):
    if server_name is None:
        error_catcher()
    try:
        response = requests.get(BASE_SIMRAIL_API + GET_STATIONS_LIST + server_name)
        if response.status_code != 200 or response is None:
            raise Exception("No response from Simrail API")
    except:
        error_catcher()
    return response.json()


def get_trains_list(server_name=None):
    if server_name is None:
        error_catcher()
    try:
        response = requests.get(BASE_SIMRAIL_API + GET_TRAINS_LIST + server_name)
        if response.status_code != 200 or response is None:
            raise Exception("No response from Simrail API")
    except:
        error_catcher()
    return response.json()
