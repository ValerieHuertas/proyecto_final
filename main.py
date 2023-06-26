
import Login
import diccionarios
while True:
    print("\n*****SOFTWARE VARIEDADES MALU*****\n")
    print("\n*****MENU*****")
    print("Inventario = 1")
    print("Ingresos   = 2")
    print("Arreglos   = 3")
    print("Clientes   = 4")
    print("Encargos   = 5")
    print("Salir      = 6")
    main_seleccion = int(input("por favor ingresa la opcion seleccionada: "))
    if main_seleccion == 1:
        import inventario
    elif main_seleccion == 2:
        import ingresos
    elif main_seleccion ==3:
        import arreglos
    elif main_seleccion == 4:
        import clientes
    elif main_seleccion == 5:
        import encargos
    elif main_seleccion == 6:
        exit()
    else:
        print("opcion seleccionada incorrecta.")