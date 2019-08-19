from app import app
import json
import requests
from flask import request, session, make_response, jsonify, Response, render_template, redirect
from database_config import *

def error(comment):
    result = dict()
    result['status'] = 'Error'
    result['message'] = comment
    return jsonify(result)




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
        return error('Недостаточно данных')

    account = AccountsDB.get_by_login(req['login'])
    if account is None:
        return error('Пользователя не существует')

    if account['password'] != req['password']:
        return error('Неправильный пароль')

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


    print(request.data)

    try:
        req = json.loads(request.data)
        if str(type(req)) != "<class 'dict'>":
            return error('Unknown error')
    except:
        return error('Unknown error')

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
            print('Пропущен атрибут ' + w)
            return error('Missing attribute - ' + w)


    account = AccountsDB.get_by_login(req['login'])

    if not account is None:
        print('Логин занят')
        return error('Данный логин уже зарегистрирован')


    account = dict()
    for i in params:
        account[i] = req[i]

    AccountsDB.insert(account)

    result['status'] = 'Ok'
    result['message'] = ''
    print('Зарегистрировался новый пользователь ' + account['login'])
    return jsonify(result)



@app.route("/req/get_user_info", methods=['GET'])
def req_get_user_info_get():
    result = dict()
    result['status'] = None
    result['message'] = None

    if 'login' not in session:
        return error('User is not authorized')

    account = AccountsDB.get_by_login(session['login'])

    result['status'] = 'Ok'
    result['message'] = ''
    result['data'] = account
    return jsonify(result)

@app.route("/req/get_user_info/<id>", methods=['GET'])
def req_get_user_info_id_get(id):
    result = dict()
    result['status'] = None
    result['message'] = None

    try:
        id = int(id)
    except:
        return error('Wrong id')


    if 'login' not in session:
        return error('User is not authorized')

    account = AccountsDB.get_by_id(id)

    if account is None:
        return error('Nonexistent id')

    result['status'] = 'Ok'
    result['message'] = ''
    result['data'] = account
    return jsonify(result)


@app.route("/req/get_group_info/<id>", methods=['GET'])
def req_get_group_info_id_get(id):
    result = dict()
    result['status'] = None
    result['message'] = None

    try:
        id = int(id)
    except:
        return error('Wrong id')

    if 'login' not in session:
        return error('User is not authorized')

    group = GroupsDB.get_by_id(id)

    if group is None:
        return error('Nonexistent id')

    result['status'] = 'Ok'
    result['message'] = None
    result['data'] = group
    return jsonify(result)


@app.route("/req/get_recomendation/<group_id>", methods=['GET'])
def req_get_recomendation_group_id(group_id):
    result = dict()
    result['status'] = None
    result['message'] = None

    try:
        group_id = int(group_id)
    except:
        return error('Wrong group_id')

    if 'login' not in session:
        return error('User is not authorized')

    user = get_user_id_in_group(session['account_id'], group_id)

    if user is None:
        return error('User is not member this group')

    result['status'] = 'Ok'
    result['message'] = ''
    result['data'] = user['result_recommendation']
    return jsonify(result)



@app.route("/req/send_eval/<group_id>", methods=['GET'])
def req_send_eval_group_id(group_id):
    result = dict()
    result['status'] = None
    result['message'] = None

    try:
        group_id = int(group_id)
    except:
        return error('Wrong group_id')



    if 'login' not in session:
        return error('User is not authorized')

    group = GroupsDB.get_by_id(group_id)
    if group is None:
        return error('Nonexistent group_id')




    req = json.loads(request.data)

    params = ['author_id', 'appreciated_id', 'group_id', 'date', 'parameters', 'comment']
    for par in params:
        if par not in req:
            return error('Missing attribute - ' + par)


    return error('User is not member this group')




