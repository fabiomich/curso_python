# Generadores I
# Estructuras que extraen valores de una funcion y se almacenan
# en objetos iterables, que se pueden recorrer.

def generaPares(limite):
	num=1
	lista=[]
	while num<limite:
		lista.append(num*2)
		num+=1
	return lista

def generaPares2(limite):
	num=1
	while num<limite:
		yield num*2
		num+=1

print(generaPares(10))
generador = generaPares2(10)

print(next(generador))

# for x in generador:
# 	print(x)