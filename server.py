# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:30:23 2020

@author: mdamelio
"""

from BroadcasterWebsocketServer import BroadcasterWebsocketServer
import json
from time import sleep
import random

server = BroadcasterWebsocketServer('', '8888', True)
server.start()

try:
    while True:
        data = {"symbol": random.choice(["AL30","AL29","GD30","GD35"]),
                "settlType": random.choice([1,2,3]),
                "currency": "ARS",
                "price": round(random.normalvariate(6500,500),2),
                "size": random.randint(1,100)
        }
        print(f"Sending message -> Symbol: {data['symbol']} - SettlType: {data['settlType']} - Currency: {data['currency']} - Price {data['price']} - Size: {data['size']}")
        server.broadcast(json.dumps(data))
        sleep(2)
except KeyboardInterrupt:
    server.stop()