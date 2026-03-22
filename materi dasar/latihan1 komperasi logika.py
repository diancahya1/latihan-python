#"---0+++5---8+++11---15+++
# gabungan (or)
pilih= float(input("masukkan angka :"))

# memeriksa setiap angka
a= (pilih >= 0 or pilih <=5)
print (a)

b= (pilih >= 8 or  pilih <= 11)
print (b)

hasil = a or b
print ("jadi hasilnya :", hasil)

# irisan (and)
pilih= float(input("masukkan angka :"))

a= (pilih <= 0 and pilih >=5)
print (a)

b= (pilih <= 8 and pilih >= 11)
print (b)

hasil = a or b
print ("jadi hasilnya :", hasil)


print ("==========================")
'''
1. (10-20)
2. (30-40)
'''
pilih = float(input("masukkan angka :"))

a= (pilih >= 10 and pilih<=20 )
b= (pilih >= 30 and pilih <= 40)

hasil = a or b
print ("jadi hasilnya :", hasil)