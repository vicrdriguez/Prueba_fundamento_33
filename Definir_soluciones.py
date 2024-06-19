
Tipo_paquete = ['grande','mediano','pequeño']
SECTOR = ['centro','sur','norte']


# Funcion Registrar pedidos
def Registrar_pedido(Lista_pedidos):


    NombreApellido = input("Ingrese su nombre y su apellido pofavor: ")
    Direccion = input("sector la direccion del pedido porfavor: ")
    Sector = input(f"digite el sector de la ciudad porfavor {SECTOR}: ").lower()
    DetallePedido = input(f"Ingrese el detalle del pedido {Tipo_paquete}: ").lower()

    while DetallePedido not in Tipo_paquete:
        print(f"el detalle que digito no es valido porfavor ingresar de nuevo {Tipo_paquete}: \n")
        DetallePedido = input(f"Ingrese el detalle del pedido {Tipo_paquete}: ").lower()

    while Sector not in SECTOR:
        print(f"el sector que digito no es valido porfavor ingresar de nuevo {SECTOR}: ")
        Sector = input(f"digite el sector de la ciudad porfavor {SECTOR}: ").lower()

    Lista_pedidos.append({
        'nombre':NombreApellido,
        'direccion':Direccion,
        'sector':Sector,
        'detalle':DetallePedido
    })


# Funcion Listar Pedidos
def Listar_pedidos(Lista_pedidos):
    for Pedidos in Lista_pedidos:
        print(Pedidos)

# Funcion Imprimir Lista con pedidos 
def imprimir_Pedido(Lista_pedidos):

    SectorDeseado = input("digite el sector  de los pedidos que quiera imrpimir porfavor: ").lower()

    while SectorDeseado not in SECTOR:
        print(f"Ese sector no existe porfavor escribe de nuevo, los sectores son {SECTOR}")
        SectorDeseado = input("digite el sector  de los pedidos que quiera imrpimir porfavor: ").lower()

    if SectorDeseado == "sur":
        Sector_sur = []
        archivo = f"PlantillaSur{'PlantillaSur'}.txt"
        for paqueteS in Lista_pedidos:
            if paqueteS['sector'] == "sur":
                Sector_sur.append(paqueteS)

    elif SectorDeseado == "centro":
        Sector_centro = []
        archivo = f"PlantillaCentro{'PlantillaCentro'}.txt"
        for paqueteC in Lista_pedidos:
            if paqueteC['sector'] == "centro":
                Sector_centro.append(paqueteC)

    elif SectorDeseado == "norte":
        Sector_norte = []
        archivo = f"PlantillaNorte{'PlantillaNorte'}.txt"
        for paqueteN in Lista_pedidos:
            if paqueteN['sector'] == "norte":
                Sector_norte.append(paqueteN)


    



    # No pude hacer que no aparescan las demas planillas  si solo queria seleccionar la de un sector especifico , pero si se guarda los datos  

    with open(archivo,'w') as archivo_txt:

        if archivo == f"PlantillaSur{'PlantillaSur'}.txt":
            for dato in Sector_sur:
                archivo_txt.write(f"NOMBRE Y APELLIDO: {dato['nombre' ]}")
                archivo_txt.write(f"DIRECCION: {dato['direccion']} ")
                archivo_txt.write(f"SECTOR: {dato['sector']} ")
                archivo_txt.write(f"DETALLE DEL  PEDIDO: {dato['detalle']} \n")
        
        elif archivo == f"PlantillaCentro{'PlantillaCentro'}.txt":
            for dato in Sector_centro:
                archivo_txt.write(f"NOMBRE Y APELLIDO: {dato['nombre' ]}")
                archivo_txt.write(f"DIRECCION: {dato['direccion']} ")
                archivo_txt.write(f"SECTOR: {dato['sector']} ")
                archivo_txt.write(f"DETALLE DEL  PEDIDO: {dato['detalle']} \n")
        
        elif archivo == f"PlantillaNorte{'PlantillaNorte'}.txt":
            for dato in Sector_norte:
                archivo_txt.write(f"NOMBRE Y APELLIDO: {dato['nombre' ]}")
                archivo_txt.write(f"DIRECCION: {dato['direccion']} ")
                archivo_txt.write(f"SECTOR: {dato['sector']} ")
                archivo_txt.write(f"DETALLE DEL  PEDIDO: {dato['detalle']} \n")







    










    

        




