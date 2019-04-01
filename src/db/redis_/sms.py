from src.db.redis_ import client_main as _client
from src.utils import config
import datetime


_prefix = config("redis.key.prefix.sms")


def _prefix_count(type_: int) -> str:
    _today = datetime.datetime.now().strftime("%Y%m%d")
    return _prefix + "send:count:" + str(type_) + ":" + _today


def _prefix_text(phone: str, type_: int) -> str:
    return _prefix + "text:" + str(type_) + ":" + phone


def clear(phone: str, type_: int = None):
    # clear text
    if type_ is None:
        names = [_prefix_text(phone, n) for n in [1, 2, 3, 4]]
        _client.delete(*names)
    elif type_ in [1, 2, 3, 4]:
        name = _prefix_text(phone, type_)
        _client.delete(name)

    # clear counts
    if type_ is None:
        for n in (1, 2, 3, 4):
            name = _prefix_count(n)
            _client.hdel(name, phone)
    elif type_ in (1, 2, 3, 4):
        name = _prefix_count(type_)
        _client.hdel(name, phone)


def clears(phones: list):
    for phone in phones:
        clear(phone)


def set_value(phone, value: int, type_: int):
    name = _prefix_count(type_)
    value = _client.hset(name, phone, value)
    return value


def count(phone: str, _type: int):
    name = _prefix_count(_type)
    value = _client.hget(name, phone)
    return value


def text(phone: str, _type: int):
    name = _prefix_text(phone, _type)
    value = _client.get(name)
    return value


if __name__ == "__main__":
    _phone = "15700000005"
    print(text(_phone, 1))
