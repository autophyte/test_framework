import os
import hashlib as _hashlib
import threading as _threading


_SIGN_SALT = "12345678900987654321123456789009"


def root_path() -> str:
    """
    当前工程根目录。
    :return:
    """
    return os.path.dirname(
        os.path.dirname(os.path.dirname(
            __file__)))


def path(file_name: str) -> str:
    """
    根据指定文件名，获取在当前项目下的绝对路径。
    :param file_name:
    :return:
    """
    return os.path.abspath(os.path.join(root_path(), file_name))


def concurrent_do(fun, tc: int = 5, loop: int = 4):
    def _loop_run():
        for _ in range(loop):
            fun()

    handle_list = list()
    for n in range(tc):
        handle = _threading.Thread(target=_loop_run)
        handle.start()
        handle_list.append(handle)

    for handle in handle_list:
        handle.join()


def md5(source: str, encoding: str = "utf-8") -> str:
    return _hashlib.md5(source.encode(encoding)).hexdigest()


def sign(source: str) -> str:
    """
    获取魔方sign值
    :param source:
    :return:
    """
    _value = _SIGN_SALT + source + _SIGN_SALT
    return _hashlib.md5(_value.encode("utf-8")).hexdigest()


def url(host: str, api: str) -> str:
    """
    根据host和api，拼接url地址
    :param host: api请求host
    :param api: api名
    :return:
    """
    if host.endswith("/") and api.startswith("/"):
        host_ = host[:-1]
    elif not host.endswith("/") and not api.startswith("/"):
        host_ = host + "/"
    else:
        host_ = host

    return host_ + api


def synchronized(func):
    func.__lock__ = _threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return lock_func


def singleton(cls):
    """
    定义singleton装饰器，用于装饰类，构成单例类
    :param cls: 需要被装饰的类
    :return:
    """
    instances = {}

    @synchronized
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


def run_once(obj):
    """
    装饰器，同样的参数只能使函数执行一次或类实例化一次
    :param obj: 需要被装饰的类或函数
    """
    instances = {}

    def wrapper(*args, **kwargs):
        key = str(obj) + str(args) + str(kwargs)
        key = _hashlib.md5(key.encode("utf-8")).hexdigest()
        if key not in instances:
            instances[key] = obj(*args, **kwargs)
        return instances[key]

    return wrapper


if __name__ == "__main__":
    print(path("123"))
