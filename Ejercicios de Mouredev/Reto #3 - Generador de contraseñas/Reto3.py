"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
    - Longitud: Entre 8 y 16.
    - Con o sin letras mayúsculas.
    - Con o sin números.
    - Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
"""
import random
import string

def generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_simbolos):
    caracteres = string.ascii_lowercase

    if usar_mayusculas:
        caracteres += string.ascii_uppercase

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    longitud = random.randint(8, 16)
    usar_mayusculas = random.choice([True, False])
    usar_numeros = random.choice([True, False])
    usar_simbolos = random.choice([True, False])
    #random choice eligira una true o false
    

    contrasena = generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_simbolos)
    print("Contraseña generada:", contrasena)

if __name__ == "__main__":
    main()

'''
Importamos los módulos necesarios:

random: para generar números aleatorios y realizar elecciones aleatorias.
string: para obtener conjuntos predefinidos de caracteres, como letras minúsculas, letras mayúsculas, dígitos y símbolos de puntuación.
Definimos la función generar_contrasena que toma cuatro parámetros:

longitud: la longitud deseada de la contraseña.
usar_mayusculas: un valor booleano que indica si se deben usar letras mayúsculas en la contraseña.
usar_numeros: un valor booleano que indica si se deben usar números en la contraseña.
usar_simbolos: un valor booleano que indica si se deben usar símbolos en la contraseña.
Inicializamos la variable caracteres con los caracteres disponibles inicialmente, que son las letras minúsculas.

Si el parámetro usar_mayusculas es True, agregamos las letras mayúsculas a la variable caracteres.

Si el parámetro usar_numeros es True, agregamos los dígitos a la variable caracteres.

Si el parámetro usar_simbolos es True, agregamos los símbolos de puntuación a la variable caracteres.

Generamos la contraseña llamando a la función random.choice para elegir un carácter aleatorio de caracteres en cada iteración del bucle for, y lo concatenamos a la contraseña.

Finalmente, retornamos la contraseña generada.

Definimos la función main que no recibe parámetros. En esta función:

Generamos aleatoriamente la longitud de la contraseña entre 8 y 16 caracteres.
Aleatoriamente decidimos si se deben usar mayúsculas, números y símbolos.
Llamamos a la función generar_contrasena pasando los parámetros generados y asignamos el resultado a la variable contrasena.
Imprimimos la contraseña generada en la consola.
Por último, verificamos si el módulo se está ejecutando directamente mediante __name__ == "__main__", y en ese caso, llamamos a la función main para iniciar la generación de la contraseña.

De esta manera, cada vez que ejecutes el programa, se generará una contraseña aleatoria con los parámetros aleatorios establecidos en ese momento.





'''
