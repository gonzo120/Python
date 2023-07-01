
# Reto #4: PRIMO, FIBONACCI Y PAR
#
#  Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  fibonacci y par.
#  Ejemplos:
#  - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  
'''
La serie de Fibonacci es una secuencia de números en la 
que cada número es la suma de los dos números anteriores. 
La secuencia comienza con 0 y 1, y a partir de ahí cada número es la suma 
de los dos números anteriores.

La secuencia de Fibonacci se ve así: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
'''
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def es_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero


def es_par(numero):
    return numero % 2 == 0


def verificar_numero(numero):
    if es_primo(numero):
        primo = "es primo"
    else:
        primo = "no es primo"

    if es_fibonacci(numero):
        fibonacci = "es fibonacci"
    else:
        fibonacci = "no es fibonacci"

    if es_par(numero):
        par = "es par"
    else:
        par = "es impar"

    resultado = f"{numero} {primo}, {fibonacci} y {par}"
    return resultado


# Ejemplos de uso
numero = 6
resultado = verificar_numero(numero)
print(resultado)

numero = 7
resultado = verificar_numero(numero)
print(resultado)
