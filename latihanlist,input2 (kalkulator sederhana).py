print ("-------------******------------")

print ("selamat datang di kalkulator sederhana")
print ("-------------******------------")

while True : #agar program berjalan terus tanpa henti 
    print ("\nmenu:")
    print ("1. pertambahan")
    print ("2. pengurangan")
    print ("3. perkalian")
    print ("4. pembagian")
    print ("5. keluar")
    
    try :
        pilihan= int(input("silahkan masukkan pilihan anda :"))
        
        if pilihan == 1:
            print("kamu memilih pertambahan")
            a= int(input("silahkan masukkan angka pertama :"))
            b= int(input("silahkan masukkan angka kedua :"))
            print ("berikut hasilnya",float(a+b))
            
        elif pilihan == 2:
            print("kamu memilih pengurangan")
            a= int(input("silahkan masukkan angka pertama :"))
            b= int(input("silahkan masukkan angka kedua :"))
            print ("berikut hasilnya",float(a-b))
        
        elif pilihan == 3:
            print("kamu memilih perkalian")
            a= int(input("silahkan masukkan angka pertama :"))
            b= int(input("silahkan masukkan angka kedua :"))
            print ("berikut hasilnya",float(a*b))
        
        elif pilihan == 4:
            print("kamu memilih pembagian")
            a= int(input("silahkan masukkan angka pertama :"))
            b= int(input("silahkan masukkan angka kedua :"))
            if b != 0 :
                print ("berikut hasilnya",float(a/b))
            else:
                print ("tidak terdefinisi")
        
        elif pilihan == 5:
            print ("terimakasih karena telah menggunakan kalkulator sederhana")
            break
        else :
            print("pilihan tidak valid, silahkan masukkan sesuai dengan yang ada di pilihan")      
        
    except ValueError: #agar try tidak menyalahkan semua program
        print ("pilihan tidak valid, silahkan masukkan sesuai dengan yang ada di pilihan")
        
    
