# # Filter huruf vokal
# def nyoba(lst):
#     vokal="aiueoAIUEO "
#     hasil=[]
#     i=0
#     while i<len(lst):
#         if lst[i] not in vokal:
#             hasil.append(lst[i])
#         i+=1
#     return hasil
# print(nyoba("Hello World"))

# Menghitung huruf yang berulang
def perulangan(kata):
    hasil=0
    i=0
    while i < len(kata):
        if kata[i]==kata[i+1]:
            hasil=hasil+1
        i+=1
    return hasil
print(perulangan("hello"))