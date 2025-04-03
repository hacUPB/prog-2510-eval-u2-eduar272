1.
import math
 
# Leer coordenadas
x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))
 
# Calcular distancia
p1 = x2 - x1
p2 = y2 - y1
D = math.sqrt(p1**2 + p2**2)
 
# Mostrar resultado
print("La distancia es:", D)
 
2.
# Leer cantidad de tela
cantidad_tela = float(input("Ingrese la cantidad de tela: "))
 
# Calcular el residuo al dividir por 0.0254
cantidad_restante = cantidad_tela % 0.0254
 
# Mostrar resultado
print("La cantidad restante de tela es:", cantidad_restante)
 
3.
import math
 
# Leer los valores de A y B
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
 
# Calcular la hipotenusa C
C = math.sqrt(A**2 + B**2)
 
# Mostrar el resultado
print("El valor de C es:", C)
 
4.
# Leer la fecha de nacimiento
dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))
año = int(input("Ingrese el año de nacimiento: "))
 
# Leer la fecha actual
dia_actual = int(input("Ingrese el día actual: "))
mes_actual = int(input("Ingrese el mes actual: "))
año_actual = int(input("Ingrese el año actual: "))
 
# Calcular la edad
edad = año_actual - año
 
# Verificar si ya cumplió años este año
if mes_actual < mes or (mes_actual == mes and dia_actual < dia):
    edad -= 1
    print("Aún no ha cumplido años este año.")
elif mes_actual == mes and dia_actual == dia:
    print("¡Feliz Cumpleaños!")
else:
    print("Ya ha cumplido años este año.")
 
# Mostrar la edad
print("Edad:", edad)
 
5.
# Leer datos de entrada
horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
pago_hora = float(input("Ingrese el pago por hora: "))
 
# Calcular sueldo base
sueldo = horas_trabajadas * pago_hora
 
# Aplicar condiciones según el número de horas trabajadas
if 41 <= horas_trabajadas <= 45:
    sueldo *= 2
elif 46 <= horas_trabajadas <= 50:
    sueldo *= 3
elif horas_trabajadas > 50:
    print("No está permitido")
    exit()  # Termina el programa
 
# Mostrar el sueldo final
print("El sueldo es:", sueldo)