from flask import Flask, request, jsonify

app=Flask(__name__)

@app.put("/BrkngRcrds")
def breakingRecords():
    scores=request.json["scores"]
    highest_score = lowest_score =scores[0]
    total_highest=total_lowest=0
    for a in scores:
        if highest_score < a:
            highest_score=a
            total_highest+=1
        if lowest_score> a:
            lowest_score=a
            total_lowest+=1
    return jsonify({"Hasil":[total_highest,total_lowest]})

if (__name__)==("__main__"):
    app.run(debug=True)