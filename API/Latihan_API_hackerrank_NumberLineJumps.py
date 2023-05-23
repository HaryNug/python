from flask import Flask, request, jsonify

app=Flask(__name__)

@app.put("/path1/<int:x1>")
def kangaroo(x1):
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

if (__name__)==("__main__"):
    app.run(debug=True)