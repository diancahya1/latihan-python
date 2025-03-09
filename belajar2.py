#operasi komparasi 
# setiap hasil dari operasi komparasi adalah boolean

a=4
b=2
# lebih dari (>)
print ("=========== lebih dari (>)")
hasil= a > 3
print (a,'>',3,hasil)
hasil= 2 > 3
print (2,'>',3,hasil)

# kurang dari (<)
print ("=========== kurang dari (<)")
hasil= a < 3
print (a,'<',3,hasil)
hasil= 2 < 3
print (2,'<',3,hasil)

# lebih dari sama dengan (>=)
print ("=========== lebih dari sama dengan (>=)")
hasil= a >= 3
print (a,'>=',3,hasil)
hasil= 2 >= 3
print (2,'>=',3,hasil)
hasil= a >= 4
print (a,'>=',4,hasil)

# kurang dari sama dengan (<=)
print ("=========== kurang dari sama dengan (<=)")
hasil= a <= 3
print (a,'<=',3,hasil)
hasil= 2 <= 3
print (2,'<=',3,hasil)
hasil= a <= 4
print (a,'<=',4,hasil)

#  sama dengan (==) / adapun juga tidak sama dengan(!=)
print ("===========  sama dengan (==)")
hasil= a == 3
print (a,'==',3,hasil)
hasil= 2 == 3
print (2,'==',3,hasil)
hasil= a == 4
print (a,'==',4,hasil)



#operasi logika/boolean, ada (not,or , and, xor)


# not (membalikkan logika jika dia true maka berubah jadi false)

print ("============not")
a=True
b=False
print ("data a =", not True )
print ("data b", not False)

print ("============contoh if not")
pilih = str(input("masukkan daftar belanja :"))
if not pilih :
    print ("data tidak boleh kosong")
else :
    print ("data ada")

# or (selalu menyatakan true jika salah satu kondisi true)
print ("===============or")
a= False
b= True
c= a or b
print (a,'OR',b,'=',c)

a= False
b= False
c= a or b
print (a,'OR',b,'=',c)

a= True
b= True
c= a or b
print (a,'OR',b,'=',c)   

# AND (kebalikan dari 'or' yaitu akan selalu false jika salah satu kondisi false)
print ("==================AND") 

a= False
b= True
c= a and b
print (a,'AND',b,'=',c)

a= False
b= False
c= a and b
print (a,'AND',b,'=',c)

a= True
b= True
c= a and b
print (a,'AND',b,'=',c)

print ("================XOR") 
# XOR (xor ini akan menyatakan true jika salah satu kondisi terdapat true)
a= False
b= True
c= a ^ b
print (a,'XOR',b,'=',c)
a= False
b= False
c= a ^ b
print (a,'XOR',b,'=',c)
a= True
b= True
c= a ^ b
print (a,'XOR',b,'=',c)

#operasi bitwise

print ("================OPERASI BITWISE")
'''
operasi bitwise ini berhubungan dengan biner bit bit data
ada 4 jenis dalam bitwise
1. or  (|)
2. and (&)
3. xor (^)
'''
print ("==========or")
# or ini kayak penambahan biner gitu 
a= 9
b= 5
c= a | b
print ('nilai :', a, 'dengan binernya yaitu :', format(a,'08b'))
print ('nilai :', b, 'dengan binernya yaitu :', format(b,'08b'))
print ('nilai :', c, 'dengan binernya yaitu :', format(c,'08b'))


print ("==========and")
# and ini kayak perkalian 
c= a & b
print ('nilai :', a, 'dengan binernya yaitu :', format(a,'08b'))
print ('nilai :', b, 'dengan binernya yaitu :', format(b,'08b'))
print ('nilai :', c, 'dengan binernya yaitu :', format(c,'08b'))

print ("==========xor")
# and ini kayak perkalian 
c= a ^ b
print ('nilai :', a, 'dengan binernya yaitu :', format(a,'08b'))
print ('nilai :', b, 'dengan binernya yaitu :', format(b,'08b'))
print ('nilai :', c, 'dengan binernya yaitu :', format(c,'08b'))

print ("==========not")
# and ini kayak perkalian 
c= ~a
d= ~b
print ('nilai :', a, 'dengan binernya yaitu   :', format(a,'08b'))
print ('nilai :', b, 'dengan binernya yaitu   :', format(b,'08b'))
print ('nilai :', c, 'dengan binernya yaitu :', format(c,'08b'))
print ('nilai :', d, 'dengan binernya yaitu  :', format(d,'08b'))
'''
berarti nih di not itu intinya membalik misal dia positif maka ubah jadi negatif begitupun sebaliknya
dan, angka 0 jadi angka 1 begitupun sebalkknya
intinya mengenai bit yang terdiri dari 8 bit dimulai dari kanan.
sama kayak indeks lah di mulai dari kanan yaitu 
misal :
00000000        dan ini hanya mengenal angka 0 dan 1, dan ini berarti misal ada angka 1 di indeks ke 3 
76543210        nah itu sama aja kayak 2^3 artinya 8

00001000        nah ini 2^3

'''
#shifting

#shift right (>>)
# ini artinya menggeser bit ke kanan sebanyak yang di suruh
print ("===============shift right")
c= a >> 2
print ('nilai :', a, 'dengan binernya yaitu   :', format(a,'08b'))

print ('nilai :', c, 'dengan binernya yaitu :', format(c,'08b'))

#shift left (<<)
# ini artinya menggeser bit ke kiri sebanyak yang di suruh dan menambahkan 0 di akhir kanan
print ("===============shift left")

c= b << 2
print ('nilai :', b, 'dengan binernya yaitu   :', format(b,'08b'))

print ('nilai :', c, 'dengan binernya yaitu :', format(c,'08b'))