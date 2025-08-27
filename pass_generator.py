import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

#Using list comprehension method
password = "".join([random.choice(charValues) for i in range(pass_len)])
print("Password is: ", password)

#Using normal method
password = ""
for i in range(pass_len):
    password += random.choice(charValues)


print("Password is: ", password)