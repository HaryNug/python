from flask import Flask, request, jsonify

app=Flask(__name__)

@app.get("/path/<int:k>")
def divisibleSumPairs(k):
    n=int(request.args.get("n"))
    ar=request.json["ar"]
    hasil=0
    for i in range(0,n):
        for j in range(i+1,len(ar)):
            if (ar[i]+ar[j])%k==0:
                hasil+=1        
    return jsonify({"hasil":hasil})

if (__name__)==("__main__"):
    app.run(debug=True)