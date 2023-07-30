import os

def iniciar():
    while True:
        os.system('clear') # cls en Windows

        print("========================")
        print("  BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Buscar cliente      ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Cerrar el Manager   ")
        print("========================")

        opcion = input("> ")
        os.system('clear') # cls en Windows

        if opcion == '1':
            print("Listando los clientes...\n")
        elif opcion == '2':
            print("Buscando un cliente...\n")
        elif opcion == '3':
            print("Añadiendo un cliente...\n")
        elif opcion == '4':
            print("Modificando un cliente...\n")
        elif opcion == '5':
            print("Borrando un cliente...\n")
        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")