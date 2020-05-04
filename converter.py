import os
import sys
import fileinput

print("Grupo-1AN:")
print("Kevin Manfredy Axpuac Juárez - 15006597")
print("Antares: ")
def impHelp():
    print("  -baseIn <base de entrada>")
    print("          convert -baseOut 16 16")
    print("  -baseOut <base de salida>")
    print("          convert -baseOut 16 16")
    print("  -outFile <file name>")
    print("          convert -baseOut 16 16")
    print("  -file <file name>")
    print("          convert -baseOut 16 16")
    print("          **********************************************************")
    print("          Nombre del Proyecto: Cambiador de Base")
    print("          Información de Proyecto:")
    print("             Convierte un número de una base a otra.")
    print("                 Ejemplo: pasa un número de base 2 a base 10")
    print("                     conversor >> convert -baseOut 10 0b1100")
    print("                     resultado >> 12")
    print("          ***********************************************************")
    print("             Kevin Manfredy Axpuac Juárez, 15006597 , IME")
    print("             Ciencias de la Computación I, Universidad Galileo, 2020")

def error():
    print("resultado >> ERROR! Expresión no valida")
#Bandera baseOut
baseOut = False
baseOutDefault = 10
#Bandera baseIn
baseIn = False
baseInDefault = 10
#Bandere file
file = False
fileName = ''
#Bandera outFile
outFile = False
outFileName = ''
#Numero a Convertir
numberConvert = ''
#Prefijos
prefijos = {
    8 : '0',
    2 : '0b',
    16 : '0x',
    10 : ''
}


#Valida y convierte el número de una base a otra
def convert():
    from validateNumberIn import validateNumberIn
    from toBase10 import toBase10
    from toBase import toBase
    import re
    hex = re.compile('0x[0-9A-F]+')
    bi = re.compile('0b[0-1]+')
    dec = re.compile('[0-9]+')
    oct = re.compile('0[0-7]+')
    global numberConvert
    global baseInDefault
    if not baseIn:
        if len(numberConvert) > 1:
            if numberConvert[0:2] == '0x':
                baseInDefault = 16
            elif numberConvert[0:2] == '0b':
                baseInDefault = 2
            elif numberConvert[0:1] == '0':
                baseInDefault = 8
    else:
        if baseInDefault == 2:
            if not bi.match(numberConvert):
                print("resultado >> ERROR! numero mal formado")
                return
        elif baseInDefault == 16:
            if not hex.match(numberConvert):
                print("resultado >> ERROR! numero mal formado")
                return
        elif baseInDefault == 8:
            if not oct.match(numberConvert):
                print("resultado >> ERROR! numero mal formado")
                return

    if len(numberConvert) > 1:
        if numberConvert[0:2] == '0x':
            numberConvert = numberConvert[2: len(numberConvert)]
        elif numberConvert[0:2] == '0b':
            numberConvert = numberConvert[2: len(numberConvert)]
        elif numberConvert[0:1] == '0':
            numberConvert = numberConvert[1: len(numberConvert)]

    if file:
        if outFile:
            tempFile = open(fileName, 'r+')
            tmpFileOut = open(outFileName, 'w')
            for line in tempFile.readlines():
                palabra = line.split()
                switch = []
                for x in range(0, len(palabra)):
                    if not baseIn:
                        if bi.match(palabra[x]):
                            switch.append({'palabra': palabra[x], 'numero': palabra[x], 'baseOut': baseOutDefault,
                                           'baseIn': 2})
                        elif hex.match(palabra[x]):
                            switch.append({'palabra': palabra[x], 'numero': palabra[x], 'baseOut': baseOutDefault,
                                           'baseIn': 16})
                        elif dec.match(palabra[x]):
                            switch.append({'palabra': palabra[x], 'numero': palabra[x], 'baseOut': baseOutDefault,
                                           'baseIn': 10})
                        elif oct.match(palabra[x]):
                            switch.append({'palabra': palabra[x], 'numero': palabra[x], 'baseOut': baseOutDefault,
                                           'baseIn': 8})
                    else:
                        if baseInDefault == 10:
                            if dec.match(palabra[x]):
                                switch.append({'palabra': palabra[x], 'numero': palabra[x], 'baseOut': baseOutDefault,
                                               'baseIn': baseInDefault})
                        if baseInDefault == 8:
                            if oc.match(palabra[x]):
                                switch.append({'palabra': palabra[x], 'numero': palabra[x], 'baseOut': baseOutDefault,
                                               'baseIn': baseInDefault})
                        if baseInDefault == 16:
                            if hex.match(palabra[x]):
                                switch.append({'palabra': palabra[x], 'numero': palabra[x], 'baseOut': baseOutDefault,
                                               'baseIn': baseInDefault})
                        if baseInDefault == 2:
                            if bi.match(palabra[x]):
                                switch.append({'palabra': palabra[x], 'numero': palabra[x], 'baseOut': baseOutDefault,
                                               'baseIn': baseInDefault})
                pref = ''
                if baseOut:
                    if baseOutDefault == 2:
                        pref = prefijos[2]
                    elif baseOutDefault == 16:
                        pref = prefijos[16]
                    elif baseOutDefault == 8:
                        pref = prefijos[8]
                    else:
                        pref = prefijos[10]
                else:
                    pref = prefijos[10]
                for x in range(0, len(switch)):
                    line = line.replace(switch[x]['palabra'],pref + toBase(toBase10(switch[x]['numero'], switch[x]['baseIn']), baseOutDefault))
                tmpFileOut.write(line)
            tempFile.close()
            tmpFileOut.close()
        else:
            print("resultado >> ERROR! archivo de salida no indicado")
    elif validateNumberIn(numberConvert, baseInDefault):
        number = toBase(toBase10(numberConvert, baseInDefault), baseOutDefault)
        print("resultado >>", number)
    else:
        print("resultado >> ERROR! Número a convertir mal formado.")

def init():
    loop = 1
    while loop:
        command = input("conversor >> ").strip()
        if command == "":
            error()
            continue
        elif command == 'quit':
            print("Saliendo...")
            print("Gracias por usar nuestro convertidor.")
            break
        commands = command.split()
        if len(commands) > 1:
            if commands[0] != 'convert':
                error()
                continue
            if commands[1] == '-help':
                impHelp()
                continue

            global baseInDefault
            global baseOutDefault
            global fileName
            global outFileName
            global numberConvert
            global baseOut
            global baseIn
            global file
            global outFile

            baseOut = False
            baseIn = False
            file = False
            outFile = False
            baseInDefault = 10
            baseOutDefault = 10
            fileName = ''
            outFileName = ''
            numberConvert = ''
            tamano = len(commands) - 1
            x = 1
            while x <= tamano:
                if x == tamano:
                    numberConvert = commands[x]
                if '-' in commands[x]:
                    if commands[x] == '-baseIn':
                        x += 1
                        try:
                            try:
                                numero = int(commands[x])
                                if 1 < numero < 37:
                                    baseInDefault = numero
                                    baseIn = True
                                else:
                                    print("resultado >> ERROR! La bandera", commands[x - 1], "contiene una Base no válida")
                                    break
                            except ValueError:
                                print("resultado >> ERROR! La bandera", commands[x - 1], "no contiene valor ")
                                break
                        except IndexError:
                            print("resultado >> ERROR! La bandera", commands[x - 1], "no contiene valor ")
                            break
                    elif commands[x] == '-baseOut':
                        x += 1
                        try:
                            try:
                                numero = int(commands[x])
                                if 1 < numero < 37:
                                    baseOutDefault = numero
                                    baseOut = True
                                else:
                                    print("resultado >> ERROR! La bandera", commands[x - 1],
                                          "contiene una Base no válida")
                                    break

                            except ValueError:
                                print("resultado >> ERROR! La bandera", commands[x - 1], "no contiene valor ")

                                break
                        except IndexError:
                            print("resultado >> ERROR! La bandera", commands[x - 1], "no contiene valor ")
                            break
                    elif commands[x] == '-file':
                        x += 1
                        try:
                            if '-outFile' in commands[x]  or '-baseIn' in commands[x]  or '-baseOut' in commands[x]:
                                print("resultado >> ERROR! La bandera", commands[x - 1], "no contiene valor ")
                                break
                            fileName = commands[x]
                            file = True
                        except IndexError:
                            print("resultado >> ERROR! La bandera", commands[x - 1], "no contiene valor ")
                            break
                    elif commands[x] == '-outFile':
                        x += 1
                        try:
                            if '-file' in commands[x] or '-baseIn' in commands[x] or '-baseOut' in commands[x]:
                                print("resultado >> ERROR! La bandera", commands[x - 1], "no contiene valor ")
                                break
                            outFileName = commands[x]
                            outFile = True
                        except IndexError:
                            print("resultado >> ERROR! La bandera", commands[x - 1], "no contiene valor ")
                            break
                    else:
                        error()
                        break
                x += 1
            convert()
        else:
            if commands[0] == 'convert':
                print("resultado >> ERROR! Faltan argumentos")
            else:
                error()
init()



