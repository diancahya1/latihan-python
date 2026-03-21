print ("kalkulator sederhana")
print ("========================")

angka1 = float(input(" masukkan angka pertama \t\t:"))
operasi = input("masukkan operasi yang diinginkan (+,-,*,/) :")
angka2 = float(input("masukkan angka kedua \t\t:"))

if operasi == "+":
    hasil = angka1 + angka2
    print("hasil penjumlahan dari",angka1, "+",angka2,"yaitu :",hasil )
    print (angka1 +angka2)
elif operasi == "-" :
    print ("hasil =",angka1+angka2)
elif operasi == "*" :
    print ("hasilnya =",angka1 *angka2)
elif operasi == "/" :
    print ("hasil = ", angka1/angka2)
else :
    print ("operasi unvalid, masukkan yang bener")