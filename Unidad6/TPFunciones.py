# Actividad 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# Actividad 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingresa tu nombre: ")
print(saludar_usuario(nombre))


# Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


# Actividad 4
PI = 3.14159

def calcular_area_circulo(radio):
    return PI * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * PI * radio

radio = float(input("Ingresa el radio del circulo: "))

print("Area del circulo:", round(calcular_area_circulo(radio), 2))
print("Perimetro del circulo:", round(calcular_perimetro_circulo(radio), 2))


# Actividad 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresa una cantidad de segundos: "))
print("Equivalen a horas:", segundos_a_horas(segundos))


# Actividad 6
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}: ")
    for i in range(1, 10 + 1):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresa un numero para ver su tabla: "))
tabla_multiplicar(numero)


# Actividad 7
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))

suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicacion: {mult}, Division: {div}")


# Actividad 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

print(f"Tu IMC es: {calcular_imc(peso, altura):.2f}")


# Actividad 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Ingresa la temperatura en Celsius : "))
print(f"{celsius}°C son {celsius_a_fahrenheit(celsius)}°F")


# Actividad 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))
c = float(input("Tercer numero: "))

print("El promedio es:", calcular_promedio(a, b, c))