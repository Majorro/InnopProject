import json

def postdata_to_json(row):
    if row is None:
        return None

    post_id, author_id, appreciated_id, group_id, date, parameters, comment = row

    post = dict()

    post['post_id'] = post_id

    post['author_id'] = author_id
    post['appreciated_id'] = appreciated_id
    post['group_id'] = group_id
    post['appreciated_id'] = appreciated_id
    post['date'] = date
    post['parameters'] = json.loads(parameters)
    post['comment'] = comment
    return post


class PostModel:
    def __init__(self, data_base):
        self.connection = data_base.get_connection()
        self.init_table()

    def init_table(self):
        cursor = self.connection.cursor()

        #post_id, author_id, appreciated_id, group_id, date, parameters, comment
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                            post_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            author_id INTEGER,
                            appreciated_id INTEGER,
                            group_id INTEGER,
                            date BLOB,
                            parameters BLOB,
                            comment BLOB
                            )''')

        cursor.close()
        self.connection.commit()

    #post_id, author_id, date, parameters, comment


    def insert(self, post):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO posts ( 
                            author_id, 
                            appreciated_id,
                            group_id,
                            date, 
                            parameters, 
                            comment) 

                VALUES (?, ?, ?, ?)''', (
                post['author_id'],
                post['appreciated_id'],
                post['group_id'],
                post['date'],
                json.dumps(post['parameters']),
                post['comment']
          ))

        cursor.execute('''SELECT last_insert_rowid()''')
        id = cursor.fetchone()[0]
        cursor.close()
        self.connection.commit()
        return id

    def get_by_id(self, post_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM posts WHERE post_id = ?", (str(post_id),))
        rows = cursor.fetchone()
        if not rows:
            return None

        return postdata_to_json(rows)



    def update_post(self, post):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE posts SET  
                                        author_id = '{}',
                                        appreciated_id = '{}',
                                        group_id = '{}',
                                        date='{}',
                                        parameters='{}',
                                        comment='{}'
                                        WHERE post_id = ?'''.format(
            post['author_id'],
            post['appreciated_id'],
            post['group_id'],
            post['date'],
            json.dumps(post['parameters']),
            post['comment']),

                       (post['post_id'],))
        cursor.close()
        self.connection.commit()
        return

    def delete_post(self, post_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM posts WHERE post_id = ?''', (str(post_id),))
        cursor.close()
        self.connection.commit()

    def get_all_by_group_id(self, group_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM posts WHERE group_id = ?", (str(group_id),))
        rows = cursor.fetchall()
        all = []
        for w in rows:
            all.append(postdata_to_json(w))
        return all

    def get_all_by_group_id_and_account_id(self, group_id, account_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM posts WHERE group_id = ? AND appreciated_id = ?", (str(group_id), str(account_id)))
        rows = cursor.fetchall()
        all = []
        for w in rows:
            all.append(postdata_to_json(w))
        return all

'''
post = dict()
post['author_id'] = 1
post['appreciated_id'] = 2
post['group_id'] = 3
post['date'] = '01.02.2001'
post['parameters'] = {'param1':'123123', 'param2': '123', 'param3': {'param4': '123', 'param5': '123'}}
post['comment'] = 'Вы плохо высказывает свои мысли, постарайтесь выражаться более внятно.'
'''

#post = PostsDB.get_by_id(1)

'''
post = PostsDB.get_by_id(3)
print(post)
post['parameters']['new_param'] = 'text'
PostsDB.update_post(post)
'''


# PostsDB.delete_post(3)