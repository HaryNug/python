# # Filter huruf vokal
# def nyoba(lst):
#     vokal= "aiueoAIUEO "
#     hasil =[]
#     for i in lst:
#         if i not in vokal:
#             hasil.append(i)
#     return hasil
# print(nyoba("Hello World"))

# Menghitung huruf yang berulang
def perulangan(kata):
    hasil=0
    for k in range(0,len(kata)-1):
        if kata[k]==kata[k+1]:
            hasil=hasil+1
    return hasil
print(perulangan("oodooo"))
        