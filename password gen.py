#library 
import random
# defining all possible characters 
u_L = "QWERTYUIOPLKJHGFDSAZXCVBNM"
l_l = "qwertyuioplkjhgfdsazxcvbnm"
num ="0123456789"
symbs = "/*-.=+)(&^%$#@!`~_{}[];:'|\<>,?/|\ "
upper, lower, number, symbols = 1,1,1,1

all =""
if upper:
    all+= u_L
    
if lower:
    all+= l_l

if number:
    all+= num
 
if symbols:
    all+= symbs

length = int(input("please enter the password length: "))
amount = int(input("please enter the number of password you need: "))
# loop to generate password
for x in range(amount):
    password= "".join(random.sample(all, length))
    print(password)
    