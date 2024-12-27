from assistant.storages.redis import RedisStorage

temp_storage = RedisStorage(db=0)
consistent_storage = RedisStorage(db=1)