print("Programa de evaluacion de notas de alumnos")
nota_alumno=input("Introduce la nota del alumno: ")
# Condicional IF
def evaluacion(nota):
	valoracion="aprobado"
	if nota < 5:
		valoracion = "suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))

# else elif
print("\nVerificacion de acceso")
edad_usuario=int(input("Introduce la edad: "))
if edad_usuario < 18:
	print("No puedes pasar")
else:
	print("Puedes pasar")
print("El programa termino")

# No existe Switch en Python
edad=-7
if 0 < edad < 100:
	print("Edad es correcta")
else:
	print("Edad es incorrecta")

sal_presi = int(input("Introduce salario del presi: "))
print("Salario presidente: " + str(sal_presi))
sal_dir = int(input("Introduce salario del dir: "))
print("Salario dir: " + str(sal_dir))
sal_area = int(input("Introduce salario del area: "))
print("Salario area: " + str(sal_area))
sal_admin = int(input("Introduce salario del admin: "))
print("Salario admin: " + str(sal_admin))

if sal_admin < sal_area < sal_dir < sal_presi:
	print("Todo funciona")
else:
	print("Alga a fallado")

# programa de BECA
print("Programa de becas")
dist = int(input("introduce la distancia en km: "))
print(dist)
hermanos = int(input("introduce hermanos: "))
print(hermanos)
salario = int(input("introduce salario: "))
print(salario)

if dist > 40 and hermanos > 2 and salario <= 5000:
	print("tienes la beca")
else:
	print("Te jodiste sin beca.")

# Operador IN

print("Asignaturas año 2022")
print("Asignaturas optativas:")
print("Informatica - pruebas - usabilidad")
asignatura=input("Escribe la asignatura escogida: ")
if asignatura in ("Informatica", "pruebas", "usabilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("La asignatura escogida no existe.")