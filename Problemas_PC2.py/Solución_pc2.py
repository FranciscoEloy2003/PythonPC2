#PROBLEMA 1:Escribe un programa en Python para encontrar los números que son divisibles por 7 
# y múltiplos de 5, en el rango de 1500 y 2700 
numeros_cumplidores = []

# Iteramos a través del rango de 1500 a 2700 (ambos incluidos)
for numero in range(1500, 2701):
    # Verificamos si el número es divisible por 7 y múltiplo de 5
    if numero % 7 == 0 and numero % 5 == 0:
        # Si cumple ambas condiciones, lo añadimos a la lista
        numeros_cumplidores.append(numero)

# Imprimimos los números que cumplen las condiciones
print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros_cumplidores)


#PROBLEMA 2: Definir la función que imprime el patrón
def imprimir_patron(n):
    # Imprimir la parte superior del patrón
    for i in range(1, n + 1):
        print('* ' * i)

    # Imprimir la parte inferior del patrón
    for i in range(n - 1, 0, -1):
        print('* ' * i)

# Llamar a la función con el tamaño deseado del patrón
imprimir_patron(5)


#PROBLEMA 3:numeros = []  # Lista para almacenar los números ingresados
numeros = []  # Lista para almacenar los números ingresados
num_pares = 0
num_impares = 0

continuar = True

while continuar:
    respuesta = input("Desea ingresar un número? (SI/NO): ")
    if respuesta.upper() == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta.upper() == "NO":
        continuar = False
    else:
        print("Respuesta no válida. Por favor ingrese 'SI' o 'NO'.")

# Contar números pares e impares
for num in numeros:
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

# Mostrar resultados
print("Números ingresados:", numeros)
print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)


#PROBLEMA 4: Función para ingresar 
def ingresar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la calificación {i+1} del alumno {nombre}: "))
        notas.append(nota)
    return {"Alumno": nombre, "Notas": notas}

# Función para mostrar el listado completo de alumnos
def mostrar_listado(alumnos):
    print("Listado de alumnos:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# Programa principal
def main():
    alumnos = []
    n = int(input("Ingrese el número de alumnos: "))
    for _ in range(n):
        alumno = ingresar_alumno()
        alumnos.append(alumno)
    mostrar_listado(alumnos)

if __name__ == "__main__":
    main()



#PROBLEMA 5:
def contar_digitos(numero, digito):
    # Convertir el número a cadena para usar el método count
    numero_str = str(numero)
    # Contar la cantidad de veces que aparece el dígito en el número
    cantidad = numero_str.count(str(digito))
    return cantidad

# Ejemplo de uso
numero_ingresado = 15789000
digito = 0
cantidad = contar_digitos(numero_ingresado, digito)
print(f"Cantidad de veces {digito} en el número: {cantidad}")



#PROBLEMA 6: Función para generar la serie de Fibonacci hasta un límite dado
def fibonacci(limite):
    # Inicializamos los dos primeros números de la serie
    a, b = 0, 1
    fibonacci_series = []

    # Agregamos 0 a la serie ya que es el primer número de Fibonacci
    fibonacci_series.append(a)

    # Generamos la serie de Fibonacci hasta el límite especificado
    while b <= limite:
        fibonacci_series.append(b)
        a, b = b, a + b

    return fibonacci_series

# Llamamos a la función e imprimimos la serie de Fibonacci hasta el número 50
fib_series = fibonacci(50)
print("Serie de Fibonacci hasta el número 50:", fib_series)



#PROBLEMA 7:
def es_primo(numero):
    # Verificar si el número es menor que 2
    if numero < 2:
        return False
    # Iterar sobre los números desde 2 hasta la raíz cuadrada del número + 1
    for i in range(2, int(numero ** 0.5) + 1):
        # Si el número es divisible por algún número en este rango, no es primo
        if numero % i == 0:
            return False
    # Si no fue divisible por ningún número en el rango, es primo
    return True

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
    
    

#PROBLEMA 8: Escribe una función de Python para calcular el factorial de un número
def factorial(numero):
    # Verificar si el número es 0 o 1, en cuyo caso el factorial es 1
    if numero == 0 or numero == 1:
        return 1
    # Inicializar el resultado del factorial como 1
    resultado = 1
    # Iterar desde 2 hasta el número dado, multiplicando el resultado en cada iteración
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
numero = int(input("Ingrese un número entero no negativo: "))
if numero < 0:
    print("El factorial de un número negativo no está definido.")
else:
    print("El factorial de", numero, "es:", factorial(numero))
    

#PROBLEMA 9: 
def omitir_vocales(cadena):
    vocales = 'aeiouAEIOU'  
    resultado = ''  
    
    for letra in cadena:
        if letra not in vocales: 
            resultado += letra
    
    return resultado

# Solicitar al usuario que ingrese el texto
texto = input("Ingrese el texto: ")

# Llamar a la función e imprimir el resultado
resultado = omitir_vocales(texto)
print("Texto sin vocales:", resultado)



#PROBLEMA 10:
def obtener_mes_numero(mes):
    meses = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }
    return meses.get(mes, "00")

def convertir_fecha(input_fecha):
    # Separar la entrada por espacios y comas
    partes_fecha = input_fecha.replace(",", "").split()
    
    # Si la fecha está en formato mes/día/año
    if "/" in partes_fecha[0]:
        mes, dia, año = partes_fecha[0].split("/")
    else: # Si la fecha está en formato mes día, año
        mes = partes_fecha[0]
        dia = partes_fecha[1]
        año = partes_fecha[2]
    
    # Obtener el número del mes
    mes_numero = obtener_mes_numero(mes)
    
    # Formatear la fecha en AAAA-MM-DD
    fecha_formateada = "{}-{}-{}".format(año, mes_numero, dia.zfill(2))
    
    return fecha_formateada

# Ejemplos de uso
input_fecha = input("Ingrese la fecha en formato mes/día/año o mes día, año: ")
fecha_formateada = convertir_fecha(input_fecha)
print("Fecha en formato AAAA-MM-DD:", fecha_formateada)
