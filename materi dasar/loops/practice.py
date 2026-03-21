# loop to make segitiga

sisi = 4

count = 1
for i in range (sisi) :
  print ("*"*count)
  count +=1

print ("========================")

count = 1
while True :
    print ("*"*count)
    count += 1
    if count > sisi :
        break
        
print ("========================")
sisi = 6
spasi = int (sisi/2)
count = 1
while True :
  if count%2 :
    print (" "*spasi + "*"*count)
    spasi -=1
    count += 1
  else :
    count += 1
    continue
  if count > sisi :
    break

# ini segitiga full
print ("=================")
sisi = 10
spasi = int (sisi/2)
count = 1
while True:
  if(count %2) :
    print (" "*spasi + "*"*count)
    spasi -=1
    count +=1
  else :
    count +=1
    continue
  if count > sisi :
    break
while True :
  if (count%2) :
    
    spasi +=1
    print(" "*spasi + "*"*count)
    count -=1
  else :
    count -=1
  if count == 0:
    break



