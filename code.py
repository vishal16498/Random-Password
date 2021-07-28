import random
l = int(input("How many letters do you need in your password: "))
n = int(input("How many numbers do you need in your password: "))
s = int(input("How many symbol do you need in your password: "))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
for i in range(l):
    password.append(random.choice(letters))
for i in range(n):
    password.append(random.choice(numbers))
for i in range(s):
    password.append(random.choice(symbols))
a = random.sample(password, len(password))
print("".join(a))
