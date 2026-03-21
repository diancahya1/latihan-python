#list 

print ("macam macam list")
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
print (list1)
print (list2)
print (list1[0])
print (list2[0])
print (list1[0:3])
print (list2[0:3])
print (list1[0:5:2])
print (list2[0:5:2])
print (list1[-1])
print (list2[-1])
print (list1[-2])
print (list2[-2])



print ("========================")
print ("list of list")
list3 = [[1,2,3],[4,5,6],[7,8,9]]
print (list3)
print (list3[0])
print (list3[1])
print (list3[2])

#ambil data dari list
data = ["ucup","otong","mario","joko"]
print (data[0])

# ambil info jumlah data dalam list (len)
print ("jumlah data dalam list adalah", len(data))

# manipulasi data dalam list
#nambah data di akhir
data.append("budi")
print (data)
print ("jumlah data dalam list adalah", len(data))


#nambah data sesuai posisi yg diinginkan
data.insert(2,"bubu")
print (data)
#nambah list baru
data_baru = ["abi","ui","sobi"]
data.extend(data_baru)
print ("datanya menjadi =",data)

#rubah data
data[0]="yayan"
print ("data setelah diubah =",data)
#hapus data
data.remove("otong")
print ("data setelah dihapus =",data)
#hapus data sesuai index
del data[1]
print ("data setelah dihapus =",data)


#menghitung jumlah data dalam list
baru = [1,2,4,6,2,5,1,3,3,32,]
print ("jumlah angka 4 dalam data yaitu  :",baru.count(4))

#ambil index data dalam list
data_lama = ["Ucup,budi"]
#print ("data ucup berada pada indeks :",data_lama.index("Ucup"))
data_lama.append("budi")
data_lama.append("Ucup")
print ("data lama =",data_lama)


#sort data dalam list(mengurutkan)
angka = [1,2,3,4,6,5,7,8,9,10]
angka.sort()
print ("data angka setelah di sort :",angka)

#reverse (membalikkan data)
angka.reverse()
print ("data angka setelah di reverse :",angka)

#menduplikasi list dengan copy
a= ["budi", "dinda", "jaki"]
b= a.copy()
print ("data b=",b)
c= a.copy()

print ("addres a =",hex(id(a)))
print ("addres b =",hex(id(b)))
print ("addres c =",hex(id(c)))

print ("a=",a)
c[1]= "ucup"
print ("c=",c)

# list yg menjadi satu dan dikelompokkan
peserta_0 = ["ucup",22,"laki-laki"]
peserta_1 = ["budi",23,"laki-laki"]
peserta_2 = ["gita",19,"perempuan"]

list_peserta= [peserta_0,peserta_1,peserta_2]
print (f"peserta = {list_peserta}")

for peserta in list_peserta :
    print (f"nama : {peserta[0]}")
    print (f"umur : {peserta[1]}")
    print (f"gender : {peserta[2]}")
    print ("========================")

