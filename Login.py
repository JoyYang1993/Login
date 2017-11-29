# -*- coding: utf-8 -*-

from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify
app = Flask(__name__)


@app.route('/login', methods=('POST',))
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username == 'root' and password == '12345':
        return jsonify({'code': 200, 'msg': 'ok', 'token': username})
    return jsonify({'code': 400, 'msg': 'error'})


if __name__ == '__main__':
    app.run(debug=True)

