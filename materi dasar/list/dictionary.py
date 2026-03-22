#dictionary struktur yang memiliki pasangan key dan value   
#key is like name or something pokoknya yang ada di bagian depan
#value is like the answer of key 

# bentuk dasar dari dictionary :
# dictionary = {key : value}

# ini contoh dari dictionary

mahasiswa = {
    "nama": "Budi",
    "umur": 20
    ,
    "jurusan": "Informatika"
}

# dan dictionary selalu menggunakan key untuk memanggil data 

# contoh, (ini datanya berdasarkan data di atas ya)
print (mahasiswa ["nama"])
print (mahasiswa ["umur"]) 

# penggunaan get yaitu untuk memastikan apkah key itu ada di dalam dictionary atau tidak
# get = untuk memastikan dan tidak terjadi eror. contohnya :
print (mahasiswa.get("alamat", "data tidak di temukan")) # contoh data yang tidak di temukan di dictionary

#dan jika ingin menambahkan data/key baru ke dictionary
mahasiswa ["angkatan"]= 2023
mahasiswa ["jurusan"]= "teknik_telekomunikasi"
print (mahasiswa["angkatan"])
print (mahasiswa ["jurusan"])
print (mahasiswa.get("umur", "data belum diisi"))

print("---------------******-----------------")
# menghapus data/key dalam dictionary (ada 2 cara)

del mahasiswa["angkatan"]
print (mahasiswa)

# cara ke 2 :
mahasiswa.pop("umur")
print (mahasiswa)

print ("------------*******-------------")

# ada juga dictionary dalam dictionary(nested dictionary)
data = {
    1001:{"nama" : "susi", "umur" : " 23"},
    1002:{"nama" : "lila" , "umur" :"11" }
}
print (data [1001]["nama"])

print ("------------********------------")
#looping di dictionary
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

# looping hanya key nya saja
for key in mahasiswa:
    print(key)

# looping hanya value saja
for value in mahasiswa.values():
    print(value)
    
# looping key dan value sekaligus
for key,value in mahasiswa.items():
    print (f"{key}",{value})

