import sqlite3
import json


class DB:
    def __init__(self, database_name): # database_name example: olympiads_db.db
        conn = sqlite3.connect(database_name, check_same_thread=False)
        self.connection = conn

    def get_connection(self):
        return self.connection

    def __del__(self):
        self.connection.close()


from DatabaseModels/AccountModel import AccountModel

my_db = DB('db.db')
AccountsDB = AccountModel(my_db)










