class Database:
    def __init__(self, db_name: str, file: list):
        import sqlite3
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.name = db_name
        self.file = file
        self.example = file[0]

    def data_type(self, data):
        return 'TEXT'

    def sql(self):
        output = ''
        for key in self.example:
            output += f' {str(key)} {self.data_type(self.example[key])},'
        return output[:-1]

    def values(self, data):
        output = ''
        for key in data:
            output += f""" "{data[key]}","""
            print(output)
        return output[:-1]

    def create_table(self):
        try:
            self.cursor.execute(f"CREATE TABLE main ({self.sql()})")
            self.connection.commit()
        except Exception as e:
            print('Error : ', e)

    def insert(self, data):
        try:
            self.cursor.execute(f"INSERT INTO main VALUES ({self.values(data)})")
            self.connection.commit()
        except Exception as e:
            print('insert Failed : ',  e)
            self.create_table()

    def insert_all(self):
        for item in self.file:
            self.insert(item)

    def select(self):
        self.cursor.execute(f'SELECT * FROM {self.name}')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def run(self):
        self.insert_all()
        self.select()

    def __del__(self):
        self.connection.close()

