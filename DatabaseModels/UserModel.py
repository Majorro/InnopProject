import json

def userdata_to_json(row):
    if row is None:
        return None

    user_id, account_id, group_id, result_data,  result_recommendation, posts = row

    user = dict()
    user['user_id'] = user_id
    user['account_id'] = account_id
    user['group_id'] = group_id
    user['result_data'] = json.loads(result_data)
    user['result_recommendation'] = json.loads(result_recommendation)
    user['posts'] = json.loads(posts)
    return user


class UserModel:
    def __init__(self, data_base):
        self.connection = data_base.get_connection()
        self.init_table()

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            account_id INTEGER,
                            group_id INTEGER,
                            result_recommendation BLOB,
                            result_data BLOB,
                            posts BLOB
                        )''')

        cursor.close()
        self.connection.commit()

    def insert(self, user):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users ( 
                            account_id,
                            group_id,
                            result_recommendation,
                            result_data,
                            posts) 

                VALUES (?, ?, ?, ?, ?)''', (
                user['account_id'],
                user['group_id'],
                json.dumps(user['result_recommendation']),
                json.dumps(user['result_data']),
                json.dumps(user['posts'])
          ))

        cursor.execute('''SELECT last_insert_rowid()''')
        id = cursor.fetchone()[0]
        cursor.close()
        self.connection.commit()
        return id

    def get_by_id(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id_user = ?", (str(user_id),))
        rows = cursor.fetchone()
        if not rows:
            return None

        return userdata_to_json(rows)



    def update_user(self, user):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE users SET  
                                        account_id = '{}',
                                        group_id = '{}',
                                        result_recommendation = '{}',
                                        result_data='{}',
                                        posts='{}'
                                        WHERE user_id = ?'''.format(
            user['account_id'],
            user['group_id'],
            json.dumps(user['result_recommendation']),
            json.dumps(user['result_data']),
            json.dumps(user['posts']),
            (user['user_id'],)))

        cursor.close()
        self.connection.commit()
        return

    def delete_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM users WHERE user_id = ?''', (str(user_id),))
        cursor.close()
        self.connection.commit()

    def get_one_by_group_id_and_account_id(self, group_id, account_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE group_id = ? AND account_id = ?",
                       (str(group_id), str(account_id)))
        row = cursor.fetchone()
        return userdata_to_json(row)



# user = dict()
# user['result_recommendation'] = 'Рекомендую тебе подкачаться в проектировании'
# user['result_data'] = {'param1': 1, 'param2': 2, 'что-то там': {'12': '123'}}
# user['posts'] = [1, 2 , 3, 4]
#
# UsersDB.insert(user)
#
# UsersDB.delete_user(1)
