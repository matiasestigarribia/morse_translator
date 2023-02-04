"""
traductor de cualquier cosa a codigo morse

input de frase a traducir

recorro todos los elementos de la frase, 
matcheo elemento y recupero valor de un diccionario con como seria el caracter en codigo morse para cada elemento, 
retorno la suma de todos esos elementos en una lista

"""
print("bienvenido al traductor a codigo morse")

diccionario_valores_traduccion = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
}
frase_traducida = []
# def traducir (frase_a_traducir):
frase_a_traducir = input("Por favor, ingrese frase a traducir: ")
"""for x in frase_a_traducir:
    for llave, valor in diccionario_valores_traduccion.items():
        if llave == x:
            frase_traducida.append(valor)
print(frase_traducida)
"""

"""def reproducir_frase(frase_traducida):
    for x in frase_traducida:
        for y in x:
            if y == '.':pass
                #play short sound
            else:
                #play long sound
"""


def traducir(frase_a_traducir):
    frase_a_traducir = input("Por favor, ingrese frase a traducir: ")
    for x in frase_a_traducir:
        for llave, valor in diccionario_valores_traduccion.items():
            if llave == x:
                frase_traducida.append(valor)
        return frase_traducida


print("esta esta saliendo de la funcion " + str(frase_traducida))

traducir("bcaa")
