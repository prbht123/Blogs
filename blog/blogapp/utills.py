import redis
import json
from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
import time

#CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# connect to redis
r = redis.StrictRedis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)

class Red:
    def set(cache_key,data):
        data = json.dumps(data)
        data = r.set(cache_key,data,ex=60*60*24)
        return data

    def get(cache_key):
        cache_data = r.get(cache_key)
        if not cache_data:
            return None
        print(cache_data)
        cache_data = json.loads(cache_data.decode('utf-8'))
        return cache_data
    
    def delete(cache_key):
        pp = r.delete(cache_key)
        print(pp)
        #kk = redis.delete(*X)
        return pp
