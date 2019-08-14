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


from DatabaseModels.AccountModel import AccountModel
from DatabaseModels.GroupModel import GroupModel
from DatabaseModels.UserModel import UserModel
from DatabaseModels.PostModel import PostModel

my_db = DB('db.db')

AccountsDB = AccountModel(my_db)
GroupsDB = GroupModel(my_db)
UsersDB = UserModel(my_db)
PostsDB = PostModel(my_db)