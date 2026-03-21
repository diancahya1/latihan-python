# ini practice untuk dictionary dengan tambahan import datetime

import datetime
import os
import random

data  = {
    "nama":"didi",
    "nim": '000000000',
    'lahir': datetime.datetime(1111, 1, 11),
}

data_mahasiswa= {}

while True:

    os.system("cls")
    print (f"{'selamat datang ':^20}")
    print (f"{'data mahasiswa':^20}")
    print ("="*20)

    mahasiswa = dict.fromkeys(data.keys())
    mahasiswa ['nama'] = input ("masukkan nama mahasiswa :")
    mahasiswa ['nim'] = input ("masukkan nim mahasiswa :")
    tahun_lahir = int(input("masukkan tahun lahir mahasiswa :"))
    bulan_lahir = int(input("masukkan bulan lahir mahasiswa :"))    
    hari_lahir = int(input("masukkan hari lahir mahasiswa :"))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,hari_lahir)

    data_mahasiswa[mahasiswa ['nim']] = mahasiswa

    for key in data_mahasiswa :
        # key adalah nim mahasiswa
        # data_mahasiswa[key] adalah dictionary yang berisi data mahasiswa
        # nama, nim, dan lahir
        # akan diambil dari data_mahasiswa[key]
        # dan ditampilkan dalam format yang sudah ditentukan    
        nama = data_mahasiswa[key]['nama']
        nim = data_mahasiswa[key]['nim']
        lahir = data_mahasiswa[key]['lahir']

        print (f"{key :<6} | {nama :<17} | {nim:<12} | {lahir:%d-%m-%Y}")

    print ("\n")
    is_done = input ("apakah sudah(y/n) :")
    if is_done =="y":
        break
    
print ("terima kasih sudah memasukkan data mahasiswa")

for key in data_mahasiswa :
    nama = data_mahasiswa[key]['nama']
    nim = data_mahasiswa[key]['nim']
    lahir = data_mahasiswa[key]['lahir']

    print (f"{key :<6} {nama :<17} {nim:<12} {lahir:%d-%m-%Y}")
