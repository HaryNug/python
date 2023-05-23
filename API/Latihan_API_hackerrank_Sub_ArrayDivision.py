from flask import Flask, request, jsonify

app=Flask(__name__)

@app.post("/brthdy")
def birthday():
    s=request.json["s"]
    d=request.json["d"]
    m=request.json["m"]
    
    hasil=0
    for i in range(0,len(s)):
        if sum(s[i:i+m])==d:
            hasil+=1
    return jsonify({"hasil":hasil})

if (__name__)==("__main__"):
    app.run(debug=True)