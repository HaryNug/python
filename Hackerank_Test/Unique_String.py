# def UniqueString(strng):
#     for i in strng:
#         if strng.count(i)==1:
#             for a in range(0,len(strng)):
#                 if strng[a]==i:
#                     return a+1
#     return -1
# print(UniqueString("arman"))

# metode index
def UniqueString(strng):
    for i in strng:
        if strng.count(i)==1:
            return strng.index(i)+1
    return -1
print(UniqueString("mama"))