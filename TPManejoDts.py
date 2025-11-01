#TP Manejo de Datos - Unidad 8 
# Actividad 2

productos = []

with open(r"D:\Documentos\UTN\1C\Programacion I\Repositorio\UTN-TUPaD-Programacion1\U8\productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")

        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

print("Listado de productos: ")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


# Activdidad 3

print("Agregar producto nuevo: ")
nuevo_nombre = input("Nombre: ")
nuevo_precio = float(input("Precio: "))
nuevo_cantidad = int(input("Cantidad: "))

productos.append({
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nuevo_cantidad
})


# Actividad 4

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nuevo_cantidad}\n")


# Actividad 5

print("Buscar producto ")
buscar = input("Ingrese el nombre del producto a buscar: ")

encontrado = False

for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"Producto encontrado:")
        print(f"Nombre: {p['nombre']}, Precio: {p['precio']}, Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("No existe un producto con ese nombre.")


# Actividad 6

with open(r"D:\Documentos\UTN\1C\Programacion I\Repositorio\UTN-TUPaD-Programacion1\U8\productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo actualizado")