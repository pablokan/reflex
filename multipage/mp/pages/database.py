import sqlite3

class Database():
    def __init__(self, dbName: str, *args) -> None:
        self.cone = sqlite3.connect(dbName+'.db')
        self.cursor = self.cone.cursor()
        self.tableName = dbName
        fields = list(args)
        if len(fields) != 0:
            self.fieldNames = ['id'] + [field.split()[0] for field in fields]
            strFieldsConTipo = ', '.join(fields)
            query = f"CREATE TABLE IF NOT EXISTS {self.tableName} (id INTEGER PRIMARY KEY, {strFieldsConTipo})"
            self.cursor.execute(query)
            self.cone.commit()
        else:
            self.cursor.execute(f"PRAGMA table_info({self.tableName})")
            dataColumnas = self.cursor.fetchall()
            self.fieldNames = [columna[1] for columna in dataColumnas]      

    def get_all(self):
        self.cursor.execute(f"SELECT * FROM {self.tableName}")
        records = self.cursor.fetchall()
        return records


