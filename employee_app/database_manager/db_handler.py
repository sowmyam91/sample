import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class SqlManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()

    def get(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def execute(self, query):
        self.cursor.execute(query)

    def get_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
