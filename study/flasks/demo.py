# -*- coding:utf-8 -*-
from flask import Flask, request

app = Flask(__name__)


@app.route("/login")
def login():
    name = request.args.get("name")
    pwd = request.args.get("pwd")
    pwd = "123456"

    print(name, pwd)
    return {"name": name, "pwd": pwd}


@app.route("/getpage")
def getpage():
    page = request.args.get("n")
    name = "test"
    return {"name": name, "page": page}


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()
