def plusMinus(arr):
    hasil1=0
    hasil2=0
    hasil3=0
    for i in arr:
        if i>0:
            hasil1 +=1
        elif i<0:
            hasil2 +=1
        elif i==0:
            hasil3 +=1
    print(hasil1/len(arr))
    print(hasil2/len(arr))
    print(hasil3/len(arr))
            
plusMinus([-4, 3, -9, 0, 4, 1])
