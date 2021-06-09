from flask import Flask, render_template, request, redirect, flash, session, send_file
from passlib.hash import sha256_crypt
import pymysql
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO, StringIO  # 그래프를 이미지로 저장하기위한 변환 라이브러리

app = Flask(__name__)

app.secret_key = 'my_secret_key'


# 메인 화면& 로그인
@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('is_logged') is not None:
        return render_template("index.html", user=session.get('is_logged'))
    elif request.method == "POST":
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='1234',
            db='flasktest'
        )
        cursor = db.cursor()
        sql = 'SELECT PW FROM login where ID = %s;'
        usid = request.form['Username']
        ps = request.form['psword']
        cursor.execute(sql, usid)
        user = cursor.fetchone()
        if user is None:
            flash("없는 아이디입니다.")
        elif sha256_crypt.verify(ps, user[0]):
            session['is_logged'] = usid
            return render_template("index.html", user=session.get('is_logged'))
        else:
            flash("틀린 비밀번호입니다.")
        return render_template("log_in.html")
    else:
        return render_template("log_in.html")


# 회원가입 기능
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='1234',
            db='flasktest'
        )
        cursor = db.cursor()
        name = request.form['Name']
        email = request.form['Email']
        id = request.form['Username']
        psword = sha256_crypt.encrypt(request.form['psword'])
        sql_insert = "INSERT INTO `login` (`name`, `email`, `ID` , `PW`) VALUES (%s, %s, %s, %s);"
        val = [name, email, id, psword]
        cursor.execute(sql_insert, val)
        db.commit()
        topic = cursor.fetchall()
        db.close()
        return redirect("/")
    else:
        return render_template("register.html")


# 로그아웃 기능
@app.route('/log_out')
def log_out():
    session.clear()
    return render_template("log_in.html")

# 정보화면 - 아직 만드는 중
@app.route('/about')
def about():
    if session.get('is_logged') is not None:
        return render_template("about.html")
    else:
        return render_template("log_in.html")



if __name__ == '__main__':
    app.run(debug=1)
