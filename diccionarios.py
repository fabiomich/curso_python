# Asociacion de tipo clave:valor { }
dicc = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
print(dicc["España"])
dicc["Italia"]="Lisboa"
print(dicc)
dicc["Italia"]="Roma"
print(dicc)
del(dicc["Reino Unido"])
print(dicc)
dicc1 = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
tupla = ["Colombia", "Peru", "Ecuador"]
dicc2 ={tupla[0]:"Bogota",tupla[1]:"Lima",tupla[2]:"Quito"}
print(dicc2)
dicc3 = {23:"Jordan", "nombre":"michael", "Equipo":"Chicago", "anillos":[1991,1992,2000]}
print(dicc3["anillos"][1])
print(dicc.keys())
print(dicc.values())
print(len(dicc3))