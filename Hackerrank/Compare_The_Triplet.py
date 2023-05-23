# def compareTriplets(a, b):
#     hasil =[0,0]
#     i = 0
#     while i < len(a):
#         if a[i]>b[i]:
#             hasil[0] += 1
#         elif a[i]<b[i]:
#             hasil[1]+=1
#         i+=1
#     return hasil
                       
# print(compareTriplets([17,28,30],[99,16,8]))

# Convert ke For
def compareTripletsfor(c,d):
    hasil=[0,0]
    i=0
    for k in c:
        if k>d[i]:
            hasil[0] +=1
        elif k<d[i]:
            hasil[1] +=1
        i+=1
    return hasil
print(compareTripletsfor([17,7,2],[9,18,21]))
