def pthFactor(n,p):
    hasil=[]
    for i in range(1,n+1):
        if n%i==0:
            hasil.append(i)
    if p<=len(hasil):
        return hasil[p-1]
    else:
        return 0

print(pthFactor(30,8))
