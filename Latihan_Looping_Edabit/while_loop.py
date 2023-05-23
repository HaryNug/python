# i = 1
# while i < 6:
#   print(i)
#   i += 1

# def jazzify(lst):
#     i=0
#     while i < 3:
#         if "7" not in hurf[i]:
#             hurf[i]+="7"
#         i+=1
#     return lst

# hurf = ['A', 'Z7', 'b', 'c', 'u', 'y']
# print(jazzify(hurf))
def compareTriplets(a, b):
    hasil =[0,0]
    i = 0
    while i < len(a):
        if a[i]>b[i]:
            hasil[0] += 1
        elif a[i]<b[i]:
            hasil[1]+=1
        i+=1
    return hasil
print(compareTriplets([30,30,28,],[29,30,37]))