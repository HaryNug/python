from flask import Flask, request, jsonify

app=Flask(__name__)

@app.post("/add")
def penjumlahan():
    a=request.args.get("a")
    b=request.args.get("b")
    response = {"hasil":int(a)+int(b)}
    return jsonify(response)

@app.put("/mltply")
def multiply():
    a=request.headers.get("a")
    b=request.headers.get("b")
    response1={
        "hasil":int(a)*int(b)
              }
    return jsonify(response1)

if (__name__)==("__main__"):
    app.run(debug=True)