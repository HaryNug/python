# def isPrime(n):
#     if n>1:
#         for i in range(2,int(n/2)+1):
#             if n%i==0:
#                 return i
#     return 1
#     #     elif n%n==0 and n%i==0:
#     #         hasil.append(i)
#     # return hasil
# print(isPrime(2))

def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return i
    return 1
    # if len(hasil)>2:
    #     return hasil[1:2]
    # else:
    #     return hasil[0:1]
print(isPrime(2))