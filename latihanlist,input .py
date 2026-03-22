print (" selamat datang ")
  
daftar_belanja = []

while True :
    print ( "\nmenu:")
    print ("1. menampilkan daftar belanja")
    print ("2. menambahkan item ke daftar belanja")
    print ("3. menghapus item dari daftar belanja")
    print ("4. keluar dari program")
    
    try: #agar tidak ada kesalahan dalam menginput
        pilihan= int(input("masukkan angka"))
   
        
        if pilihan == 1:
            if daftar_belanja :
                print ("\nberikut daftar belanja kamu:")
                for i, item in enumerate(daftar_belanja,1): #enumerate itu bira listnya pakek no bukan berjejer
                    print (f"{i}.{item}")
                
            else:
                print ("belum ada daftar belanja untuk saat ini")
        elif pilihan == 2:
            item = input ("masukkan item yang ingin kamu tambahkan :")
            daftar_belanja.append(item)
            print(f"'{item}' telah ditambahkan dalam daftar belanja")
            print (daftar_belanja)
        elif pilihan == 3:
            item = input ("masukkan item yang ingin kamu hapus :")
            if item in daftar_belanja :
                daftar_belanja.remove(item)
                print(f"'{item}' telah di hapus dalam daftar belanja")
            else :
                print (" item yang kamu masukkan tidak ada dalam daftar belanja")
        elif pilihan == 4:
            print ("terimakasih =]")
            break # berhenti biar gak berulang ulang terus
        else :
            print ("pilihan tidak valid")
            
    except ValueError: # ini untuk biar try nya gak merah terus, intinya except= biar gak salah terus
        print ( "pilihan tidak valid, masukkan angka yang sesuai")
   
