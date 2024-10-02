import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=[]
for i in range(0,nr_letters):
    random1= random.choice(letters[0:52])
    password.append(random1)
    #print(random1)
for i in range(0,nr_numbers):
    random2=random.choice(numbers)
    password.append(random2)
    #print(random2)
for i in range(0,nr_symbols):
    random3=random.choice(symbols[0:9])
    password.append(random3)
    #print(random3)
print(password)
random1= random.shuffle(password)
print(password)

actual_password=""
for i in password:
    actual_password+=i

print(f"your password is :{actual_password}")
