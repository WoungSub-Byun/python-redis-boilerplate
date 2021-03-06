from typing import Any
import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379


class RedisUtil:
    def __init__(self) -> None:
        self.redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def delete_set(self, key: str) -> Any:
        return self.redis_client.delete(key)

    def get_set(self, key: str) -> Any:
        return self.redis_client.get(key)

    def add_dataset(self, key: str, value: str) -> Any:
        return self.redis_client.set(key, value)

    def flush_db(self):
        return self.redis_client.flushdb()


def main():
    rd_client = RedisUtil()
    rd_client.add_dataset("test-key", "test-value")
    rd_data = rd_client.get_set("test-key")
    print("[test get data] - key: {}, value: {}".format("test-key", rd_data))
    rd_client.delete_set("test-key")
    rd_data = rd_client.get_set("test-key")
    print("[test get data 2] - key: {}, value: {}".format("test-key", rd_data))


main()
