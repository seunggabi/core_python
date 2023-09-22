import pymysql


class MySQL:
    def __init__(
        self,
        host: str = None,
        user: str = None,
        password: str = None,
        db: str = None,
        charset: str = "utf8",
        database: str = None,
    ):
        database = db or database

        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
        )

        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def select(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def fields(self, table):
        rows = self.select("DESC %s" % table)

        return list(map(lambda x: x[0], rows))
