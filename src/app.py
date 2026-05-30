from prestamosnny import PrestamosNNY

class App:
    
    def admin(self, main_class):
        log = False
        print("--- INICIO DE SESIÓN ---")
        usuario = input("Ingrese usuario: ")
        contrasena = input("Ingrese contraseña: ")
        
        try:              
            with open("usuarios.csv", "r", encoding="utf-8") as f:
                lineas = f.readlines()
                for linea in lineas[1:]:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(';')
                    if len(partes) >= 2:
                        if partes[0] == usuario and partes[1] == contrasena:
                            print("\nAcceso concedido.\n")
                            log = True
                            break
        except Exception as e:
            print(f"Error al verificar credenciales: {e}")
        
        if not log:
            print("Usuario o contraseña incorrectos.\n")
        else:
            while True:
                print("""Menú Principal:
1. Total de Prestamos Registrados
2. Total de Items Devueltos
3. Total de Ventas realizadas
4. Total Pago realizados
5. Lista de Amigos
6. Amigos con mayor y menor cantidad de prestamos""")
                opcion = input("Seleccione una opción (Enter para salir): ")
                print("\n")
                if opcion == "1":
                    main_class.listar_prestamos()
                    input("\n")
                elif opcion == "2":
                    main_class.listar_inventario(0)
                    print("    Total devoluciones: ", main_class.total_devoluciones)
                    input("\n")
                elif opcion == "3":
                    main_class.listar_inventario(2)
                    input("\n")
                elif opcion == "4":
                    main_class.total_pagos()
                    input("\n")
                elif opcion == "5":
                    main_class.listar_amigo()
                    input("\n")
                elif opcion == "6":
                    main_class.top_prestamos()
                    input("\n")
                elif not opcion or opcion == " " or opcion == "":
                    confirmacion = input("¿Está seguro que desea salir? (s/n): ")
                    if confirmacion.lower() == "s":
                        print("Saliendo del admin panel!")
                        return
                    else:
                        print("Continuando en el programa.")
                else:
                    print("Opción inválida, por favor seleccione una opción del 1 al 6.")
    
    
    def main(self):
        prestamos_nny = PrestamosNNY()
        while True:
            print("""
    ████  ████  █████  ████ █████  ███  █   █  ███   ████            █   █ █   █ █   █ 
    █   █ █   █ █     █       █   █   █ ██ ██ █   █ █                ██  █ ██  █  █ █  
    ████  ████  ████   ███    █   █████ █ █ █ █   █  ███     ████    █ █ █ █ █ █   █   
    █     █  █  █         █   █   █   █ █   █ █   █     █            █  ██ █  ██   █   
    █     █   █ █████ ████    █   █   █ █   █  ███  ████             █   █ █   █   █   \n""")
            print("""Menú Principal:
1. Registrar Amigo
2. Registrar Prestamo
3. Registrar Devolucion
4. Consular Items con mas de 30 dias
5. Consultar Articulos Prestados
6. Administrador""")
            opcion = input("Seleccione una opción (Enter para salir): ")
            print("\n")
            if opcion == "1":
                prestamos_nny.registrar_amigo()
                input("\n")
            elif opcion == "2":
                prestamos_nny.registrar_prestamo()
                input("\n")
            elif opcion == "3":
                prestamos_nny.eliminar_prestamos()
                input("\n")
            elif opcion == "4":
                prestamos_nny.verificar_prestamos_vencidos()
                input("\n")
            elif opcion == "5":
                prestamos_nny.listar_inventario(1)
                input("\n")
            elif opcion == "6":
                self.admin(prestamos_nny)
                input("\n")
            elif not opcion or opcion == " " or opcion == "":
                confirmacion = input("¿Está seguro que desea salir? (s/n): ")
                if confirmacion.lower() == "s":
                    # Auto-guardar al salir
                    prestamos_nny.exportar_datos()
                    print("Saliendo del programa. ¡Hasta luego!")
                    break
                else:
                    print("Continuando en el programa.")
            else:
                print("Opción inválida, por favor seleccione una opción del 1 al 6.")

app = App()
app.main()
