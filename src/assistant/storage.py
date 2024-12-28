
from assistant.storages.redis import RedisStorage
from assistant.settings.default_settings import settings

temp_storage = getattr(settings, 'temp_storage', RedisStorage(db=0))
consistent_storage = getattr(settings, 'consistent_storage', RedisStorage(db=1))