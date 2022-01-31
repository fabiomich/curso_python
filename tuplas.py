# Diferencia entre tuplas y listas
# es que las Listas van con [ ]
# las Tuplas van con ( )
tupla = ("pepe", 13, 1.2, 2000)
print(tupla[2])
#convertir tuplas en lista y viceversa
lista=list(tupla)
print(lista,tupla)
lista2=["maria", 350]
tupla2=tuple(lista2)
print(lista2, tupla2)
print("pepe" in tupla)
print(tupla2.count(350))
print(len(lista2), len(tupla2))
tupla_unitaria=("-James",) #Tupla unitaria
print(tupla_unitaria)
t1 = ("pablo", 13, 1, 2000)
nombre, dia, mes, agno = t1
print(nombre)
print(dia)
print(mes)
print(agno)