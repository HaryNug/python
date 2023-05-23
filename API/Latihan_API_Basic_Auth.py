import requests, base64
from flask import Flask, request, jsonify

app=Flask(__name__)

@app.get('/login')
def login():
    auth = request.headers.get("Authorization") #ngambil kode dari username dan password
    code = auth[6:] #slicing mengambil kode basic
    decode = (base64.b64decode(code)).decode() #mengubah menjadi bites-(base64)-string
    username = decode.split(":")[0] #mengambil username dengan split pada index
    password = decode.split(":")[1] #mengambil password dengan split pada index

    response= {
        "auth" : auth,
        "code" : code,
        "decode" : decode,
        "username" : username,
        "password" : password
        }
    return jsonify(response)

if (__name__)==("__main__"):
    app.run(debug=True)