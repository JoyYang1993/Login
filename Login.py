# -*- coding: utf-8 -*-

from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify
app = Flask(__name__)

# token加密解密


@app.route('/login', methods=('POST',))
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username == 'root' and password == '12345':
        return jsonify({'code': 200, 'msg': 'ok', 'token': username})
    return jsonify({'code': 400, 'msg': 'error'})


@app.route('/index')
def index():
    token = request.headers.get('token')
    if token:
        return jsonify({'code': 200, 'data': {'love': 'lp'}})
    return jsonify({'code': 400})


if __name__ == '__main__':
    app.run(debug=True)

