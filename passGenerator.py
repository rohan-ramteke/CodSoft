import random
import string

length=int(input("Enter the length of password :"))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

var=lower+upper+num+symbols

p=random.sample(var,length)
password="".join(p)
print()
print("Your Password is :" , password)
