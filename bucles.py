import math
# Bucles
#############################################################################
# Bucles FOR
#############################################################################

# for i in [1,2,3]:
# 	print("Hola")

# for i in ["p", "i", "v", "o"]:
# 	print(i)

# Range

# for x in range(10):
# 	print(x)

# for x in range(1):
# 	print(f"valor de la variable {x}")

# for x in range(5,50,3):
# 	print(f"valor de la variable {x}")

# valido=False
# email=input("Introduce tu email:")
# for x in range(len(email)):
# 	if email[x]=="@":
# 		valido=True

# if valido:
# 	print("email correcto")
# else:
# 	print("email incorrecto")

# contador=0
# email=False
# val_email = input("Ingrese su email: ")
# for x in val_email:
# 	if x == "@" or x == ".":
# 		email=True
# 		contador+=1
# 		break

# if email:
# 	print("email correcto")
# else:
# 	print("email incorrecto")

# if contador == 2:
# 	print("email correcto")
# else:
# 	print("email incorrecto")

#############################################################################
# BUCLE WHILE
#############################################################################

# i=1
# while i<=10000:
# 	print(i)
# 	i+=1

# edad=int(input("introduce tu edad: "))
# while edad < 5 or edad > 100:
# 	print("Ha ingresado una vaina que no es.")
# 	edad=int(input("introduce tu edad: "))

# print("Gracias por participar.")
# print(f"La edad del usuario es {edad}")



print("Calculo de raiz cuadrada")
num=int(input("ingresa un numero: "))
intentos=0
while num<0:
	print("Imposible calcular con negativos")

	if intentos==2:
		print("Ya intento mucho mijo. Chao")
		break

	num=int(input("ingresa un numero: "))
	if num<0:
		intentos+=1

if intentos<2:
	solucion=math.sqrt(num)
	print(f"Raiz cuadrada de {num} es: {solucion}")

# CONTINUE PASS ELSE

# for letra in "python":
# 	if letra=="h":
# 		continue
# 	print("letra " + letra)

nom = "Pildoras Informaticas"
