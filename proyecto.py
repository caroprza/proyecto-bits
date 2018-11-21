import csv
from statistics import mode
def idk():
    try:
        archivo=open("data.csv", "r")
    except:
        print("No se puede abrir el archivo o no existe.")
    else:
        matriz=[]
        l=0
        for linea in archivo:
            if l>0 and l<1658:
                lin=linea.rstrip()
                list=lin.split(";")
                matriz.append(list)
            l+=1
        return matriz
datos=idk()

def promedio(datos,hora):
    suma=0
    linea=0
    num=0
    for lista in datos:
        for c in lista:
            if hora in c:
                bits=float(datos[linea][1])
                suma+=bits
                num+=1
        linea+=1
    prom=suma/num
    return prom


def hora_menor(datos,dia):
    linea=0
    list=[]
    for lista in datos:
        for c in lista:
            if dia in c:
                list.append(float(datos[linea][1]))
        linea+=1
    linea=0
    m=str(min(list))
    for lista in datos:
        if m in lista:
            print(datos[linea][0])
        linea+=1


def hora_dia_menor(datos):
    matriz=[]
    list=[]
    linea=0
    for lista in datos:
        if linea==0:
            try:
                list.append(int(datos[linea][1]))
            except:
                list.append(float(datos[linea][1]))
        elif linea==(len(datos)-1):
            try:
                list.append(int(datos[linea][1]))
            except:
                list.append(float(datos[linea][1]))
            matriz.append(list)
        else:
            if datos[linea][0][:11]!=datos[linea-1][0][:11]:
                matriz.append(list)
                list=[]
            try:
                list.append(int(datos[linea][1]))
            except:
                list.append(float(datos[linea][1]))
        linea+=1
    archivo=open("reporte.txt", "w+", encoding="UTF-8")
    archivo.write("Reporte de horas con menor tráfico\n")
    list=[]
    for lista in matriz:
        linea=0
        m=str(min(lista))
        for l in datos:
            if m in l:
                print(datos[linea][0])
                archivo=open("reporte.txt", "a", encoding="UTF-8")
                archivo.write(str(l))
                archivo.write("\n")
                list.append(int(datos[linea][0][12:14]))
            linea+=1
    archivo.write("La hora con mayor frecuencia de menor tráfico es ")
    archivo.write(str(mode(list)))
    archivo.write(":30")
    archivo.close()


def dia_menor(datos):
    list=[]
    linea=0
    suma=0
    for lista in datos:
        if linea==0:
            hr=9
            if hr>=9 and hr<=21:
                bits=float(datos[linea][1])
                suma+=bits
        elif linea==(len(datos)-1):
            if hr>=9 and hr<=21:
                bits=float(datos[linea][1])
                suma+=bits
                list.append(suma)
        else:
            if datos[linea][0][:11]!=datos[linea-1][0][:11]:
                list.append(suma)
                suma=0
                hr=0
            if hr>=9 and hr<=21:
                bits=float(datos[linea][1])
                suma+=bits
        hr+=1
        linea+=1
    print(list)
    m=str(min(list))
    dia=0
    for i in list:
        if m in str(i):
            break
        dia+=1
    print(datos[dia*24][0][1:11])


def suma(datos,inicio,final):
    start=0
    end=0
    linea=0
    suma=0
    for lista in datos:
        if inicio in lista[0]:
            start=1
        if start==1 and end!=1:
            bits=float(datos[linea][1])
            suma+=bits
        if final in lista[0]:
            end=1
        linea+=1
    print(suma)


def mayor_flujo(datos,inicio,final):
    list=[]
    start=0
    end=0
    linea=0
    for lista in datos:
        if inicio in lista[0]:
            start=1
        if start==1 and end!=1:
            list.append(float(datos[linea][1]))
        if final in lista[0]:
            end=1
        linea+=1
    linea=0
    m=str(max(list))
    for lista in datos:
        if m in lista[1]:
            print(datos[linea][0])
        linea+=1


def menu():
    print("Elige una opción")
    print("1. Promedio de tráfico en una hora en particular")
    print("2. La hora con menor tráfico")
    print("3. La hora con menor tráfico")
    print("4. Día con menor tráfico")
    print("5. Suma de bits en un periodo determinado")
    print("6. La hora con mayor flujo de bits en un periodo determinado")
    print("7. Salir")
    opc=input("¿Qué opción deseas hacer?")
    return opc
opc="0"
while opc!="7":
    opc=menu()
    if opc=="1":
        hora=input("¿Qué hora buscas? (Dar en formato hora:min)")
        print(promedio(datos,hora))
        input("Presiona enter para continuar")
    elif opc=="2":
        dia=input("¿Qué día buscas? (Dar en formato mes-día)")
        hora_menor(datos,dia)
        input("Presiona enter para continuar")
    elif opc=="3":
        hora_dia_menor(datos)
        input("Presiona enter para continuar")
    elif opc=="4":
        dia_menor(datos)
        input("Presiona enter para continuar")
    elif opc=="5":
        inicio=input("¿Cuál es la primera fecha? (Dar en formato mes-día hora:min)")
        final=input("¿Cuál es la segunda fecha?")
        suma(datos,inicio,final)
        input("Presiona enter para continuar")
    elif opc=="6":
        inicio=input("¿Cuál es la primera fecha? (Dar en formato mes-día hora:min)")
        final=input("¿Cuál es la segunda fecha?")
        mayor_flujo(datos,inicio,final)
        input("Presiona enter para continuar")
    else:
        print("Ingrese una opción válida")
        input("Presiona enter para continuar")
