import datetime as dt
# Menggunakan datetime untuk mendapatkan tanggal saat ini

hari = dt.date.today().day
# Menggunakan atribut day untuk mendapatkan hari
print (hari)
bulan = dt.date.today().month
print(bulan)
year = dt.date.today().year
print (year)

print ("hari ini adalah hari :",hari,"bulan :", bulan,"tahun :",year)
input("masukkan tanggal lahir anda (dd/mm/yy) :")
tanggal = int(input("tanggal : \t"))
bulan = int(input("bulan : \t"))
tahun = int(input("tahun : \t"))

tanggal_lahir =dt.date(tahun, bulan, tanggal)
print(tanggal_lahir)

umur = dt.date.today() - tanggal_lahir
# Menghitung selisih antara tanggal hari ini dan tanggal lahir

print ("umur sekarang \t:",umur)
umur_tahun = umur.days// 365
print (" umur sekarnag adalah :", umur_tahun)
