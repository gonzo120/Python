def hacker_language(text):
    leet_alphabet = {
        'a': '4',
        'b': 'I3',
        'c': '[',
        'd': ')>',
        'e': '3',
        'f': '|=',
        'g': '&',
        'h': '#',
        'i': '1',
        'j': '_|',
        'k': '>|',
        'l': '1',
        'm': '/\/\\',
        'n': '^/',
        'o': '0',
        'p': '|*',
        'q': '(_,)',
        'r': 'I2',
        's': '5',
        't': '7',
        'u': '(_)',
        'v': '\/',
        'w': '\/\/',
        'x': '><',
        'y': 'j',
        'z': '2'
    }
    leet_text = ''
    for char in text.lower():
        if char.isalnum():
            leet_text += leet_alphabet.get(char, char) #comprueba que la frase introducida sea alfanumérica
        else:
            leet_text += char #en el caso de que la frase introducida no sea alfanumérica porque tiene espacios en blanco o algún otro caracter se dejará tal cual ha sido introducido.
    return leet_text

frase = input("Escribe un texto para convertirlo a lenguaje hacker: ")
print(hacker_language(frase))

'''
Explicación del bucle for:

for char in text.lower(): crea un bucle que recorre cada carácter en el 
texto ingresado por el usuario después de convertirlo a minúsculas utilizando el método lower().
 Esto permite que la conversión a lenguaje hacker sea independiente de mayúsculas y minúsculas.
if char.isalnum(): verifica si el carácter es alfanumérico, es decir, 
si es una letra o un número. Esto se realiza utilizando el método isalnum(),
 que devuelve True si el carácter es alfanumérico y False en caso contrario.
leet_text += leet_alphabet.get(char, char) agrega al resultado leet_text la transformación del carácter
 a lenguaje hacker utilizando el diccionario leet_alphabet. 
 Si el carácter no está presente en el diccionario, se agrega tal cual utilizando char.
else: se ejecuta si el carácter no es alfanumérico, por ejemplo, 
si es un espacio en blanco o un carácter especial. En ese caso, el carácter se agrega tal cual a leet_text.
En resumen, el bucle for recorre cada carácter del texto ingresado por el usuario 
y realiza la transformación correspondiente a lenguaje hacker si es alfanumérico,
 o lo agrega sin cambios si no lo es.

'''

