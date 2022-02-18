from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask import session  # 記得設定 app.secret_key
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vaapad666",
    database="mydatabase"
)
mycursor = mydb.cursor(buffered=True)  # buffered=True 才能正確得出mycursor.rowcount

app = Flask(__name__, static_folder="static", static_url_path="/")

app.secret_key = "wingardiumleviosa"


@app.route("/")
def index():
    if "username" in session:
        return redirect("/member/")
    return render_template("home.html")


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    mycursor.execute("SELECT * FROM member WHERE username= %s", (username,))
    # In Python, a tuple containing a single value must include a comma. For example, ('abc') is evaluated as a scalar while ('abc',) is evaluated as a tuple.
    if mycursor.rowcount == 0:
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (name, username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("home.html")
    else:
        return redirect(url_for("error", message="帳號已經被註冊"))


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    mycursor.execute(
        "SELECT * FROM member WHERE username= %s AND password= %s", (username, password))
    if mycursor.rowcount == 1:
        # 將登入資料紀錄在session中
        session["username"] = username
        session["password"] = password
        return redirect("/member/")
    elif username == "" or password == "":
        # 利用 url_for 導到對應函式的路由，同時加上 query string
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))


@app.route("/member/")
def member():
    if "username" in session:
        mycursor.execute(
            "SELECT name FROM member WHERE username=%s", (session['username'],))
        name = mycursor.fetchone()[0]
        return render_template("member.html", name=name)
    return redirect("/")


@app.route("/error/")
def error():
    message = request.args.get("message")  # 取得 url_for 所導入到網址路徑的 query string
    return render_template("error.html", message=message)


@app.route("/signout")
def signout():
    session.clear()
    return redirect("/")


@app.route("/api/members")
def products():
    username = request.args.get("username")
    mycursor.execute("SELECT * FROM member WHERE username= %s", (username,))
    if mycursor.rowcount > 0:
        result = mycursor.fetchone()
        output = {
            "data": {
                "id": result[0],
                "name": result[1],
                "username": username
            }
        }
        return jsonify(output)
    else:
        output = {
            "data": None
        }
        return jsonify(output)


app.run(port=3000)
