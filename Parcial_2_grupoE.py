#Importar librerias
from math import *

#crear variables 

inf="Ingrese el límite de integración inferior:\n"
sup="Ingrese el límite de integración superior:\n"
subint="Ingrese un número impar positivo de subintervalos:\n"
numinv="El valor ingresado no es válido.\n"

#crear funcion lambda
fx=lambda x: sin(x)*(e**(5*x))

#definir datos que se solicitan al usuario
a=float(input(inf)) #limite inferior

b=float(input(sup)) #limite superior

n=int(input(subint)) #cantidad de subintervalos

# Condicionar el ingreso de n a impar positivo
par=n%2
while n<1 or par==0:
    n=int(input(subint))
    par=n%2

# Desarrollo de la función
h = (b-a)/n
xi = a
suma = fx(xi)
for i in range(0,n-2,2):
    xi = xi + h
    suma = suma + 4*fx(xi)
    xi = xi + h
    suma = suma + 2*fx(xi)
xi = xi + h
suma = suma + 4*fx(xi)
suma = suma + fx(b)
integral = (h/3)*suma

#Respuesta
print('El resultado aproximado es: ', integral)
