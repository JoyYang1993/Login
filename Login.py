# -*- coding: utf-8 -*-

import pymysql.cursors
from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify
app = Flask(__name__)

# token加密解密


@app.route('/login', methods=('POST',))
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username and password:
        # 连接数据库
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='', db='yj', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        cursor = connection.cursor()
        # 操作sql
        selectUserSql = "SELECT `username`, `password` FROM `account` WHERE username='" + username + "'"
        print selectUserSql
        cursor.execute(selectUserSql)
        result = cursor.fetchone()
        print result
        if result and result['password'] == password:
            return jsonify({'code': 200, 'msg': 'ok', 'token': username})
    return jsonify({'code': 400, 'msg': 'error'})




@app.route('/index')
def index():
    token = request.headers.get('token')
    if token:
        return jsonify({'code': 200, 'data': {'love': 'lp'}})
    return jsonify({'code': 400})


@app.route('/register', methods=('POST', ))
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if username and password:
        # 连接数据库
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='', db='yj', charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        cursor = connection.cursor()
        # 插入数据
        insertSql = "INSERT INTO `account` (`username`, `password`) VALUES ( '"+username + "','" + password + "')"
        print insertSql
        cursor.execute(insertSql)
        # 提交
        connection.commit()
        return  jsonify({'code': 200})
    return jsonify({'code': 400})


if __name__ == '__main__':
    app.run(debug=True)

