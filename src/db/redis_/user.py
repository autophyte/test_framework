from src.db.redis_ import client_session as _client_session
from src.utils import config


def token(uid: str) -> str:
    """
    从redis中获取用户登陆信息
    :param uid: 用户id
    :return:
    """
    return _client_session.get(
        config.get("redis.key.prefix.token") + str(uid).strip())
