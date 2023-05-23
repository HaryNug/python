def divisibleSumPairs(n, k, ar):
    hasil=0
    for i in range(0,n):
        for j in range(i+1,len(ar)):
            if (ar[i]+ar[j])%k==0:
                hasil+=1        
    return hasil
print(divisibleSumPairs(6,3,[1, 3, 2, 6, 1, 2]))
