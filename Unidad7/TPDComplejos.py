#TP Datos Complejos  - Unidad 7

#Diccionario inicial
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}


# Activadad 1
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Activadad 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)

# Activadad 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)


# Activadad 4
agenda = {}
for _ in range(5):
    nombre = input("Nombre de la persona: ")
    numero = input("Numero: ")
    agenda[nombre] = numero

consulta = input("Ingresa un nombre para buscar su numero: ")

if consulta in agenda:
    print(f"El numero de {consulta} es {agenda[consulta]}")
else:
    print("El contacto no existe")


# Activadad 5
frase = input("Ingresa una frase: ")
palabras = frase.split()
unicas = set(palabras)
print("Palabras unicas: ", unicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Frecuencia de palabras:", conteo)

# Activadad 6
alumnos = {}

for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Nota {i+1} para {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} - Promedio: {promedio:.2f}")

# Actividad 7
parcial1 = {1,2,3,5,7}
parcial2 = {2,3,4,6,7}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", (parcial1 ^ parcial2))
print("Aprobaron al menos uno:", parcial1 | parcial2)

# Actividad 8
stock = {"pan": 20, "leche": 10, "huevos": 30}
producto = input("Producto a consultar: ")

if producto in stock:
    agregar = int(input("Cuantas unidades queres agregar? "))
    stock[producto] += agregar
else:
    nuevo = int(input("El producto no existe, Ingresa stock inicial: "))
    stock[producto] = nuevo

print(stock)

# Activadad 9
agenda = {
    ("Lunes", "10:00"): "Gimnasio",
    ("Martes", "15:00"): "Dentista",
    ("Viernes", "20:00"): "Cine"
}

dia = input("Día: ")
hora = input("Hora: ")

evento = agenda.get((dia, hora), "No hay actividad registrada")
print(evento)

# Actividad 10
paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Perú": "Lima"}
invertido = {capital: pais for pais, capital in paises.items()}
print(invertido)