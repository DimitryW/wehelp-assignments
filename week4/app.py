from flask import Flask, request, render_template, redirect, url_for
from flask import session # 記得設定 app.secret_key

app = Flask(__name__, static_folder="static", static_url_path="/")

app.secret_key = "avada kedavra"

# homepage
@app.route("/")
def index():
    if session.get("username")=="test" and session.get('password')=="test":  
    # session["username"]如果不存在會報錯
    # 改用session.get('username')，如果不存在會報 "None"
        return redirect("/member/")
    return render_template("home.html")

@app.route("/signin", methods=["POST"])
def signin():
    name = request.form["username"]
    password = request.form["password"]
    # 將登入資料紀錄在session中
    session["username"] = name
    session['password'] = password
    if name=="test" and password=="test":
        return redirect("/member/")
    elif name=="" or password=="":
        return  redirect(url_for("error", message="請輸入帳號、密碼")) # 利用 url_for 導到對應函式的路由，同時加上 query string
    else:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))

@app.route("/member/")
def member():
    if session.get("username")=="test" and session.get('password')=="test": 
        return render_template("member.html")
    return redirect("/") 

@app.route("/error/")
def error():
    message = request.args.get("message") # 取得 url_for 所導入到網址路徑的 query string
    return render_template("error.html", message=message)

@app.route("/signout")
def signout():
    session.clear()
    return redirect("/")


app.run(port=3000)
