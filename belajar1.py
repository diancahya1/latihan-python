#casting tipe data
data_int= 9
print ("data =", data_int, "tipe=", type(data_int))

#jadi kalo mau ganti tipe tinggal tulis aja di depannya
data_str = str(data_int)
data_float = float(data_int)
data_boolean = bool(data_int)

print ("data =", data_str, "tipe=", type(data_str))
print ("data =", data_float, "tipe=", type(data_float))
print ("data =", data_boolean, "tipe=", type(data_boolean))

# input dari user dengan tipe data bool, ini hampir mirip kayak input biasa tapi ada tambahan bool di depannya
data_boolean = bool(int(input("masukkan angka :")))
print ("data =", data_boolean," tipe=", type (data_boolean))

#operasi aritmatika
a= int(input("masukkan angka ;"))
b= int(input("masukkan angka ;"))

#penambahan
hasil= a+b
print (a,'+', b'=', hasil)
#pengurangan
hasil= a-b
print (a,'-',b,'=', hasil)
#perkalian
hasil= a*b
print (a,'*',b,'=',hasil)
#pembagian
hasil= a/b
print (a,'/',b,'=',hasil)
#pangkat
hasil= a**b
print (a,'**',b,'=',hasil)
#modulus/ sisa dari hasil pembagian/dibulatkan
hasil= a%b
print (a,'%',b,'=',hasil)
#floor division(hampir sama kayak modulus yaitu membulatkan ke atas)
hasil= a//b
print (a,'//',b,'=',hasil)
#prioritas operation
'''
1. dalam kurung
2.eksponen
3.perkalian
4.pertambahan dan pengurangan
'''
#-dalam kurung,eksponen,perkalian dan pertambahan

# perhitungan dalam suhu/temperatur
print ("\nprogram konversi temperature")
celcius= float(input("masukkan angka :"))
print ("suhu adalah", celcius,"celcius")
#celcius ke reamur
reamur= (4/5)*celcius
print (reamur)
# celcius ke fahrenheit
farenheit= ((9/5)*celcius)+32
print (farenheit)
# celcius ke kelvin
kelvin= (celcius + 273)
print (kelvin)

# kelvin ke fahrenheit
kelvi= int(input("masukkan angka :"))
kelvin = (9/5)*(kelvi-273)+32
print (kelvin)

# fahrenheit ke kelvin
farenheit= 20
farenheit= (5/9)*(farenheit-32)+273
print (farenheit)