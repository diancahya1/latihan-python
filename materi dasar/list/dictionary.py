#dictionary
print ("Selamat datang di program dictionary")
#penjelasan singkat
print ("Program ini akan membantu anda untuk menyimpan data dalam bentuk dictionary")   
print ("Anda bisa memasukkan data dengan format key:value")
print ("Contoh: nama:John, umur:30, kota:Jakarta")
print ("Anda bisa memasukkan data sebanyak yang anda mau")
print ("Untuk keluar dari program ini, ketik 'exit' pada input")
#inisialisasi dictionary
data_dict = {}
while True:
    #input data
    data_input = input("Masukkan data (key:value) atau ketik 'exit' untuk keluar: ")
    if data_input.lower() == 'exit':
        break
    try:
        key, value = data_input.split(':')
        data_dict[key.strip()] = value.strip()
    except ValueError:
        print("Format salah! Gunakan format key:value")
        continue
#tampilkan data
print("\nData yang telah dimasukkan:")
for key, value in data_dict.items():
    print(f"{key}: {value}")
#dictionary dengan data campuran
data_mixed = {
    "nama": "John",
    "umur": 30,
    "kota": "Jakarta",
    "hobi": ["membaca", "bersepeda"],
    "is_student": False
}
print("\nData campuran dalam dictionary:")
for key, value in data_mixed.items():
    print(f"{key}: {value}")
#dictionary dengan data berulang
data_repeated = {
    "nama": "John",
    "umur": 30,
    "kota": "Jakarta",
    "hobi": ["membaca", "bersepeda"],
    "is_student": False,
    "hobi": ["membaca", "bersepeda", "menulis"] # key 'hobi
    # akan diupdate dengan nilai baru
}
print("\nData dengan key berulang dalam dictionary:")   
for key, value in data_repeated.items():
    print(f"{key}: {value}")
#dictionary dengan data tidak berurutan
data_unordered = {
    "kota": "Jakarta",
    "nama": "John",
    "umur": 30,
    "hobi": ["membaca", "bersepeda"]
}
print("\nData tidak berurutan dalam dictionary:")
for key, value in data_unordered.items():
    print(f"{key}: {value}")
#dictionary dengan data berisi list
data_with_list = {
    "nama": "John",
    "umur": 30,
    "kota": "Jakarta",
    "hobi": ["membaca", "bersepeda"]
}
print("\nData dengan list dalam dictionary:")
for key, value in data_with_list.items():
    print(f"{key}: {value}")
#dictionary dengan data berisi set
data_with_set = {  
    "nama": "John",
    "umur": 30,
    "kota": "Jakarta",
    "hobi": {"membaca", "bersepeda"} # set tidak berurutan
}   
print("\nData dengan set dalam dictionary:")
for key, value in data_with_set.items():
    print(f"{key}: {value}")

print ("\n\n","="*20)

#operator pada dictionary
data_dict = {
    "nama": "John",
    "umur": 30,
    "kota": "Jakarta"
}

#panjang
print ("panjang dictionary:", len(data_dict))

# mengecek apakah key ada atau tidak
key = "cup"
checkey= key in data_dict
print (f"apakah {key} ada di data_dict ?",{checkey})

# mengakses nilai dengan key
key = "nama"   
if key in data_dict:
    print(f"Nilai dari {key} adalah: {data_dict[key]}")
else:
    print(f"{key} tidak ditemukan dalam dictionary")

# mengupdate data
data_dict ["umur"] = 20
print (data_dict)
# atau bisa juga dengan cara 
data_dict.update ({"nama":"ucup"})
print (data_dict)

#menghapus data

del data_dict ["kota"]
print (data_dict)

print ("\n\n","="*20)

teman = {
    "cp":"ucup",
    "tp":"tobi",
    "hp":"hendra",
}

#looping dic, yg keluar key nya
for key in teman :
    print (key)

#looping dic, yg keluar value nya

for value in teman.values():
    print(value)
#looping dic, yg keluar key dan value nya
for key, value in teman.items():
    print(f"{key}: {value}")


#dict_copy

print("\n\n","="*20)
# membuat dictionary
data = {
    "a": 1,
    "b": 2,
}
# menyalin dictionary
data_baru = data.copy()
print("Data asli:", data)
print("Data baru:", data_baru)
# mengubah data baru
data_baru["a"] = 3
print("Data baru setelah diubah:", data_baru)
print("Data asli tetap:", data)

