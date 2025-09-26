#Trabajo Practico n° 3 Estructura Ondicionales
#Alumno: Garcias, Maria jose  38628708 , comision n° 5

#Ejercicio 1:

#edad = int (input("Por favor, ingrese su edad:"))
#if (edad > 18 ):
#    print ("Es mayor de edad")

#else:
#    print ("Es menor de edad")

#Ejercicio 2:

#nota = float(input("Por favor, ingrese la nota: "))
#if ( nota >= 6 ):
#    print ("Aprobado")

#else: 
#    print ("Desaprobado")

#Ejercicio 3:

#numero = int (input ("Por favor, ingrese un numero: "))
#if numero % 2 == 0:
#    print ("Ha ingresado un numero par")

#else:
#    print ("Por favor, ingrese un numero par")


#Ejercicio 4: 

#edad = int (input("Por favor, ingrese su edad: "))
#if ( edad < 12 ):
#    print ("Niño/a")

#elif  edad >= 12 and edad < 18:
#    print ("Adolescente")

#elif  edad >= 18 and edad < 30:
#    print ("Adulto/a joven")

#else:
#    print ("Adulto/a")

#Ejercicio 5

#contraseña = input ("Por favor, ingrese una contraseña: ")
#longitud_contraseña = len (contraseña)

#if longitud_contraseña >= 8 and longitud_contraseña <= 14:
#    print ("Ha ingresado una contraseña correcta")

#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6 

#import random
#from statistics import mode, median, mean
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#try: 
#    moda = mode(numeros_aleatorios)

#except:
#    moda = "No definida o única"

#mediana = median(numeros_aleatorios)
#media = mean(numeros_aleatorios)

#print("--- Valores Calculados ---")
#print(f"Lista de 50 números generada: {numeros_aleatorios}")
#print(f"Media (Promedio): {media:.2f}")
#print(f"Mediana (Valor central): {mediana}")
#print(f"Moda (Valor más frecuente): {moda}")
#print("--------------------------")

#if isinstance(moda, (int, float)):

#    if media > mediana and mediana > moda:
#        print("\nEl resultado es:")
#        print("Sesgo positivo o a la derecha. (Media > Mediana > Moda)")

#    elif media < mediana and mediana < moda:
#        print("\nEl resultado es:")
#        print("Sesgo negativo o a la izquierda. (Media < Mediana < Moda)")

#    elif media == mediana and mediana == moda:
#        print("\nEl resultado es:")
#        print("Sin sesgo. (Media = Mediana = Moda)")   

#    else:
#        print("\nEl resultado es:")
#        print("La distribución de los números no cumple estrictamente con el patrón de sesgo positivo, negativo o sin sesgo.")
        
#else:
#    print("\nEl resultado es:")
#    print("No se pudo determinar el sesgo de forma estricta porque la Moda no está definida o es un conjunto multimodal.")

#Ejercicio 7

#Frase_o_palabra = input("Por favor, ingrese una frase o palabra: ")
#VOCALES = "aeiouAEIOU"
#ultimo_caracter = frase_o_palabra[-1]

#if ultimo_caracter in VOCALES:
#    string_final = frase_o_palabra + "!"
#    print(string_final)

#else:
#    print(frase_o_palabra)

# Ejercicio 8:


#nombre = input("Por favor, ingrese su nombre: ")

#print("\nOpciones de formato:")
#print("1. Nombre en MAYÚSCULAS (Ej: PEDRO)")
#print("2. Nombre en minúsculas (Ej: pedro)")
#print("3. Nombre con Inicial Mayúscula (Ej: Pedro)")

#try:
#    opcion = int(input("Ingrese el número de la opción que desea (1, 2 o 3): "))
#except ValueError:
#    print("\nOpción no válida. Debe ingresar un número (1, 2 o 3).")
#    exit() 

#nombre_formateado = "" 

#if opcion == 1:
#    nombre_formateado = nombre.upper()
    
#elif opcion == 2:
#    nombre_formateado = nombre.lower()
    
#elif opcion == 3:
#    nombre_formateado = nombre.title()
    
#else:
#    print("\nOpción no reconocida. Por favor, ingrese 1, 2 o 3.")
    
#if nombre_formateado:
#    print(f"\nResultado: {nombre_formateado}") 


#Ejercicio 9: 

#try:
#    magnitud = float(input("Por favor, ingrese la magnitud del terremoto (escala de Richter): "))
#except ValueError:
#    print("Entrada no válida. Por favor, ingrese un número.")
#    exit()


#if magnitud < 3:
#    categoria = "Muy leve (imperceptible)."
#elif magnitud >= 3 and magnitud < 4:
#    categoria = "Leve (ligeramente perceptible)."
#elif magnitud >= 4 and magnitud < 5:
#    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)."
#elif magnitud >= 5 and magnitud < 6:
#    categoria = "Fuerte (puede causar daños en estructuras débiles)."
#elif magnitud >= 6 and magnitud < 7:
#    categoria = "Muy Fuerte (puede causar daños significativos)."
#elif magnitud >= 7:
#    categoria = "Extremo (puede causar graves daños a gran escala)."
#else:

#    categoria = "Magnitud fuera del rango estándar de clasificación."


#print(f"\nLa magnitud {magnitud} se clasifica como: {categoria}")

#Ejercicio 10

#HEMISFERIO_VALIDO = "NnSs"

#print("Clasificador de Estación del Año")
#hemisferio = input("¿En qué hemisferio se encuentra? (Norte/Sur - Ingrese N o S): ")
#mes = input("Ingrese el mes actual (ej: diciembre): ").lower() 
#try:
#    dia = int(input("Ingrese el día del mes (ej: 25): "))
#except ValueError:
#    print("Error: El día debe ser un número entero.")
#    exit()

#if hemisferio not in HEMISFERIO_VALIDO:
#    print("Error: Hemisferio no válido. Por favor, ingrese 'N' o 'S'.")
#    exit()

#periodo_del_anio = ""

#if (mes == "diciembre" and dia >= 21) or \
#   (mes == "enero") or \
#   (mes == "febrero") or \
#   (mes == "marzo" and dia <= 20):
#    periodo_del_anio = "Periodo 1"

#elif (mes == "marzo" and dia >= 21) or \
#     (mes == "abril") or \
#     (mes == "mayo") or \
#     (mes == "junio" and dia <= 20):
#    periodo_del_anio = "Periodo 2"

#elif (mes == "junio" and dia >= 21) or \
#     (mes == "julio") or \
#     (mes == "agosto") or \
#     (mes == "septiembre" and dia <= 20):
#    periodo_del_anio = "Periodo 3"

#elif (mes == "septiembre" and dia >= 21) or \
#     (mes == "octubre") or \
#     (mes == "noviembre") or \
#     (mes == "diciembre" and dia <= 20):
#    periodo_del_anio = "Periodo 4"

#estacion = "No determinada (revise el nombre del mes)."

#if periodo_del_anio == "Periodo 1":
#    if hemisferio.upper() == 'N':
#        estacion = "Invierno"
#    elif hemisferio.upper() == 'S':
#        estacion = "Verano"

#elif periodo_del_anio == "Periodo 2":
#    if hemisferio.upper() == 'N':
#        estacion = "Primavera"
#    elif hemisferio.upper() == 'S':
#        estacion = "Otoño"

#elif periodo_del_anio == "Periodo 3":
#    if hemisferio.upper() == 'N':
#        estacion = "Verano"
#    elif hemisferio.upper() == 'S':
#        estacion = "Invierno"

#elif periodo_del_anio == "Periodo 4":
#    if hemisferio.upper() == 'N':
#        estacion = "Otoño"
#    elif hemisferio.upper() == 'S':
#        estacion = "Primavera"

#print(f"\nUsted se encuentra en el hemisferio {hemisferio.upper()}.")
#print(f"Para la fecha {dia} de {mes.capitalize()}, la estación es: {estacion}")