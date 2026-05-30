import os
from datetime import datetime, timedelta
from utilidades import Utilidades
from prestamo import Prestamo
from cliente import Cliente
from objeto import Objeto

class PrestamosNNY:
    def __init__ (self):
        self.clientes = []
        self.inventario = []
        self.contador_id_inventario = 0
        self.prestamos = []
        self.contador_id_prestamos = 0
        self.total_devoluciones = 0
        self.dias_prestamo_definidos = [5, 10, 15, 30]
        self.categorias = {
1: ("Videojuegos", "VID"),
2: ("Libros", "LIB"),
3: ("Música y video", "MUV"),
4: ("Herramientas", "HER"),
5: ("Dinero", "DIN"),
6: ("Misceláneo y varios", "MIV")
}
        self.util = Utilidades()
        self.importar_datos()

    def importar_datos(self):
        # Cargar clientes
        print("Importando datos...")
        if os.path.exists("clientes.csv"):
            try:
                with open("clientes.csv", "r", encoding="utf-8") as f:
                    lineas = f.readlines()
                    if len(lineas) > 1:
                        for linea in lineas[1:]:
                            linea = linea.strip()
                            if not linea: continue
                            sep = ';' if ';' in linea else ','
                            partes = linea.split(sep)
                            if len(partes) >= 5:
                                doc, nom, ape, cor, tpd = partes[0], partes[1], partes[2], partes[3], int(partes[4])
                                if not any(c.get_documento() == doc for c in self.clientes): # Evitar duplicados
                                    self.clientes.append(Cliente(nom, ape, doc, cor, tpd))
            except Exception as e:
                print(f"Error al importar clientes: {e}")
        else:
            print("No se encontró el archivo clientes.csv. Iniciando con lista de clientes vacía.")

        # Cargar objetos y préstamos
        if os.path.exists("objetos.csv"):
            try:
                with open("objetos.csv", "r", encoding="utf-8") as f:
                    lineas = f.readlines()
                    if len(lineas) > 1:
                        max_id_obj, max_id_pre = 0, 0
                        for linea in lineas[1:]:
                            linea = linea.strip()
                            if not linea: continue
                            sep = ';' if ';' in linea else ','
                            partes = linea.split(sep)
                            if len(partes) >= 4:
                                id_obj = partes[0].strip()
                                nom_obj, pre_obj = partes[1], int(float(partes[2]))
                                estado = int(partes[3].strip().lower())
                                
                                prefijo = id_obj.split('-')[0] if '-' in id_obj else None
                                id_categoria = next((k for k, v in self.categorias.items() if v[1] == prefijo), 6)

                                nuevo_obj = Objeto(id_obj, nom_obj, pre_obj, id_categoria)
                                nuevo_obj.set_estado(estado)
                                self.inventario.append(nuevo_obj)
                                
                                if '-' in id_obj and id_obj.split('-')[1].isdigit():
                                    num_id = int(id_obj.split('-')[1])
                                    if num_id > max_id_obj: max_id_obj = num_id

                                if estado == 1 and len(partes) >= 8:
                                    id_pre, doc_cliente, fecha_str = int(partes[4]), partes[5], partes[6]
                                    vencido = (partes[7].strip().lower() == 'true')

                                    amigo = next((c for c in self.clientes if c.get_documento() == doc_cliente), None)
                                    if amigo:
                                        fecha_venc = datetime.strptime(fecha_str, "%Y-%m-%d").date()
                                        nuevo_prestamo = Prestamo(id_pre, amigo, nuevo_obj, fecha_venc)
                                        nuevo_prestamo.set_vencido(vencido)
                                        self.prestamos.append(nuevo_prestamo)
                                        if id_pre > max_id_pre: max_id_pre = id_pre
                        
                        self.contador_id_inventario = max_id_obj
                        self.contador_id_prestamos = max_id_pre
            except Exception as e:
                print(f"Error al importar objetos y prestamos: {e}")
        else:
            print("No se encontró el archivo objetos.csv. Iniciando con inventario y préstamos vacíos.")

    def exportar_datos(self):
        try:
            with open("clientes.csv", "w", encoding="utf-8") as f:
                f.write("documento;nombre;apellido;correo;tpd\n")
                for c in self.clientes:
                    f.write(f"{c.get_documento()};{c.get_nombre()};{c.get_apellido()};{c.get_correo()};{c.get_tpd()}\n")

            with open("objetos.csv", "w", encoding="utf-8") as f:
                f.write("id_objeto;nombre;precio;estado;id_prestamo;doc_cliente;fecha_vencimiento;vencido\n")
                for obj in self.inventario:
                    prestamo = next((p for p in self.prestamos if p.get_objeto() == obj), None)
                    if prestamo:
                        doc = prestamo.get_amigo().get_documento()
                        fecha_str = prestamo.get_fecha().strftime('%Y-%m-%d')
                        f.write(f"{obj.get_ID()};{obj.get_nombre()};{obj.get_precio()};{obj.get_estado()};{prestamo.get_ID()};{doc};{fecha_str};{prestamo.get_vencido()}\n")
                    else:
                        f.write(f"{obj.get_ID()};{obj.get_nombre()};{obj.get_precio()};{obj.get_estado()};;;;\n")
            print("Datos exportados exitosamente a clientes.csv y objetos.csv")
        except Exception as e:
            print(f"Error al exportar los datos: {e}")
    
    def registrar_amigo(self):
        u = self.util
        while True:
            nombre = input("Ingrese el nombre del amigo: ")
            if u.texto(nombre):
                break
            else:
                print("    - Error: nombre invalido (mínimo 3 caracteres, sin espacios ni números)")
        
        while True:
            apellido = input("Ingrese el apellido del amigo: ")
            if u.texto(apellido):
                break
            else:
                print("    - Error: apellido invalido (mínimo 3 caracteres, sin espacios ni números)")
        
        while True:
            documento = input("Ingrese el documento del amigo: ")
            if u.documento(documento):
                break
            else:
                print("    - Error: documento invalido (3-15 dígitos, sin espacios ni letras)")
        
        while True:
            correo = input("Ingrese el correo del amigo: ")
            if u.correo(correo):
                break
            else:
                print("    - Error: correo invalido (sin espacios, un '@', termina con '.com')")

        while True:
            print("""Tiempos de Prestamos Definidos (Dias):
    1) 5
    2) 10
    3) 15
    4) 30""")
            opcion = input("Seleccione el tiempo de préstamo: ")
            if opcion in ['1', '2', '3', '4']:
                tpd = self.dias_prestamo_definidos[int(opcion) - 1]
                break
            else:
                print("    - Error: opción inválida, seleccione una opción del 1 al 4")
        
        if len(self.clientes) > 0:
            for cliente in self.clientes:
                if cliente.get_documento() == documento:
                    print("    - Error: ya existe un amigo registrado con ese documento.")
                    return
        
        objeto_cliente = Cliente(nombre.lower(), apellido.lower(), documento, correo, tpd)
        self.clientes.append(objeto_cliente)
        print("    Amigo registrado exitosamente.")
        print(f"    - {objeto_cliente.info()}")

    def listar_amigo(self):
        if not self.clientes:
            print("No hay amigos registrados.")
            return None
        total = 0
        print("Lista de Amigos:")
        for idx, amigo in enumerate(self.clientes, start=1):
            print(f"{idx}. {amigo.info()}")
            total += 1
        print(f"    Total: {total}")

    def registrar_inventario(self):
        u = self.util
        while True:
            nombre = input("Ingrese el nombre del objeto: ")
            if nombre and len(nombre.strip()) >= 3 and len(nombre) >= 3:
                break
            else:
                print("    - Error: el nombre del objeto no puede estar vacío y debe tener al menos 3 caracteres.")
        
        while True:
            precio_input = input("Ingrese el precio del objeto: ")
            precio = u.num(precio_input)
            if precio:
                break
            else:
                print("    - Error: precio inválido (debe ser un número, entero positivo)")
        
        for key, value in self.categorias.items():
            print(f"    {key}. {value[0]}")
        while True:
            opcion = input("Seleccione el tiempo de préstamo: ")
            if opcion in ['1', '2', '3', '4', '5', '6']:
                id_categoria = int(opcion)
                categoria_elegida = self.categorias[id_categoria][0]
                print(f"    - Categoría seleccionada: {categoria_elegida}")
                break
            else:
                print("    - Error: opción inválida, seleccione una opción del 1 al 6")
        
        prefijo = self.categorias[id_categoria][1]
        nuevo_id = f"{prefijo}-{self.contador_id_inventario + 1:03}"
        objeto_inventario = Objeto(nuevo_id, nombre.lower(), precio, id_categoria)
        self.inventario.append(objeto_inventario)
        self.contador_id_inventario += 1
        print("Objeto registrado en inventario exitosamente.")
        print(f"    - {objeto_inventario.info()}")

    def listar_inventario(self, estado = None):
        if not self.inventario:
            print("No hay objetos en el inventario.")
            return
        
        estado_map = {0: "Disponibles", 1: "Prestados", 2: "Vendidos"}
        
        if estado in estado_map:
            print(f"Inventario de objetos {estado_map[estado]}:")
        else:
            print("Inventario de objetos:")

        total = 0
        for idx, obj in enumerate(self.inventario, start=1):
            if estado is None:
                print(f"{idx}. {obj.info()} ({estado_map.get(obj.get_estado(), 'Desconocido')})")
                total += 1
            elif obj.get_estado() == estado:
                print(f"{idx}. {obj.info()}")
                total += 1

        if total == 0:
            print("No hay objetos para mostrar.")
        else:
            print(f"    Total: {total}")
    
    def total_pagos(self):
        print("======= REPORTE DE PAGOS (OBJETOS VENDIDOS) =======")
        suma_precios = 0
        suma_intereses = 0
        suma_totales = 0
        
        for obj in self.inventario:
            if obj.get_estado() == 2:
                precio = obj.get_precio()
                interes = int(precio * 0.23)
                total_obj = precio + interes
                
                print(f"- {obj.get_ID()}: {obj.get_nombre()} | Precio: ${precio} | Interés (23%): ${interes} | Total: ${total_obj}")
                
                suma_precios += precio
                suma_intereses += interes
                suma_totales += total_obj
            
        if suma_totales == 0:
            print("No hay pagos de objetos vendidos hasta el momento.")
        else:
            print("-" * 40)
            print(f"Total Objetos:    ${suma_precios}")
            print(f"Total Intereses:  ${suma_intereses}")
            print(f"Total:            ${suma_totales}")
            print("===========================================")

    def buscar_objeto(self, id):
        if not self.inventario:
            print("No hay objetos en el inventario.")
            return None
        
        # Verficar si el ID es valido
        abc, num = id.split('-') if '-' in id else (None, None)
        prefijos = [val[1] for val in self.categorias.values()]
        if abc and (abc in prefijos) and num and num.isdigit():
            for obj in self.inventario:
                if obj.get_ID() == id:
                    print(obj.info())
                    return obj
            print("No se encontró un objeto con ese ID.")
            return None
        else:
            print("ID inválido. El formato debe ser 'ABC-XXX' donde ABC es el prefijo de la categoría y XXX es un número.")
            return None

    def registrar_prestamo(self):
        if not self.clientes or not self.inventario:
            print("No hay clientes o inventario disponible para registrar un préstamo.")
            return
        
        # Seleccionar cliente
        self.listar_amigo()
        seleccion_cliente = input("    Seleccione el número del amigo para el préstamo (Enter para cancelar): ")
        if not seleccion_cliente:
            print("Operación cancelada.")
            return
        else:
            idx_cliente = int(seleccion_cliente)
            if 1 <= idx_cliente <= len(self.clientes):
                cliente = self.clientes[idx_cliente - 1]
                print(f"Amigo seleccionado: {cliente.info()}")
            else:
                print("Índice de amigo fuera de rango. Operación cancelada.")
                return
        
        print("\n")
        # Seleccionar objeto
        self.listar_inventario(estado=0) # Mostrar solo objetos disponibles
        seleccion_objeto = self.buscar_objeto(input("    Ingrese el ID del objeto a prestar (Enter para cancelar): "))
        if not seleccion_objeto:
            print("Error: Objeto no encontrado.")
            return
        else:
            objeto = seleccion_objeto
            if objeto.get_estado() != 0:
                print("El objeto seleccionado no está disponible para préstamo. Operación cancelada.")
                return
        
        print("\n")
        while True:
            print("""Tiempos de Prestamos Definidos (Dias):
    1) 5
    2) 10
    3) 15
    4) 30""")
            opcion = input("Seleccione el tiempo de préstamo: ")
            if opcion in ['1', '2', '3', '4']:
                dias = self.dias_prestamo_definidos[int(opcion) - 1]
                break
            else:
                print("    - Error: opción inválida, seleccione una opción del 1 al 4")
        
        fecha_prestamo = datetime.now().date()
        fecha_vencimiento = fecha_prestamo + timedelta(days=dias)
        # Marca el objeto como prestado
        objeto.set_estado(1)
        # Crea el préstamo y lo guarda
        nuevo_prestamo = Prestamo(self.contador_id_prestamos + 1, cliente, objeto, fecha_vencimiento)
        self.prestamos.append(nuevo_prestamo)
        self.contador_id_prestamos += 1
        print(f"Préstamo registrado. Fecha de Prestamo: {fecha_prestamo.strftime('%d/%m/%Y')}")
        print(f"    - {nuevo_prestamo.info()}")

    def eliminar_prestamos(self):
        if not self.prestamos:
            print("No hay préstamos registrados para eliminar.")
            return
        
        self.listar_prestamos()
        seleccion = input("    Ingrese el número del préstamo a registrar como devuelto (Enter para cancelar): ")
        if not seleccion or not seleccion.isdigit():
            print("Operación cancelada.")
            return
        idx = int(seleccion)
        if 1 <= idx <= len(self.prestamos):
            prestamo = self.prestamos.pop(idx - 1)
            # Cambiar el estado del objeto a disponible
            prestamo.get_objeto().set_estado(0)
            print("    Préstamo eliminado exitosamente y objeto devuelto al inventario.")
            
            # Generar certificado de devolución
            amigo = prestamo.get_amigo()
            objeto = prestamo.get_objeto()
            fecha_vencimiento = prestamo.get_fecha()
            fecha_actual = datetime.now().date()
            
            diferencia = prestamo.calcular_dias_restantes()
            mensaje_dias = f"Faltaban {diferencia} día(s) para el vencimiento." if diferencia > 0 else f"Devuelto con {abs(diferencia)} día(s) de retraso." if diferencia < 0 else "Devuelto justo el día del vencimiento."
            
            certificado = f"""
======================================
     CERTIFICADO DE DEVOLUCIÓN
======================================
Amigo: {amigo.get_nombre()} {amigo.get_apellido()}
Documento: {amigo.get_documento()}
--------------------------------------
Objeto devuelto: {objeto.get_nombre()}
Categoria: {self.categorias[objeto.get_id_categoria()][0] if objeto.get_id_categoria() > 0 else "Sin categoría"}
ID Objeto: {objeto.get_ID()}
--------------------------------------
Fecha de vencimiento: {fecha_vencimiento.strftime('%d/%m/%Y')}
Fecha de devolución:  {fecha_actual.strftime('%d/%m/%Y')}
{mensaje_dias}
======================================
"""
            print(certificado)
        else:
            self.total_devoluciones += 1
            print("Índice fuera de rango. Operación cancelada.")

    def listar_prestamos(self):
        if not self.prestamos:
            print("No hay préstamos registrados.")
            return
        print("Lista de Préstamos:")
        total = 0
        for idx, prestamo in enumerate(self.prestamos, start=1):
            print(f"{idx}. {prestamo.info()}")
            total += 1
        print(f"    Total: {total}")

    def generar_certificado_venta(self, prestamo):
        amigo = prestamo.get_amigo()
        objeto = prestamo.get_objeto()
        precio = objeto.get_precio()
        fecha_actual = datetime.now().date()
        intereses = int(precio * 0.23)
        
        certificado = f"""
======================================
           FACTURA DE VENTA
======================================
Fecha de Vencimiento: {prestamo.get_fecha().strftime('%d/%m/%Y')}
Fecha de Venta Automática: {fecha_actual.strftime('%d/%m/%Y')}

Cliente: {amigo.get_nombre()} {amigo.get_apellido()}
Documento: {amigo.get_documento()}
--------------------------------------
Motivo: Préstamo excedido por más de 30 días.
El siguiente objeto pasa a ser propiedad del cliente.

Objeto: {objeto.get_nombre()}
Categoria: {self.categorias[objeto.get_id_categoria()][0] if objeto.get_id_categoria() > 0 else "Sin categoría"}
ID Objeto: {objeto.get_ID()}

--------------------------------------
Precio del Objeto: ${precio}
Intereses: ${intereses} (23%)
Total a Pagar: ${precio + intereses}
======================================
"""
        print(certificado)

    def verificar_prestamos_vencidos(self):
        if not self.prestamos:
            print("No hay préstamos activos para verificar.")
            return

        prestamos_a_eliminar = []

        print("=== REVISIÓN DE PRÉSTAMOS ===")
        for prestamo in self.prestamos:
            dias_restantes = prestamo.calcular_dias_restantes()
            retraso = -dias_restantes
            amigo = prestamo.get_amigo()
            objeto = prestamo.get_objeto()
            
            if retraso > 0:
                if not prestamo.get_vencido():
                    prestamo.set_vencido(True)
                print(f"- VENCIDO ({retraso} días tarde): Objeto '{objeto.get_nombre()}' prestado a {amigo.get_nombre()} {amigo.get_apellido()}")
                if retraso > 30:
                    print("  -> Facturando venta por límite de tiempo!")
                    prestamos_a_eliminar.append(prestamo)
            else:
                print(f"- Al día (Faltan {abs(dias_restantes)} días): Objeto '{objeto.get_nombre()}'")

        # Convertir préstamos vencidos en ventas
        for p in prestamos_a_eliminar:
            objeto = p.get_objeto()
            self.generar_certificado_venta(p)
            
            # Cambiar estado a vendido
            objeto.set_estado(2)

            # Eliminar préstamo activo
            self.prestamos.remove(p)

        if prestamos_a_eliminar:
            print(f"\nSe han cerrado {len(prestamos_a_eliminar)} préstamo(s) mediante venta automática.")

    def top_prestamos(self):
        if not self.prestamos:
            print("No hay préstamos activos para mostrar.")
            return

        conteo_amigos = {}
        for p in self.prestamos:
            amigo = p.get_amigo()
            doc = amigo.get_documento()
            if doc not in conteo_amigos:
                conteo_amigos[doc] = {"amigo": amigo, "cantidad": 1}
            else:
                conteo_amigos[doc]["cantidad"] += 1
        
        lista_conteo = list(conteo_amigos.values())
        
        # Ordenar de mayor a menor cantidad
        mayor_cantidad = sorted(lista_conteo, key=lambda x: x["cantidad"], reverse=True)
        
        print("Top Amigos con más préstamos activos:")
        for idx, item in enumerate(mayor_cantidad, start=1):
            amigo = item["amigo"]
            print(f"{idx}. {amigo.get_nombre()} {amigo.get_apellido()} - Documento: {amigo.get_documento()} | {item['cantidad']} préstamo(s)")
