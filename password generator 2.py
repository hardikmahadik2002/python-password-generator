import random
import string

print("Hello,Welcome to Password Generator")

length = int(input("\nEnter the length of password :"))

#american standard code for information interchange

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

h = lower + upper + number + symbols

b= random.sample(h,length)

password = "".join(b)

h = string.ascii_letters + string.digits + string.punctuation

password ="".join(random.sample(h,length))

print(password)
 
