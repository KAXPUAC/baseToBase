#Pasa un numero decimal a otra base
def toBase(numero: int, base: int):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if numero < 0:
        numero = numero * -1
    result = ''
    while numero > 0:
        numero, residuo = numero//base, numero%base
        result = chars[residuo] + result
    return result