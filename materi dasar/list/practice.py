
#list buku
import os
list_buku=[]
print ("=========================")
print ("masukkan data buku")

while True :
    judul = input ("masukkan judul buku :")
    if judul =="" :
        os.system("cls")
        print ("judul buku harus diisi")
    else :
        break
while True :
    penulis = input ("masukkan nama penulis :")
    if penulis == "" :
        os.system("cls")
        print ("nama penulis harus diisi")
    else :
        break

buku = [judul,penulis]
list_buku.append(buku)
print ("data buku yang dimasukkan =",list_buku)

# Initialize max lengths
max_judul = len(judul)
max_penulis = len(penulis)

# If you plan to append more books in a loop, update max_judul and max_penulis during each append:
# max_judul = max(max_judul, len(judul))
# max_penulis = max(max_penulis, len(penulis))
max_penulis = len(penulis)

default_judul= max(max_judul,10) #default untuk judul
default_penulis = max(max_penulis,10) #default untuk penulis

print("\n\n","="*10)
for index,buku in enumerate(list_buku) :
    print(f"{index+1} | {buku[0]} | {buku[1]}")


print ("=========================")
print ("list buku yang sudah dimasukkan")
print ("judul".ljust(default_judul), "penulis".ljust(default_penulis))

for buku in list_buku:
    judul = buku[0]
    penulis = buku[1]
    print (judul.ljust(default_judul), penulis.ljust(default_penulis))

while True:
    lanjut=input("apakah anda ingin menambahkan buku lagi? (y/n) :")
if lanjut.lower() == "y":
    ...
elif lanjut.lower() == "n" :
    print ("terima kasih sudah memasukkan data buku")
    exit()  
else:
    print ("input tidak valid, silakan masukkan 'y' atau 'n'")
    os.system("cls")

