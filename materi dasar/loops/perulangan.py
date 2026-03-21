# materi pengulangan atau loops
# INI PERULANGAN DASAR
for a in range (100) :
    print ("i love you")


# INI PERULANGAN DENGAN INPUT
angka = int(input("masukkan angka : "))
for i in range(angka):
    print ("i love you ke-", i+1)
print ("================================")
# INI PERULANGAN DENGAN INPUT DAN IF
angka = int(input("masukkan angka : "))
for i in range(angka):
    if i % 2 != 0:
        print ("i love you ke-", i, "ganjil")
    else:
        print ("i love you ke-", i, "genap")

print ("================================")

# INI PERULANGAN DENGAN INPUT DAN WHILE
angka = int(input("masukkan angka : "))
i = 1
while i < angka:
    if i % 2 == 0:
        print ("i love you ke-", i, "genap")
    else:
        print ("i love you ke-", i, "ganjil")
    
print ("================================")
# INI PERULANGAN DENGAN INPUT DAN WHILE UNTUK MENGHITUNG JUMLAH
angka = int(input("masukkan angka : "))
i = 0
jumlah = 0
while i < angka:
    if i % 2 == 0:
        print ("i love you ke-", i+1, "genap")
    else:
        print ("i love you ke-", i+1, "ganjil")
    jumlah += i
    i += 1
print("Jumlah dari 0 sampai", angka, "adalah:", jumlah)
print ("================================")

# INI PERULANGAN DENGAN INPUT DAN WHILE UNTUK MENGHITUNG JUMLAH GENAP
angka = int(input("masukkan angka : "))
i = 0
jumlah_genap = 0
while i < angka:
    if i % 2 == 0:
        print ("i love you ke-", i+1, "genap")
        jumlah_genap += i
    else:
        print ("i love you ke-", i+1, "ganjil")
    i += 1
print("Jumlah angka genap dari 0 sampai", angka, "adalah:", jumlah_genap)
print ("================================")

