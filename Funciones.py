import os,time,csv
Pedidos = []
Precio_5kg =12500
Precio_15kg =25500
Comunas = ("Santiago", "Colina", "Pirque")
def menu():
    while True:
        os.system('cls')
        print("Menú")
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos.")
        print("3. Buscar pedido por RUT.")
        print("4. Imprimir hoja de ruta.")
        print("5. Salir del programa.")

        opc = validar_opc()
        
        if opc==1:
            registrar_pedido()
        elif opc==2:
            lista_pedidos()
        elif opc==3:
            Buscar_rut()
        elif opc==4:
            imprimir_hoja()
        elif opc==5:
            salir()



def registrar_pedido():
    os.system('cls')
    print("REGISTRAR PEDIDO")
    rut = Validar_rut()
    nombre = Validar_nombre()
    direccion = Validar_direccion()
    comuna = Validar_comuna()
    Cil_5kg = validar_cil5()
    Cil_15kg = validar_cil15()

    total = (Precio_5kg*Cil_5kg)+(Precio_15kg*Cil_15kg)

    Pedido = {"Rut":rut,
              "Nombre":nombre,
              "Direccion":direccion,
              "Comuna":Comunas[comuna-1],
              "Cil.5kg":Cil_5kg, 
              "Cil.15kg":Cil_15kg,
              "Total":total}

    Pedidos.append(Pedido)
    print("AÑADIDO CON EXITO!")
    time.sleep(3)

def lista_pedidos():
    os.system('cls')
    print("LISTA DE PEDIDOS")
    if not Pedidos:
        print("No hay pedidos en la lista!")
        time.sleep(3)
    else:
        for pe in Pedidos:
            print(f"Rut: {pe['Rut']}, NOMBRE: {pe['Nombre']}, DIRECCIÓN: {pe['Direccion']}, COMUNA: {pe['Comuna']} CIL.5KG: {pe['Cil.5kg']}, CIL.15KG: {pe['Cil.15kg']}, TOTAL: {pe['Total']}")
            print("")
            time.sleep(3)

def Buscar_rut():
    os.system('cls')
    print("BUSCAR PEDIDO POR RUT")
    if not Pedidos:
        print("No hay pedidos en la lista!")
        time.sleep(3)
    else:
        rut_buscar = input("Ingrese Rut del pedido a buscar: ")
        if rut_buscar == ['Rut']:
            for pe in range(1):
                print(f"Rut: {pe['Rut']}, NOMBRE: {pe['Nombre']}, DIRECCIÓN: {pe['Direccion']}, COMUNA: {pe['Comuna']} CIL.5KG: {pe['Cil.5kg']}, CIL.15KG: {pe['Cil.15kg']}, TOTAL: {pe['Total']}")
                time.sleep(3)

        else:
            print("ERROR! El rut no esta en la lista")
            time.sleep(3)
        
def imprimir_hoja():
    os.system('cls')
    if not Pedidos:
        print("No hay pedidos en la lista!")
    else:
        print("IMPRIMIR HOJA DE RUTA")
        sector = int((input("Ingrese que sector se desea imprimir(1:Santiago, 2:Colina, 3:Pirque): ")))
    
        nombre_archivo = input("Ingrese nombre del archivo: ")+".csv"
        with open(nombre_archivo,"w",newline="") as archivo:
            escritor = csv.DictWriter(archivo,["Rut","Nombre","Direccion","Comuna","Cil.5kg","Cil.15kg", "Total"])
            escritor.writerows(Pedidos)
            print("ARCHIVO CREADO!")
            time.sleep(3)
        


def salir():
    print("Gracias, a dios")
    exit()


def Validar_rut():
    while True:
        try:
            ru = int(input("Ingrese su rut(sin puntos ni guion verificador): "))
            if ru>0:
                return ru

        except:
            print("ERROR! Debe ingresar un número entero!")

def Validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else: 
            print("ERROR! Debe ingresar su nombre sin espacios y mayor a 3 letras!")

def Validar_direccion():
    while True:
        dir = input("Ingrese dirección: ")
        if len(dir.strip())>=3 and dir.isalpha():
            return dir
        else: 
            print("ERROR! Debe ingresar una direccion mayor 3 letras(sin espacio)")

def Validar_comuna():
    while True:
        try:
            com = int(input("Ingrese comuna(1:Santiago, 2:Colina, 3:Pirque): "))
            if com in (1,2,3):
                return com
            else: 
                print("ERROR! Debe ingresar un número entero entre el 1, 2, 3!")
        except:
            print("ERROR! Debe ingresar un número entero de la comuna")

def validar_cil5():
    while True:
        try:
            cil = int(input("Cantidad de cilindros de 5kg(si no necesita 0): "))
            if cil>= 0:
                return cil
            else:
                print("Debe ingresar un número mayor o igual a 0!")
        except:
            print("ERROR! Debe ingresar un número entero!")

def validar_cil15():
    while True:
        try:
            cil = int(input("Cantidad de cilindros de 15kg(si no necesita 0): "))
            if cil>= 0:
                return cil
            else:
                print("Debe ingresar un número mayor o igual a 0!")
        except:
            print("ERROR! Debe ingresar un número entero!")

def validar_opc():
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR! Debe ingrer un número entre el 1 al 5!")
        except:
            print("ERROR! debe ingresar un número entero!")



