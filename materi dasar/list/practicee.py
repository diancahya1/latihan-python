list_buku = []

print ("selamat datang")
print ("=========================")
while True:
    buku = input("masukkan judul buku \t:")
    penulis = input ("masukkan penulis buku \t:")


    buku_baru = [buku,penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10)
    for index, buku in enumerate (list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
       
    print("\n\n","="*20)

    islanjut = input("apakah anda ingin menambahkan buku lagi? (y/n) :")
    if islanjut == "n": 
        break   
    
    
    
print("Program selesai")
print("terima kasih sudah memasukkan data buku")