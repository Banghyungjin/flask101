from flask import Flask, render_template, request, redirect, flash, session, send_file
from passlib.hash import sha256_crypt
import pymysql
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO, StringIO

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("log_in.html")
    # return "Hello World !"
    # if session.get('is_logged') is not None:
    #     return render_template("index.html", user=session.get('is_logged'))
    # elif request.method == "POST":
    #     db = pymysql.connect(
    #         host='localhost',
    #         port=3306,
    #         user='root',
    #         password='1234',
    #         db='busan'
    #     )
    #     cursor = db.cursor()
    #     sql = 'SELECT password FROM users where username = %s;'
    #     usid = request.form['Username']
    #     ps = request.form['psword']
    #     cursor.execute(sql, usid)
    #     user = cursor.fetchone()
    #     if user is None:
    #         flash("없는 아이디입니다.")
    #     elif sha256_crypt.verify(ps, user[0]):
    #         session['is_logged'] = usid
    #         return render_template("index.html", user=session.get('is_logged'))
    #     else:
    #         flash("틀린 비밀번호입니다.")
    #     return render_template("log_in.html")
    # else:
    #     return render_template("log_in.html")


if __name__ == '__main__':
    app.run()
