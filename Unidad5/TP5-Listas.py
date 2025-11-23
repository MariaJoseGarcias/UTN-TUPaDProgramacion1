#TP Listas
#Alumno: Garcias Maria Jose  38628708,  comision 5

#Ejercicio 1 

#notas_estudiantes = [7.5, 8.0, 5.5, 9.5, 6.0, 7.0, 9.0, 8.5, 6.5, 10.0]
#CANTIDAD_ESTUDIANTES = len(notas_estudiantes) 

#suma_total = 0
#nota_mas_alta = -1.0  
#nota_mas_baja = 11.0  

#print("--- 1. Lista Completa de Notas ---")
#contador = 1
#for nota in notas_estudiantes:
#    print(f"Estudiante #{contador}: {nota}")
#    contador += 1

#for nota in notas_estudiantes:

#    suma_total += nota

#    if nota > nota_mas_alta:
#        nota_mas_alta = nota
        
#    if nota < nota_mas_baja:
#        nota_mas_baja = nota

#promedio = suma_total / CANTIDAD_ESTUDIANTES

#print(f"El promedio de las {CANTIDAD_ESTUDIANTES} notas es: {promedio:.2f}")
#print(f"La nota más alta obtenida es: {nota_mas_alta}")
#print(f"La nota más baja obtenida es: {nota_mas_baja}")

#Ejercicio 2 

#lista_productos = []
#NUM_PRODUCTOS = 5

#print("Carga de Productos")
#print(f"Por favor, ingrese {NUM_PRODUCTOS} productos:")

#for i in range(NUM_PRODUCTOS):
#    while True:
#        producto = input(f"Producto #{i + 1}: ").strip() 
#        if producto:
#            lista_productos.append(producto)
#            break
#        else:
#            print("El nombre del producto no puede estar vacío. Intente de nuevo.")

#lista_ordenada = sorted(lista_productos)

#print("\nLista Ordenada Alfabéticamente")

#for item in lista_ordenada:
#    print(f"- {item}")

#print("\nEliminación de Producto")

#producto_a_eliminar = input("¿Qué producto desea eliminar de la lista? (Escriba el nombre exacto): ").strip()

#if producto_a_eliminar in lista_productos:

#    lista_productos.remove(producto_a_eliminar)
    
#    print(f"\n'{producto_a_eliminar}' ha sido eliminado")
    

#    print("\nLista Actualizada")
#    if lista_productos:
#        for item in lista_productos:
#            print(f"- {item}")
#    else:
#        print("La lista está vacía.")
        
#else:
#    print(f"\nAtención '{producto_a_eliminar}' no se encontró en la lista.")
#    print("La lista permanece sin cambios.")

#Ejercicio 3

#import random
#CANTIDAD_NUMEROS = 15
#MINIMO = 1
#MAXIMO = 100

#lista_principal = [random.randint(MINIMO, MAXIMO) for _ in range(CANTIDAD_NUMEROS)]

#lista_pares = []
#lista_impares = []

#for numero in lista_principal:

#    if numero % 2 == 0:
#        lista_pares.append(numero)
#    else:
#        lista_impares.append(numero)

#print(f"Lista Principal ({CANTIDAD_NUMEROS} números):")
#print(lista_principal)

#print(f"Lista de Números Pares ({len(lista_pares)} números):")

#for par in lista_pares:
#    print(par, end=" ") 

#print(f"Lista de Números Impares ({len(lista_impares)} números):")

#for impar in lista_impares:
#    print(impar, end=" ")

#Ejercicio 4

#datos_con_duplicados = [1, 3, 5, 3, 7, 1, 9, 5, 3]

#conjunto_sin_duplicados = set(datos_con_duplicados)
#lista_sin_duplicados = list(conjunto_sin_duplicados)

#print("Lista Original")
#print(datos_con_duplicados)

#print("\nLista sin Elementos Repetidos")

#for elemento in lista_sin_duplicados:
#    print(elemento)

#print(f"\nResultado final (sin duplicados): {lista_sin_duplicados}")

#EJercicio 5 

#estudiantes = ["Ana", "Pablo", "Aime", "David","Juan", "Diana", "Gaby", "Hugo"]

#print("Listado de Estudiantes")
#for i in range(len(estudiantes)):
#    print(f"{i + 1}. {estudiantes[i]}")

#print("\nDesea agregar o quitar algun estudiante?")
#opcion = input("Ingrese A o E: ").upper().strip()

#if opcion == "A":
#    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ").capitalize().strip()
#    if nuevo_estudiante != "":
#        estudiantes.append(nuevo_estudiante)
#        print(f"\n{nuevo_estudiante} fue agregado a la lista.")
#    else:
#        print("No se ingreso un nombre válido. Operación cancelada.")

#elif opcion == "E":
#    print("Lista actual para eliminar:")
#    for i in range(len(estudiantes)):
#        print(f"{i + 1}. {estudiantes[i]}")
    
#    nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ").capitalize().strip()

#    if nombre_eliminar in estudiantes:
#        estudiantes.remove(nombre_eliminar)
#        print(f"{nombre_eliminar} fue eliminado de la lista.")
#    else:
#        print(f"El nombre '{nombre_eliminar}' no fue encontrado. La lista no se modifico")

#else:
#    print("Opcion no valida")

#print("Lista final actualizada: ")
#for estudiante in estudiantes:
#    print(f"- {estudiante}")

#Ejercicio 6

#numeros = []
#for i in range(7):
#    valor = int(input(f"Ingrese el numero #{i + 1}: "))
#    numeros.append(valor)

#print("Lista original: ", numeros)

#ultimo = numeros[-1]
#numeros.pop()
#numeros.insert(0, ultimo)

#print("Lista rotada: ", numeros)


#Ejercicio 7 

#temperaturas_semana = [
#    ["Lunes", 15, 25],
#    ["Martes", 18, 30],
#    ["Miércoles", 12, 20],
#    ["Jueves", 19, 32],
#    ["Viernes", 16, 28],
#    ["Sábado", 17, 31],
#    ["Domingo", 20, 29]
#]

#suma_minimas = 0
#suma_maximas = 0
#amplitud_maxima = -1      
#dia_mayor_amplitud = ""

#NUM_DIAS = len(temperaturas_semana)

#for dia_datos in temperaturas_semana:
#    dia_nombre = dia_datos[0]
#    t_min = dia_datos[1]
#    t_max = dia_datos[2]
    
#    suma_minimas += t_min
#    suma_maximas += t_max
    
#    amplitud_actual = t_max - t_min
    
#    if amplitud_actual > amplitud_maxima:
#        amplitud_maxima = amplitud_actual
#        dia_mayor_amplitud = dia_nombre

#promedio_minimas = suma_minimas / NUM_DIAS
#promedio_maximas = suma_maximas / NUM_DIAS

#print("Análisis de Temperaturas Semanales")

#print(f"Promedio de Temperaturas MÍNIMAS: {promedio_minimas:.2f}°")
#print(f"Promedio de Temperaturas MÁXIMAS: {promedio_maximas:.2f}°")

#print("-" * 35)

#print("Mayor Amplitud Térmica Registrada:")
#print(f"Día: {dia_mayor_amplitud}")
#print(f"Amplitud: {amplitud_maxima}° (Máx - Mín)")

#Ejercicio 8

#NOMBRES = ["Ana", "Beto", "Carla", "David", "Elena"]
#MATERIAS = ["Matemáticas", "Historia", "Literatura"]

#notas_estudiantes = [
#    [85, 92, 78],  
#    [70, 88, 95], 
#    [90, 75, 80], 
#    [65, 90, 72], 
#    [82, 85, 90]  
#]

#num_estudiantes = len(notas_estudiantes)
#num_materias = len(notas_estudiantes[0]) 

#suma_por_materia = [0] * num_materias

#print("1. Promedio por Estudiante")

#for i in range(num_estudiantes):
#    notas_del_estudiante = notas_estudiantes[i]
#    nombre_estudiante = NOMBRES[i]
#    suma_estudiante = 0

#    for j in range(num_materias):
#        nota = notas_del_estudiante[j]

#        suma_estudiante += nota

#        suma_por_materia[j] += nota 

#    promedio_estudiante = suma_estudiante / num_materias
#    print(f"Promedio de {nombre_estudiante}: {promedio_estudiante:.2f}")

#print("\n2. Promedio por Materia")

#for k in range(num_materias):
#    nombre_materia = MATERIAS[k]
#    suma = suma_por_materia[k]

#    promedio_materia = suma / num_estudiantes
#    print(f"Promedio de {nombre_materia}: {promedio_materia:.2f}")

#Ejercicio 9 

#tablero = [
#    ["-", "-", "-"],
#    ["-", "-", "-"],
#    ["-", "-", "-"]
#]

#def mostrar_tablero():
#    print("\n  1 2 3 (Columnas)")
#    for i in range(3):
#        print(f"{i + 1}|", end=" ")
#        for j in range(3):
#            print(tablero[i][j], end=" ")
#        print()
#    print()

#def hay_ganador(simbolo):

#    for i in range(3):
#        if tablero[i][0] == simbolo and tablero[i][1] == simbolo and tablero[i][2] == simbolo:
#            return True

#    for j in range(3):
#        if tablero[0][j] == simbolo and tablero[1][j] == simbolo and tablero[2][j] == simbolo:
#            return True

#    if tablero[0][0] == simbolo and tablero[1][1] == simbolo and tablero[2][2] == simbolo:
#        return True

#    if tablero[0][2] == simbolo and tablero[1][1] == simbolo and tablero[2][0] == simbolo:
#        return True

#    return False


#jugador = "X"
#jugadas_realizadas = 0
#ganador = None

#print("TaTeTi-Jugador X vs O")

#while jugadas_realizadas < 9 and ganador is None:
#    mostrar_tablero()
#    print(f"Turno del jugador {jugador}")

#    fila = int(input("Ingrese la FILA (1-3): "))
#    columna = int(input("Ingrese la COLUMNA (1-3): "))

#    if fila < 1 or fila > 3 or columna < 1 or columna > 3:
#        print("Posición fuera de rango. Debe estar entre 1 y 3.")
#        continue

#    fila_idx = fila - 1
#    columna_idx = columna - 1

#    if tablero[fila_idx][columna_idx] != "-":
#        print("Casilla ocupada. Intente otra posición.")
#        continue

#    tablero[fila_idx][columna_idx] = jugador
#    jugadas_realizadas += 1

#    if hay_ganador(jugador):
#        ganador = jugador
#        break

#    if jugador == "X":
#        jugador = "O"
#    else:
#        jugador = "X"

#mostrar_tablero()

#if ganador is not None:
#    print(f"Ganador el jugador {ganador}")
#else:
#    print("Empate. No hay ganador.")

#Ejercicio 10 

#ventas_semana = [
#    [10, 15, 8, 20, 12, 5, 25],
#    [5, 12, 20, 15, 10, 30, 18],
#    [22, 10, 5, 18, 25, 15, 12],
#    [11, 25, 15, 10, 8, 20, 16]
#]

#NOMBRES_PRODUCTOS = ["Lapiz", "Cartuchera", "Cartulina", "Trincheta"]
#NOMBRES_DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

#num_productos = len(ventas_semana)
#num_dias = len(ventas_semana[0])

#total_por_producto = [0] * num_productos
#total_por_dia = [0] * num_dias

#max_venta_producto = -1
#nombre_producto_mas_vendido = ""

#max_venta_dia = -1
#nombre_dia_mas_vendido = ""

#for i in range(num_productos):
#    for j in range(num_dias):
#        venta = ventas_semana[i][j]

#        total_por_producto[i] += venta

#        total_por_dia[j] += venta

#print("1. Total vendido por producto")
#for i in range(num_productos):
#    producto_actual = NOMBRES_PRODUCTOS[i]
#    total = total_por_producto[i]

#    print(f"{producto_actual}: {total} unidades vendidas")

#    if total > max_venta_producto:
#        max_venta_producto = total
#        nombre_producto_mas_vendido = producto_actual

#print("2. Total vendido por día y día con mayores ventas")
#for j in range(num_dias):
#    dia_actual = NOMBRES_DIAS[j]
#    total = total_por_dia[j]

#    print(f"Total {dia_actual}: {total} unidades")

#    if total > max_venta_dia:
#        max_venta_dia = total
#        nombre_dia_mas_vendido = dia_actual

#print("3. Conclusiones")
#print(f"- El producto más vendido en la semana fue: {nombre_producto_mas_vendido} (con {max_venta_producto} unidades).")
#print(f"- El día con mayores ventas totales fue: {nombre_dia_mas_vendido} (con {max_venta_dia} unidades).")
