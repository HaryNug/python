def gainMaxValue(security_val, k):
    hasil=[]
    for i in range(0,len(security_val),k):
        hasil.append(security_val[i])   
    return sum(hasil)
print(gainMaxValue([2,-3,4,6,1],2))    