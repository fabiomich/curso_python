def suma(num1, num2):
	return num1 + num2
def resta(num1, num2):
	return num1 - num2
def multiplica(num1, num2):
	return num1 * num2
def divide(num1, num2):
	try:
		return num1 / num2
	except ZeroDivisionError:
		print("No se puede dividir entre 0.")
		return "Operacion erronea."

op1=(int(input("ingrese 1er numero: ")))
op2=(int(input("ingrese 2do numero: ")))
operacion=input("Ingrese la operacion a realizar (suma, resta, multiplica, divide): ")
if operacion=="suma":
	print(suma(op1,op2))
elif operacion=="resta":
	print(resta(op1,op2))
elif operacion=="multiplica":
	print(multiplica(op1,op2))
elif operacion=="divide":
	print(divide(op1,op2))
else:
	print("Operacion no permitida")
print("Operacion ejecutada")