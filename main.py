import random

caracteres= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("digita la longitud de la contraseña: "))
contraseña=""
for i in range(longitud):
    contraseña= contraseña + random.choice(caracteres)

print(contraseña)