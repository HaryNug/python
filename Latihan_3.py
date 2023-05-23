nyala = True
angka = 0

print("Case 1")
while (nyala and angka <10) :
    print("Matikan")
    angka +=1
print()

nyala = True
angka = 0
print("Case 2")
while (nyala or angka <10) :
    print("Matikan")
    angka +=1
    nyala = not nyala
print()

nyala = True
angka = 0
print("Case 3")
while (nyala or angka <10) :
    print("Matikan")
    angka +=3
    nyala = not nyala
print()

nyala = True
angka = 0
print("Case 4")
while (nyala and angka <10) :
    print("Matikan")
    angka +=1
    nyala = not nyala
print()
