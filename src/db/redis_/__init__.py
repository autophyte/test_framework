import redis
import socket
from src.utils import config


try:
    socket_keepalive_options = {
        socket.TCP_KEEPIDLE: 10,
        socket.TCP_KEEPCNT: 20,
        socket.TCP_KEEPINTVL: 2
    }
except AttributeError:
    socket_keepalive_options = None


client_session = redis.StrictRedis(host=config.get("redis.session.host"),
                                   port=config.get("redis.session.port"),
                                   password=config.get("redis.session.auth"),
                                   decode_responses=True,
                                   socket_connect_timeout=15,
                                   socket_keepalive=True,
                                   socket_keepalive_options=socket_keepalive_options)


client_main = redis.StrictRedis(host=config.get("redis.main.host"),
                                port=config.get("redis.main.port"),
                                password=config.get("redis.main.auth"),
                                decode_responses=True,
                                socket_connect_timeout=15,
                                socket_keepalive=True,
                                socket_keepalive_options=socket_keepalive_options)
