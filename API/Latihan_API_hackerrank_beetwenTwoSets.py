from flask import Flask, request, jsonify

app=Flask(__name__)

@app.post("/BtwnTwSts")
def getTotalX():
    a=request.json["a"]
    b=request.json["b"]
    hasil= 0
    for i in range(max(a),min(b) +1):
        c=[]
        d=[]
        for e in a:
            if i%e==0:
               c.append(i)
        if len(a)==len(c):
            for f in b:
                if f%i==0:
                   d.append(i)
        if len(b)==len(d):
            hasil+=1
    return jsonify({"Hasil":hasil})

if (__name__)==("__main__"):
    app.run(debug=True)