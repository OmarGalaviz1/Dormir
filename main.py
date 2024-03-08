import random

Caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

num = int(input("Ingresa la longitud:"))

clave = ""

for i in range(num):
    clave += random.choice(Caracteres)
print(clave)