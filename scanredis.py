import redis
import json
REDIS_HOST = 'redis-14390.c256.us-east-1-2.ec2.cloud.redislabs.com'
redis_conn = redis.Redis(  host= 'redis-14390.c256.us-east-1-2.ec2.cloud.redislabs.com',
  port= '14390',
  password= 'EEDPLADvHhC12ziP5B2m2skqO7ZRv24i',charset="utf-8", decode_responses=True)

# print(redis_conn.keys())
userNameQuery = "C"
for key in redis_conn.keys():
    
    try:
        data = json.loads(redis_conn.get(key))
        print(data)
        if (data["userName"] == userNameQuery):
            print(data)
    except Exception as e:
        # print(e)
        pass