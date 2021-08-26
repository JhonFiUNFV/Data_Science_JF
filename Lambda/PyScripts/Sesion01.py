
# Tipos de datos

# 1) Numéricos

## a) coma flotante

a= 5.6 
b= 8.6
d= a**b 
e= a/b
f= a//b # Herencia

b.__class__ # Atributo 

import math 

math.sqrt(25)


## b) Enteros

e1 = 5
e2 = 8

e3 = e1 + e2
e4 = e1 * e2


e1 = float(e1) # Método o función
e2 = complex(e2)
## c) Complejos

c1 = 4 + 5j
c2 = 5 + 6j

# 2) String

s1 = "Jhon"
s2 = "Lambda"
s3 = "Figueroa"

s4 = s1 + s2 + s3
s4 = s1 + " " + s2

s1.upper()
s2.lower()

# 3) Boleanos

b1 = True
b2 = False

b3 = 4==5
b4 = 6>2

# 4) Non type

n1 = None

# Estructuras de datos
# Estructuras de datos

# 1) Tuple

t1 = 1,2,3,4,5,6,7
t2 = (1,2,3,4,5,6,7)

# Indexación
# Comienza en 0
t1[2]
t1[0]

t2[-1]

# Operación con objetos del mismo tipo
t3 = t1 + (8,9,10)


# 2) Lista
l1 = [1,2,3,4,5,6,7]
l2 = [5,6,7,8,9]
l5 = ["Jhon",6,6,8, "Figueroa"]
l5[0][3]

# Partición (slicing)
l5[0][1:3]




l5_1=l5[0]
l5_1[3]

l3 = l1 + l2

l4 = l1 + t1
l1.__class__
t1.__class__

# Aplicación de métodos=función
l1.append(8)


# 3) Dictionary

d1 = {"Hola":1,
      "Jhon": "Figueroa",
      "3": 2}
 
# Gestión de paquetes
# No trabajar \, /
ruta = "C:/Users/Jhon/OneDrive - Universidad Nacional Federico Villareal/PHYTON/Lambda/sesion 1/687-Modulo34"

import pandas as pd 

# Cargar stata
sumaria = pd.read_stata(ruta+"/"+"sumaria-2019.dta")

# Cargar spss


# Cargar dbf


# Cargar html 