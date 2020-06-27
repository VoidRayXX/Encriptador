from random import randint

#ejercicio 3 del primer certamen del segundo semestre 2015 USM CC (progra.usm.cl)
#***La regla de desencriptación es la siguiente: la palabra desencriptada se obtiene recorriendo 
#desde el final de la palabra hasta el comienzo, considerando solo las letras en ubicaciones impares. Empezando desde la ultima letra. ***
#///La regla de desencriptacion de la hora es la siguiente: sumar cada dígito anterior al carácter ':' y calcular el resto de la division entre
#esa suma y 24. Luego, lo mismo con los dígitos despues del carácter ':', pero la division es entre la suma de esos dígitos y 60.///
#palabras de ejemplo: aczaarltp (plaza), axruatgrrreov (vergara), 776199:68556 (15:30)
#la palabra, desencriptada, clave que acaba el programa es acun (npuecea)
#nota: lo mejoré para que si escribo 'fin' deje de funcionar, en ambas opciones

def codigo_palabra(codigo):
    i = -1
    msj = ''
    while i >= -len(codigo):
        if i%2 != 0:
            msj += codigo[i]
        i -= 1
    return msj

#dig1 son los números que vienen antes del ':' (horas), y dig2 los que vienen después (minutos). Ambos son tratados como strings
#Flag nos indica si ya se llegó a ':'
#ac1 y ac2 son la suma de los valores de dig1 y dig2 respectivamente
#hh y mm, horas y minutos, son el resultado de aplicar la desencriptacion a ac1 y ac2

def codigo_hora(hora):
    dig1 = ''
    dig2 = ''
    ac1 = 0
    ac2 = 0
    Flag = False
    for x in hora:
        if Flag:
            dig2 += x
        if x != ':' and Flag == False:
            dig1 += x
        else:
            Flag = True
    for h in dig1:
        ac1 += int(h)
    for m in dig2:
        ac2 += int(m)
    hh = str(ac1 % 24)
    mm = str(ac2 % 60)
    hora_final = hh+':'+mm
    return hora_final
 
 #ciclo permite el funcionamiento repetitivo del programa
 #msj va acumulando el mensaje encriptado/desencriptado

ciclo = True

while ciclo:
    print("1)Encriptar mensaje")
    print("2)Desencriptar mensaje")
    print("3)Salir del programa")
    eleccion = int(input("Seleccione una opción: "))
    while eleccion != 1 and eleccion != 2 and eleccion != 3:
        print('Opción inválida')
        eleccion = int(input("Seleccione una opción: "))
    msj = ''

#primero se da vuelta la palabra, lo que se gurda en reverse
#luego se trabaja con una lista hecha de los componentes de reverse
#k es el indice de cada caracter, y si este es impar se le añaden caracteres aleatorios a la frase
#aux va acumulando los valores que tendrá que el mensaje encriptado
#dependiendo de si la cantidad de caracteres de aux es par o no, se usa rebanador

    if eleccion == 1:
        while msj != 'fin':
            msj = input("Ingrese el mensaje a encriptar: ")
            if msj != 'fin':
                i = -1
                reverse = ''

                while i >= -len(msj):
                    reverse += msj[i]
                    i -= 1

                lista = list(reverse)
                aux = ''
                k = 0

                for elemento in lista:
                    if k%2 != 0 and lista[k] != len(lista)-2:
                        aux += chr(randint(59,94)) + lista[k] + chr(randint(59,94))
                    else:
                        aux += lista[k]
                    k += 1

                if len(aux)%2 == 0:
                    encriptado = aux[:(len(aux)-1)]
                else:
                    encriptado = aux[:len(aux)]
                print(encriptado)

#seguir permite el funcionamiento del ciclo de recolectar los mensajes a desencriptar 
#codigo solicita el mensaje a desencriptar

    elif eleccion == 2:
        seguir = True

        while seguir:
            codigo = input("Ingrese código: ")
            if ':' in codigo:
                msj += codigo_hora(codigo) + ' '
            else:
                if codigo_palabra(codigo) == 'acun' or codigo == 'fin':
                    seguir = False
                else:
                    msj += codigo_palabra(codigo) + ' '

        print("El mensaje es: ", msj)

    else:
        ciclo = False