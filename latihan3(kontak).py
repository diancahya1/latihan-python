
print("--------********---------")
print ("selamat datang")
print ("-------********---------")

kontak={}
while True :
    print ("\nmenu")
    print("1.Menampilkan daftar kontak")
    print("2.Menambahkan kontak baru")
    print("3.Menghapus kontak")
    print("4.Mencari kontak berdasarkan nama")
    print("5.Keluar dari program")

    try :
        pilihan=int(input("silahkan masukkan pilihan kamu :"))
    
        
        if pilihan ==1:
            print("berikut daftar kontak kamu :")
            print(kontak)
    
        elif pilihan ==2:
            print("kamu memilih menambahkan daftar kontak")
            key= input("masukkan nama kontak :")
            value= input ("masukkan nomor telepon :")

            if key not in kontak : #ini untuk supaya tidak ada kontak dengan nama yang sama
                kontak[key] = value # supaya kontak ditambahkan
                print ("kontak sudah di tambahkan")
                print (kontak)
            else :
                print ("sudah terdapat kontak yang sama, silahkan tulis nama yang berbeda")
        elif pilihan ==3:
            print ("kamu memilih menghapus kontak")
        
            key= input ("masukkan nama kontak yang ingin dihapus :")
            print (kontak.get(key, "data tidak ditemukan"))
            if key in kontak :
                del kontak[key]
                print (f"kontak {key} telah dihapus!")
            else :
                print (f"kontak {key} tidak ditemukan")
    
        elif pilihan ==4:
            print ("kamu memilih mencari kontak")
            key= input("masukkan nama kontak yang ingin kamu cari :")
            print (kontak.get(key, "kontak tidak ditemukan"))
        
        elif pilihan ==5:
            print ("kamu memilih keluar")
            print ("terimakasih, sampai jumpa lagi")
            break
       
        else:
            print ("pilihanmu tidak valid, silahkan sesuaikan dengan yang ada di pilihan")
        
    except ValueError :
        print ("pilihanmu tidak valid, silahkan sesuaikan dengan yang ada di pilihan")