berat_badan = float(input ("masukkan berat badan kamu(kg): "))
tinggi_badan = float(input ("masukkan tinggi badan kamu(meter): "))

print ("haloo selamat datang")
print ("untuk menentukan apakah berat badan kamu ideal maka tulis jumlah berat dan tinggi kamu")
print ("***********_____**************")
print (" dari data yang telah di temukan berat badan kamu adalag", berat_badan, "kg" "dan tinggi badan kamu adalah", tinggi_badan, "meter")
#dibawah 18 berat badan kurang
#18-24 normal
#25-29 berlebihan
#39 < obesitas 

# mengubah tinggi dari cm ke meter 
    
tinggi_badan = tinggi_badan / 100 
#menghitung bmi
# kita menggunakan tinggi badan > 0 biar hasilnya gak 0,00
if tinggi_badan >0 :
   ideal = berat_badan / (tinggi_badan ** 2)

#lalu gunakan if else dan elif nah kegunaan elif disini yaitu sebagai pengkategorikan elif ih kayak if dalam jumlah banyak
 
if ideal < 18.5 :
     kategori = ("berat badan kurang, makan lebih banyak")
elif 18.5 <= ideal <= 24.5 :
    kategori = ("berat badan normal, bagus")
elif 25.5 <= ideal <= 29 :
    kategori = ("berat badan berlebihan ayok di kurangin")
else :
    kategori = ("obesitas, ayok perhatikan badan kamu lagi")
   
# kegunaan  {bmi:.2f} yaitu untuk mengambil data 2 angka di belakang koma, jadi agar tidak panjang saja
# kegunaan huruf "f" yaitu sebagai formatted string cara praktis memasukkan data variabel ke tipe string , caranya yaitu tuliskan huruf f di awal dan masukkan variable dalam kurung kurawa
print(f" bmi kamu yaitu {ideal:.2f} dan kategrinya yaitu {kategori}")