def birthdayCakeCandles(candles):
    hasil=0
    a= max(candles)
    for i in candles:
        if i==a:
            hasil+=1
    return hasil
print(birthdayCakeCandles([4,2,1,4]))
# nyoba count
