import os
import redis
import json

from multiprocessing import Process
from formatPrintout import testPrint, formatDocument



redis_conn = redis.Redis(  host= 'redis-14390.c256.us-east-1-2.ec2.cloud.redislabs.com',
  port= '14390',
  password= 'EEDPLADvHhC12ziP5B2m2skqO7ZRv24i',charset="utf-8", decode_responses=True)


def sub(name: str):
    print("subscribing")
    pubsub = redis_conn.pubsub()
    pubsub.subscribe("broadcast")
    for message in pubsub.listen():
        try:
            print(message)
            data = json.loads(message["data"])
            print(data)
            formatDocument(data)
            # print("%s : %s" % (name, data))
        except Exception as e:
            print(e)
       


if __name__ == "__main__":
   testPrint()
   Process(target=sub, args=("reader1",)).start()