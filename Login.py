# -*- coding: utf-8 -*-

from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify
app = Flask(__name__)


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        session['username'] = request.json.get('username')
        session['password'] = request.json.get('password')
        # 登录成功，则跳转到index页面
        return jsonify({'code': 200, 'token': "123456"})
    # 登录失败，跳转到当前登录页面
    return redirect(url_for('login'))


@app.route('/index')
def index():
    # 如果用户名和密码都存在，则跳转到index页面，登录成功
    if 'username' in session and 'password' in session:
        return redirect(url_for('index'))
    # 否则，跳转到login页面
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run(debug=True)
