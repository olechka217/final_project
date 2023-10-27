import configuration
import requests
import data

def post_new_order_kit( body ):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH, json=body, headers=data.headers) 

def get_order(t):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params={"t": t})

