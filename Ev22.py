import csv
from collections import namedtuple
datos =("fecha","Descripcion", "Cantidad", "Precio", "total")


switch = True
diccionario_ventas={}
lista_ventas=[]
Detalle = namedtuple("venta", ("fecha","Descripcion", "Cantidad", "Precio", "total"))
total2= 0
i=0


while switch:

    print("--------------MENU REGISTRO DE VENTAS-----------")
    print("¿Qué desea realizar?")
    print("1: Registrar una venta ")
    print("2: Consultar una venta por folio")
    print("3: Genererar Reporte")
    print("4: Salir del programa")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        masasrticulos = True
        

        folio = int(input("Ingrese su folio: "))
        if not folio in diccionario_ventas.keys():
            fecha = input("Ingrese la fecha: ")
            while masasrticulos:
            #folio2=input("ingresa el ID del articulo: ")
                descripcion=input("Ingrese la descripcion: ")
                cantidad=int(input("Ingrese la cantidad: "))
                precio=int(input("Ingrese el precio: "))
                resp=str(input("¿Desea agregar otro producto? Si/No: ")).upper()
                if resp != "SI":
                    masasrticulos=False
        
                iva=(precio*cantidad)*0.16
                total=(precio*cantidad)+iva
                total2= total2 + total
                Venta_Registrada=Detalle(fecha,descripcion,cantidad,precio,total)
                lista_ventas.append(Venta_Registrada)
                print("El total con iva incluido es: ",total2) 
        
        else:

            print("Esta venta ya está registrada, intente de nuevo. ")
        diccionario_ventas[folio] = lista_ventas

    elif opcion == "2":
        clave_buscar = int(input("Ingresa la clave de la compra que realizaste: "))
        if clave_buscar in diccionario_ventas.keys():
            print("Los datos de la venta son: [FECHA / DESCRIPCION / CANTIDAD / PRECIO / TOTAL]")
            print(diccionario_ventas[clave_buscar])
            print("")
            print("Regresaremos al Menu Principal")
            print("")
        else:
            print("Esa clave no esta registrada")

    elif opcion == "3":
        fecha_reporte = input("Ingrese La Fecha (dd/mm/aaaa): \n")
        print("Tu registro se generara")
        with open("Reportesobrevta.csv","w",newline="") as archivo:
            editor_csv = csv.writer(archivo)
            editor_csv.writerow(datos)
            editor_csv.writerows(lista_ventas)

    elif opcion == "4":

        print("Saldrás del sistema!")
        
        switch = False
        
    else:

        print("Esa opción no es válida")