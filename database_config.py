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


def get_user_id_in_group(account_id, group_id):
    group = GroupsDB.get_by_id(group_id)
    if group is None:
        return None

    for acc_id, us_id in group['members_id']:
        if str(acc_id) == str(account_id):
            user = UsersDB.get_by_id(us_id)
            return int(us_id)
    return None
