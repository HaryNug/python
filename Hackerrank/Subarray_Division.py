def birthday(s, d, m):
    hasil=0
    for i in range(0,len(s)):
        if sum(s[i:i+m])==d:
            hasil+=1
    return hasil
print(birthday([4],4,1))