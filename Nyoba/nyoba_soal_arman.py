# Print kelipatan 2 dari o sampai 21
i=0
while i< 21:
    print(i)
    i+=2

# Print kelipatan 2 dari a sampai b:
def nyoba(a,b):
    while a < b:
        print(a)
        a+=2
nyoba(2,30) 

# print keliapatan 2 dari suatu list
def nyoba(a):
    i =0
    while i<len(a):
        if a[i] %2==0:
            print(a[i])
        i+=1
nyoba([1,3,2,10,96,43,56])

# print ganjil genap menjadi list
def nyoba(lst):
    hasil=[]
    i=0
    while i<len(lst):
        if lst[i]%2==0:
            hasil.append("genap")
        else:
            hasil.append("ganjil")
        i+=1 
    return hasil   
print(nyoba([1,3,2,10,96,43,56]))

# output hasil kelipatan 
