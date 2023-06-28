'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

'''
Se utiliza un bucle for para iterar a través de los
 números del 1 al 100 (incluyendo ambos extremos). La variable num toma el valor de cada número en cada iteración.

Se utiliza una estructura condicional if-elif-else para evaluar diferentes casos:

a. En la primera condición if, verificamos si el número es divisible tanto por 3 como por 5. Si es así, se imprime "fizzbuzz".

b. En la siguiente condición elif, verificamos si el número es divisible solo por 3. Si es así, se imprime "fizz".

c. En la tercera condición elif, verificamos si el número es divisible solo por 5. Si es así, se imprime "buzz".

d. Si ninguna de las condiciones anteriores se cumple, se ejecuta el bloque else y se imprime el número tal cual.

El resultado se muestra por consola utilizando la función print().
'''