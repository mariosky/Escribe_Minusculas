
import redis
import os
import time

r = redis.StrictRedis( host=os.environ['REDIS_HOST'], port=6379, db=0)

redis_ready = False

#intenta hasta que este listo el contenedor
while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print("waiting for redis")
        time.sleep(3)

print("setup: redis alive")


while True:
 
    _,color=r.brpop('cola_de_mensajes')
    if color:
        color=color.upper() 
        r.lpush('cola_mayusculas',color)
        print('convirtiendo a mayusculas ' + str(color))
        time.sleep(3)
      
    