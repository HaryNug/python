import requests, base64
from flask import Flask, request, jsonify

app=Flask(__name__)

Para_User=[
    {"user1":"Password1"},
    {"user2":"Password2"},
    {"user3":"Password3"}
    ]

@app.get('/')
def login():
    username=request.authorization.username
    password=request.authorization.password
    for users in Para_User:
        for k,v in users.items():
            if k==username and v==password:
                return "Selamat datang user"
    else:
        return False
    
@app.put('/<int:x1>')
def kangaroo(x1):
    if login():
        v1=int(request.args.get("v1"))
        x2=int(request.headers.get("x2"))
        v2=int(request.headers.get("v2"))
        i= 1
        if v1 < v2 or v1 == v2:
            return jsonify({"Hasil":"No"})
        if v1 > v2:
            while i < 10000 :
                if x1+v1*i== x2+v2*i:
                    return jsonify({"Hasil":"Yes"})    
                i+=1
        return jsonify({"Hasil":"No"})
    return "Kamu siapa?"

if (__name__)==("__main__"):
    app.run(debug=True)