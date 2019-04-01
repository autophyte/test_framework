import pymysql
from DBUtils.PooledDB import PooledDB
from src.utils import config


class MySqlWallet:
    def __init__(self):
        self.pool_ = self.create_db_pool("wallet")

    @staticmethod
    def create_db_pool(db_config: str):
        return PooledDB(
            creator=pymysql,
            mincached=5,  # 5为连接池里的最少连接数
            host=config.get("db.{db_config}.address".format(db_config=db_config)),
            user=config.get("db.{db_config}.user".format(db_config=db_config)),
            passwd=config.get("db.{db_config}.password".format(db_config=db_config)),
            port=config.get("db.{db_config}.port".format(db_config=db_config)),
            db=config.get("db.{db_config}.db".format(db_config=db_config)),
            charset="utf8")

    @staticmethod
    def build_condition(source: dict) -> str:
        tmp_list = list()
        for key in source:
            if isinstance(source[key], str):
                tmp_list.append("`{key}`=\"{value}\"".format(
                    key=key, value=source[key]))
            else:
                tmp_list.append("`{key}`={value}".format(
                    key=key, value=source[key]))
        return " AND ".join(tmp_list)

    def query(self, *args, table: str, where: dict = None,
              order: str = None, desc: bool = False, limit: int = None) -> list:
        fields = ", ".join(["`"+str(x)+"`" for x in args])
        sql_ = """SELECT {fields} FROM `{table}`""".format(
            fields=fields, table=str(table))

        where_ = (where and ("WHERE " + self.build_condition(where))) or ""
        order_ = (order and "ORDER BY {order} {di}".format(
            order=order, di="DESC" if desc else "ASC")) or ""
        limit_ = (limit and "LIMIT {limit}".format(limit=limit)) or ""

        sql = " ".join([sql_, where_, order_, limit_])
        _conn = self.pool_.connection()
        _cur = _conn.cursor()
        _cur.execute(sql)

        rtv = [item for item in _cur.fetchall()]
        _cur.close()
        _conn.close()
        return rtv


mysql = MySqlWallet()
