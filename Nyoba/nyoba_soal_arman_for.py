# Kelipatan 2 dari 0 sampai 20
# for i in range(0,21):
#     if i%2==0:
#         print(i)
# print()
# Kelipatan 2 dari a sampai b
# def nyoba(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)
# nyoba(2,10)
# print()
# # Kelipatan 2 dari list
# def nyoba(a):
#     for i in a:
#         if i%2==0:
#             print(i)
# nyoba([1,3,2,10,96,43,56])

# print ganjil genap menjadi list
def nyoba(lst):
    hasil_genap=[]
    hasil_ganjil=[]
    for i in lst:
        if i%2==0:
            hasil_genap.append(i)
        else:
            hasil_ganjil.append(i)
    return hasil_genap, hasil_ganjil
print(nyoba([1,3,2,10,96,43,56]))