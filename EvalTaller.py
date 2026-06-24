Lista=[]



def numcheck(num:str)->int:
    while True:
        try:
            numero=int(input(num))
            if numero<0:
                print("Numero no puede ser menor a cero")
            else:
                return numero
        except Exception:
            print("Error numerico")

def typecheck(typ:str):
    while True:
        try:
            texto=input(typ)
            if len(texto)==0:
                print("Mensaje vacio")
            elif texto.isspace():
                print("Mensaje no puede estar vacio")
            else:
                return texto
        except Exception:
            print("Error al recibir texto")

def floatcheck(dec:str)->float:
    while True:
        try:
            valor=float(input(dec))
            if valor==0:
                print("Valor no puede ser cero")
            elif valor<0:
                print("Precio no puede ser menor a cero")
            else:
                return valor
        except Exception:
            print("Error decimal")

def listadd(nombre:str,stock:int,precio:int,disp):
    inventario={
                "Nombre":nombre,
                "Stock":stock,
                "Precio":precio,
                "Disponibilidad":disp

                }
    Lista.append(inventario)
    print("Inventario modificado exitosamente")

def listsearch(nombre:str):
    queue=0
    for i in Lista:
        if i["nombre"]==nombre:
            return queue
        queue +=1

def listcheck():
    for i in Lista:
        print(f"Nombre: {i.get("nombre")}\nStock: {i.get("stock")}\nPrecio: {i.get("precio")}\nDisponible: {i.get("disponibilidad")}")

disp="NO DISPONIBLE"
def menu():
    while True:
        print(f"========== MENÚ PRINCIPAL ========== \n 1. Agregar producto \n 2. Buscar producto \n 3. Eliminar producto")
        print(" 4. Actualizar disponibilidad \n 5. Mostrar productos \n 6. Salir \n =====================================")
        opcion=numcheck("1-2-3-4-5-6: ")
        if opcion==1:
            nombre=typecheck("Ingrese nombre del producto: ")
            stock=numcheck("Ingrese stock del producto: ")
            precio=floatcheck("Ingrese precio del producto: ")
            
            listadd(nombre,stock,precio,disp)
        if opcion==2:
            nombre=typecheck("Nombre del producto a buscar: ")
            item=listsearch(nombre)
            if item != None:
                print(Lista[item])
            else:
                print("Objeto no encontrado")
        if opcion==5:
            listcheck()
        if opcion==6:
            print("Saliendo")
            break
menu()

print(Lista)