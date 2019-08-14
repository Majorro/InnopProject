import json

def groupdata_to_json(row):
    if row is None:
        return None

    group_id, groupname,  groupimage, admins_id, members_id = row

    group = dict()

    group['group_id'] = group_id
    group['groupname'] = groupname
    group['groupimage'] = groupimage
    group['admins_id'] = json.loads(admins_id)
    group['members_id'] = json.loads(members_id)
    return group


class GroupModel:
    def __init__(self, data_base):
        self.connection = data_base.get_connection()
        self.init_table()

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                            group_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            groupname TEXT,
                            groupimage BLOB,
                            admins_id BLOB,
                            members_id BLOB
                            )''')

        cursor.close()
        self.connection.commit()

    def insert(self, group):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO groups ( 
                            groupname,
                            groupimage,
                            admins_id,
                            members_id) 

                VALUES (?, ?, ?, ?)''', (
                group['groupname'],
                group['groupimage'],
                json.dumps(group['admins_id']),
                json.dumps(group['members_id'])
          ))

        cursor.execute('''SELECT last_insert_rowid()''')
        id = cursor.fetchone()[0]
        cursor.close()
        self.connection.commit()
        return id

    def get_by_id(self, group_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM groups WHERE group_id = ?", (str(group_id),))
        rows = cursor.fetchone()
        if not rows:
            return None

        return groupdata_to_json(rows)



    def update_group(self, group):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE groups SET  
                                        groupname = '{}',
                                        groupimage='{}',
                                        admins_id='{}',
                                        members_id='{}'
                                        WHERE group_id = ?'''.format(
            group['groupname'],
            group['groupimage'],
            json.dumps(group['admins_id']),
            json.dumps(group['members_id'])),
            (group['group_id'],))
        cursor.close()
        self.connection.commit()
        return

    def delete_group(self, group_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM groups WHERE group_id = ?''', (str(group_id),))
        cursor.close()
        self.connection.commit()



# group = dict()
#
# group['groupname'] = 'Google Sheet'
# group['groupimage'] = 'XAXAeqeedsXADADweqe1dsaDAXFAf'
# group['admins_id'] = [5, 3, 1]
# group['members_id'] = [2, 1, 7]

# GroupsDB.insert(group)

# group = GroupsDB.get_by_id(2)
# group['groupname'] = 'Изменено'
# GroupsDB.update_group(group)
# #GroupsDB.update_group()
