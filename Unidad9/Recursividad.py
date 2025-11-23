# Trabajo Practico 9 - Recursividad - Garcias Maria Jose  Comision 5

# 1) Factorial recursivo

#def factorial(n):
#    if n == 0 or n == 1:
#        return 1
#    return n * factorial(n - 1)

#num = int(input("Ingrese un número: "))

#for i in range(1, num + 1):
#    print(f"Factorial de {i} = {factorial(i)}")



# 2) Fibonacci recursivo

#def fibonacci(n):
#    if n == 0:
#        return 0
#    if n == 1:
#        return 1
#    return fibonacci(n - 1) + fibonacci(n - 2)


#pos = int(input("Ingrese la posición limite: "))

#print("Serie de Fibonacci:")
#for i in range(pos + 1):
#    print(fibonacci(i), end=" ")



# 3) Potencia recursiva

#def potencia(base, exponente):
#    if exponente == 0:
#        return 1
#    return base * potencia(base, exponente - 1)

#n = float(input("Ingrese la base: "))
#m = int(input("Ingrese el exponente: "))

#resultado = potencia(n, m)
#print(f"{n} elevado a la {m} es = {resultado}")




# 4) Decimal a binario recursivo

#def decimal_a_binario(n):
#    if n == 0:
#        return "0"
#    if n == 1:
#        return "1"
#    return decimal_a_binario(n // 2) + str(n % 2)

#num = int(input("Ingrese un número decimal positivo: "))
#binario = decimal_a_binario(num)
#print(f"El número {num} en binario es: {binario}")