# Write code below 💖

height = int (input ('what is your height ?'))
credit = int (input (' how many credits you have ?'))

if height >= 137 and credit >= 10 :
   print ('enjoy the ride !')
elif height < 137 and credit >= 10 :
  print ('You are not tall enough to ride')
elif height >= 137 and credit < 10 :
  print ('You dont have enough credits')
else :
  print ('you not met either requirement')

  