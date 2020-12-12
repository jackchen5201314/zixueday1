# -*- coding:utf-8 -*-
from flask import Flask\
    , request, session, Request, make_response

app=Flask(__name__)
request:Request
app.secret_key= "key"

@app.route("/request",methods=["GET","POST"])

def hello():
    query=request.args
    post=request.form
    return query,post

@app.route("/session")

def session_handle():
    for k, v in request.args.items():
        session[k] = v
    resp = make_response({k: v for k, v in session.items()})
    for k, v in request.args.items():
        resp.set_cookie(f"cookie_{k}",v)
        return resp

if __name__ == '__main__':
    app.run()



