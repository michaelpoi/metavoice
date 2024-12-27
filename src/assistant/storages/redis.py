from assistant.storages.istorage import IStorage
import redis

class RedisStorage(IStorage):

    alias = 'redis'

    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def set(self, key, value):
        self.client.set(key, value)

    def get(self, key):
        return self.client.get(key)

    def exists(self, key):
        return self.client.exists(key) > 0

    def delete(self, key):
        self.client.delete(key)