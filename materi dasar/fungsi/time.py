#modul TIME , berhubungan dengan waktu misal 
#mendapatkan waktu saat ini, menunda eksekusi program atau mengukut waktu eksekusi sesuai kode 

#import modul time sebelum menggunakan time
import time 
#fungsi utama yang sering dipakai di time
#a) time.time() ->mendapatkan waktu saat ini dalam detik 
# fungsi ini berguna untuk menghitung waktu eksekusi program

print ("---------------contoh dari fungsi time.time :--------------------")
waktu_sekarang = time.time()
print ("waktu sekarang", waktu_sekarang)

# b) time.sleep(sekon(ini biasanya berupa angka)) ->membuat program berhenti sementara
# fungsi dari time ini, yaitu membuat jeda saat menjalankan loop/simulasi proses    
print ("----------------contoh dari fungsi time.sleep(s)-----------------")
time.sleep(5)

# c) time.ctime(sekon) -> mengubah detik ke waktu yg bisa dibaca
# fungsi dari time ini yaitu untuk mengubah detik ke format waktu yang simple
print ("----------------contoh dari fungsi time.ctime(sekon)--------------")
sekarang = time.time() # memakai fungsi time.time karna time.ctime kan mengubah detik yang sekarang 
print ("waktu sekarang :", time.ctime(sekarang))

# perbedaan time.time dan time.ctime 
# time.time ->menampilkan waktu yang sekarang dalam bentuk detik
# time.ctime -> mengubah time.time ke format yang lebih mudah dibaca, jadi di time.ctime tentunya memerlukan time.time

# d) time.localtime(s) -> mengubah waktu jadi lebih detail
print ("------------------contoh dari fungsi time.localtime---------------")
waktu = time.localtime(time.time ())
print ("waktu hari ini:", (waktu)) # ini lebih detail
print ("tahun:", waktu.tm_year)
print ("bulan:", waktu.tm_mon)
print ("hari:", waktu.tm_mday)

# e)time.strftime -> membuat format sendiri dalam waktu
# fungsi dari time ini yaitu kita dapat membuat format sendiri dalam waktu
# Format yang bisa digunakan(time.strftime):

#%Y → Tahun (2025)
#%m → Bulan (02)
#%d → Hari (07)
#%H → Jam (24 jam format)
#%M → Menit
#%S → Detik
#%a -> nama hari
print ("---------------contoh dari fungsi time.strftime---------------")
a_now= time.localtime ()
a_format = time.strftime ("%a, %Y-%m-%d %H:%M:%S", a_now)
print ("waktu sekarang :", a_format)

deadline= input("silahkan masukkan deadline tugas yang di tambahkan :", "")