lista = [1, '2', "3", 4, 5]
print(type(lista[1]))
nombres=["pedro","maria","juan","sandra"]
# Busca desde el ultimo al primero -1, -2 -3
print(nombres[-1])
# Busca en porciones desde cero hasta 2, excluye el 3
print(nombres[0:3])
print(nombres[:2])
print(nombres[2:])

nombres.append("fago") # Agrega elemento al final de la lista
nombres.insert(2,"pepe")
nombres.extend(["nombre1","nombre2"])
print(nombres.index("pepe"))
print("fago" in nombres)
nombres.remove("pepe")
nombres.pop() #Elimina el ultimo elemento de la lista

nombres2=["juanito","ximena"]
nombres3=nombres+nombres2
print(nombres3)
for x in nombres:
	print(x)