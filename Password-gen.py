import random
import string
num=int(input("how many letters do you want to generate password?"))
character=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(num):
   password+=random.choice(character)
print(password)