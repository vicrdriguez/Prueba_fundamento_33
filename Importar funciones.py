import Definir_soluciones as Fun

Lista_pedidos = []
while True:
    try:
        print("-------------------")
        print("----PaquExpress----")
        print("-------------------")
        print("1. Reistrar pedidos ")
        print("2. Listar pedidos ")
        print("3. Imprimir pedidos ")
        print("4. Salir del programa ")
        opcion = int(input("Ingrese una opcion pofavor: "))

        if opcion == 1:
            print("-------------------")
            print("----Reigstrar pedidos----")
            print("-------------------")
            Fun.Registrar_pedido(Lista_pedidos)
        elif opcion == 2:
            print("-------------------")
            print("----Listar pedidos----")
            print("-------------------")
            Fun.Listar_pedidos(Lista_pedidos)
        elif opcion == 3:
            print("-------------------")
            print("----Imprimir pedidos----")
            print("-------------------")
            Fun.imprimir_Pedido(Lista_pedidos)
        elif opcion == 4:
            print("Saliendo . . ..")
            break
        else:
            print("Ingresa una opcion valida porfavor")
    except ValueError:
        print("Error, ingrese una opcion valida porfavor")










