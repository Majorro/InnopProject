import json
def accountdata_to_json(row):
    if row is None:
        return None

    account_id, login, password, first_name, last_name, email, age, person_description, admin_groups, user_groups, invitations, urls, image = row

    account = dict()
    account['account_id'] = account_id
    account['login'] = login
    account['password'] = password
    account['first_name'] = first_name
    account['last_name'] = last_name
    account['email'] = email
    account['age'] = age
    account['person_description'] = person_description
    account['admin_groups'] = json.loads(admin_groups)
    account['user_groups'] = json.loads(user_groups)
    account['invitations'] = json.loads(invitations)
    account['urls'] = urls
    account['image'] = image
    return account


class AccountModel:
    def __init__(self, data_base):
        self.connection = data_base.get_connection()
        self.init_table()

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                            account_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            login TEXT,
                            password TEXT,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            age INTEGER,
                            person_description TEXT,
                            admin_groups BLOB,
                            user_groups BLOB,
                            invitations BLOB,
                            urls BLOB,
                            image BLOB
                            )''')

        cursor.close()
        self.connection.commit()

    def insert(self, account):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO accounts ( 
                                                login,
                                                password,
                                                first_name,
                                                last_name,
                                                email,
                                                age,
                                                person_description,
                                                admin_groups,
                                                user_groups,
                                                invitations,
                                                urls,
                                                image) 

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
            account['login'],
            account['password'],
            account['first_name'],
            account['last_name'],
            account['email'],
            account['age'],
            account['person_description'],
            json.dumps(account['admin_groups']),
            json.dumps(account['user_groups']),
            json.dumps(account['invitations']),
            json.dumps(account['urls']),
            account['image']))

        cursor.execute('''SELECT last_insert_rowid()''')
        id = cursor.fetchone()[0]
        cursor.close()
        self.connection.commit()
        return id

    def get_by_id(self, account_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM accounts WHERE account_id = ?", (str(account_id),))
        rows = cursor.fetchone()
        if not rows:
            return None

        return accountdata_to_json(rows)

    def get_by_login(self, login):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM accounts WHERE login = ?", (str(login),))
        rows = cursor.fetchone()
        if not rows:
            return None
        return accountdata_to_json(rows)

    def update_account(self, account):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE accounts SET  
                                        login = '{}',
                                        password='{}',
                                        first_name='{}',
                                        last_name='{}',
                                        email='{}',
                                        age='{}',
                                        person_description='{}',
                                        admin_groups='{}',
                                        user_groups='{}',
                                        invitations='{}',
                                        urls='{}',
                                        image='{}' WHERE account_id = ? '''.format(
            account['login'],
            account['password'],
            account['first_name'],
            account['last_name'],
            account['email'],
            account['age'],
            account['person_description'],
            json.dumps(account['admin_groups']),
            json.dumps(account['user_groups']),
            json.dumps(account['invitations']),
            json.dumps(account['urls']),
            account['image']),
            (account['account_id'],))

        cursor.close()
        self.connection.commit()
        return

    def delete_account(self, id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM accounts WHERE account_id = ?''', (str(id),))
        cursor.close()
        self.connection.commit()



#Test account
'''
import json
from bytes_functions import *

account = dict()
account['login'] = "admin"
account['password'] = "pass123"
account['first_name'] = "Василий"
account['last_name'] = "Пупкин"
account['email'] = "vasya@mail.ru"
account['age'] = 17
account['person_description'] = "тестовое описание человека"
account['admin_groups'] = [1, 2, 3]
account['user_groups'] = [1]
account['invitations'] = [5, 7]
account['urls'] = {"vk" : "https://vk.com/id1"}
# картинку передавать в байтовом представлении !!!
account['image'] = bytes_to_base64 (b"sadsad123212312sadsdadad321123")
id = AccountsDB.insert(account)
print(id)
'''


# Test get_by_id
'''
    account_id, login, password, first_name, last_name, email, age, person_description, admin_groups, user_groups, invitations, urls, image = AccountsDB.get_by_id(2)
'''

# Test get_by_login
'''
    account_id, login, password, first_name, last_name, email, age, person_description, admin_groups, user_groups, invitations, urls, image = AccountsDB.get_by_login(12)
'''



# Test update account
'''
account = AccountsDB.get_by_id(1)
print(account)
account['first_name'] = 'Кек'

AccountsDB.update_account(account)
print(AccountsDB.get_by_id(1))
'''