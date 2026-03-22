from datetime import datetime 

# sebenarnya ini kurnag penyimpanan dengan menggunakan json tapi aku belum mempelajari sampai sana
print ("---------------*******---------------")
print ("selamat datang")
print ("---------------*******---------------")
sekarang = datetime.now()
daftar_tugas = {}
while True :
    print("1.Menampilkan daftar tugas (beserta deadline-nya).")
    print("2.Menambahkan tugas baru (dengan nama tugas dan deadline).")
    print("3.Menghapus tugas berdasarkan nama tugas.")
    print("4.Mencari tugas berdasarkan nama.")
    print("5.Menampilkan tugas yang paling dekat deadline-nya.")
    print("6.Keluar dari program.")
    
    try :
        pilihan = int(input("silahkan masukkan pilihan anda :"))
        if pilihan ==1:
            print(" kamu memilih daftar tugas")
            print (daftar_tugas)
        
        elif pilihan ==2:
# pada pilihan 2 ini caranya:
#buat input dulu,tambahkan ke dictionary, dan menambahkan datetime, tambahkan pengecekan dan datetime
            print ("kamu memilih menambahkan tugas baru")
            #from datetime import datetime 
            tugas=input("masukkan nama tugas:")
            try : 
            #deadline_dt ini hanya sebuah variabel
                deadline= input ("Masukkan deadline (YYYY-MM-DD):",) 
                deadline_dt= datetime.strptime( deadline,"%Y-%m-%d") #strptime yaitu mengubah string ke datetim  
                if tugas not in daftar_tugas :
                    daftar_tugas [tugas]=deadline_dt 
                    print("tugas telah kamu tambahkan", tugas, '=',deadline)
                else :
                    print ("nama tugas yang kamu masukkan sudah ada,silahkan ganti nama tugas")
            except ValueError:
                print ("silahkan masukkan deadline sesuai dengan yang di format!")
        elif pilihan ==3:
            print ("kamu memilih menghapus tugas")
            tugas = input ("masukkan nama tugas yang ingin di hapus :")
            print (daftar_tugas.get (tugas, "tugas tidak ada"))
            if tugas in daftar_tugas:
                del daftar_tugas [tugas]
                print ("tugas telah kamu hapus")
            else :
                print ("tugas yang ingin kamu hapus tidak ada.")
        
        elif pilihan ==4:
            print ("kamu memilih mencari tugas")
            tugas = input ("tulis nama tugas :")
            print (daftar_tugas.get(tugas, "tugas tidak ada"))
        
        elif pilihan ==5:
            print("kamu memilih menampilkan tugas yang dekat deadline")
            tugas_terdekat = min(daftar_tugas, key=lambda x: daftar_tugas[x])

            for tugas,deadline_dt in daftar_tugas.items():
                if sekarang > deadline_dt :
                    print (f"BEGOK LUU, TUGAS{tugas} LEWAT DEADLINE ANJIRR,(Deadline : {deadline}) ")
                else:
                    sisa_waktu = deadline_dt - sekarang
                    print (f"{tugas}, dengan deadline {deadline}")
        elif pilihan ==6:
            print ("terimakasih dan semangat")
            break
          
    except ValueError :
        print ("pilihan tidak valid, silahkan pilih sesuai dengan yang tertera di pilihan")
    
    
    
    