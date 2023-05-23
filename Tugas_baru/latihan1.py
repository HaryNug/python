def nyoba(arr):
# berapa kali didalam array huruf yang berulang
    hasil = 0
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1]:
            hasil= hasil+2 
    return hasil

print(nyoba(["a","b","b","se","sd","sd","c","d","d","e"]))