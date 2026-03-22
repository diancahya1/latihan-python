# pertama bikin welcome message 
#kedua input nama
#ketiga bikin games sederhananya
#ketiga input pilihan user 
#dan terakhir bikin if dan elsenya
import random

welcome_message = "WELCOME"
kelinci_position = random.randint (1, 4)

print ("****************")
print (f'*** {welcome_message}  ***')
print ("****************")
nama_user = input("masukkan nama kamu")

print (f''' halo {nama_user} selamat malam, mari bermain temukanlah seekor kelinci
       dari salah satu goa yang tersedia!
       /_\ /_\ /_\ /_\ ''')

pilihan_user = int(input("menurut kamu dimana seekor kelinci itu berada ? (1 /2 /3 /4 )"))

if pilihan_user == kelinci_position :
    print (F"SELAMAT KAMU MENANG! ")
else :
    print (F" kamu kalah, posisi kelinci ada di {kelinci_position}")
