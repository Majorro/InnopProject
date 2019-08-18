from app import app
import json
import requests
from flask import request, session, make_response, jsonify, Response, render_template, redirect
from database_config import *

@app.route("/", methods=['GET'])
def index_get():
    if 'login' not in session:
        return redirect('/login')
    return render_template('index.html')

@app.route("/login", methods=['GET'])
def login_get():
    return render_template('auth.html')

@app.route("/my_groups", methods=['GET'])
def my_groups():
    if 'login' not in session:
        return redirect('/login')
    return render_template('my_groups.html')


@app.route("/del", methods=['GET'])
def del_get():
    global session
    session = {} 
    return redirect('/')







@app.route("/req/auth", methods=['POST'])
def req_auth_post():
    req = json.loads(request.data)
    result = dict()
    result['status'] = None
    result['message'] = None

    if 'login' not in req or 'password' not in req:
        result['status'] = 'Error'
        result['message'] = 'Недостаточно данных'
        return jsonify(result)

    account = AccountsDB.get_by_login(req['login'])
    if account is None:
        result['status'] = 'Error'
        result['message'] = 'Пользователя не существует'
        return jsonify(result)

    if account['password'] != req['password']:
        result['status'] = 'Error'
        result['message'] = 'Неправильный пароль'
        return jsonify(result)

    print('Пользователь вошёл в систему', account['login'])
    result['status'] = 'Ok'
    result['message'] = ''

    session['account_id'] = account['account_id']
    session['login'] = account['login']

    return jsonify(result)



@app.route("/req/reg", methods=['POST'])
def req_reg_post():
    result = dict()
    result['status'] = None
    result['message'] = None

    try:
        req = json.loads(request.data)
        if str(type(req)) != "<class 'dict'>":
            result['status'] = 'Error'
            result['message'] = 'Unknown error'
            return result
    except:
        result['status'] = 'Error'
        result['message'] = 'Unknown error'
        return result

    #print(req)

    req['sex'] = 'male'
    req['urls'] = {"facebook": "https://www.facebook.com/anton.naumtsev"}
    req['image'] = 'test'

    req['admin_groups'] = []
    req['user_groups'] = []
    req['invitations'] = []


    params = ['login', 'password', 'first_name', 'last_name', 'email', 'date', 'person_description', 'urls', 'image', 'sex', 'admin_groups', 'user_groups', 'invitations']



    for w in params:
        if w not in req:
            result['status'] = 'Error'
            result['message'] = 'Missing attribute - ' + w
            print('Пропущен атрибут ' + w)
            return jsonify(result)


    account = AccountsDB.get_by_login(req['login'])

    if not account is None:
        print('Логин занят')
        result['status'] = 'Error'
        result['message'] = 'Данный логин уже зарегистрирован'
        return jsonify(result)


    account = dict()
    for i in params:
        account[i] = req[i]

    AccountsDB.insert(account)

    result['status'] = 'Ok'
    result['message'] = ''
    print('Зарегистрировался новый пользователь ' + account['login'])
    return jsonify(result)
