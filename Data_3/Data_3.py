
from datetime import date
import random
import json
import time

# two UUID's (Ver 1) to support the idea of two IoT devices present with single 
id_1 = "73a3a020-d3eb-11e9-bb65-2a2ae2dbcce4"
id_2 = "73a3a64c-d3eb-11e9-bb65-2a2ae2dbcce4"

class device(object):
    
    def __init__(self, device_id, status, adcValue, time_stamp):
        self.device_id = device_id
        self.status = status
        self.adcValue = adcValue
        self.time_stamp = time_stamp
    
    def info(self):
        print("Device ID", self.device_id)
        print("Status", self.status)
        print("Sensor Reading", self.adcValue)
        print("Time Stamp", self.time_stamp)

def data_gen(int):
    int =  random.randint(1, 1023) 
    return int

def serialize(obj):
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__



def main():
    d_data_a = data_gen(int)
    deviceA = device(id_1,True, d_data_a, time.time())
    print(time.time())
    print()
    print(deviceA.info())
    print()
    time.sleep(1.5)
    k = serialize(deviceA)
    print(k)
    print()


if  __name__ == "__main__":
    
    print("Executing Device Simulator...")
    while(True):
        main()