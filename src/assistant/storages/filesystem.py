import os

from assistant.storages.istorage import IStorage

class FilesystemStorage(IStorage):
    alias = 'filesystem'
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _get_file_path(self, key):
        return os.path.join(self.directory, key)

    def set(self, key, value):
        with open(self._get_file_path(key), 'w') as f:
            f.write(value)


