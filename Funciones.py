import os,time
Pedidos = []
Precio_5kg =12500
Precio_15kg =25500
Comuna = ("Santiago, Colina, Pirque")
def menu():
    while True:
        os.system('cls')
        print("Menú")
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos.")
        print("3. Buscar pedido por RUT.")
        print("4. Imprimir hoja de ruta.")
        print("5. Salir del programa.")

        opc = int(input("Ingrese una opción: "))
        
        if opc==1:
            registrar_pedido()
        elif opc==2:
            lista_pedidos()
        elif opc==3:
            Buscar_rut()
        elif opc==4:
            pass
        elif opc==5:
            salir()



def registrar_pedido():
    print("REGISTRAR PEDIDO")
    rut = int(input("Ingrese su rut(sin puntos y guion): "))
    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese dirrección: ")
    comuna = input("Ingrese la comuna: ")
    Cil_5kg = int(input("Cantidad de cilindros de 5kg(si no necesita 0): "))
    Cil_15kg = int(input("Cantidad de cilindros de 15kg(si no necesita 0): "))

    total = (Precio_5kg*Cil_5kg)+(Precio_15kg*Cil_15kg)

    Pedido = {"Rut":rut,
              "Nombre":nombre,
              "Direccion":direccion,
              "Comuna":comuna,
              "Cil.5kg":Cil_5kg, 
              "Cil.15kg":Cil_15kg,
              "Total":total}

    Pedidos.append(Pedido)

def lista_pedidos():
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
    if not Pedidos:
        print("No hay pedidos en la lista!")
    else:
        rut_buscar = int(input("Ingrese Rut del pedido a buscar: "))
        if rut_buscar == Pedidos['Rut']:
            print("si esta en la lista")
        else:
            print("ERROR! El rut no esta en la lista")
        





def salir():
    print("Gracias, a dios")
    exit()


def Validar_rut():
    pass

def Validar_nombre():
    