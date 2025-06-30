# Repaso Evaluacion Transversal.
# ------------------------------
# - Uso de Funciones con y sin parametros.
# - Creacion de Menu.
# - Uso de Diccionarios.
# - Uso de Listas.
# - Ingreso de Datos desde el Teclado.
# - Presentacion de Informacion con Formato.

# (Manejar Diccionarios y Listas Entrelazadas.)
# ---------------------------------------------
# Caso Verduleria.
# Se necesita desarrollar una aplicacion en Python que permita manejar de
# forma independiente los productos y sus ventas, con ello se necesita Listar
# Ventas por producto, totalizar ventas por producto, ventas en un rango de fechas
# Totalizar las ventas de una categoria. cantidad de ventas entre un rango de precios
# de productos.

# Productos = {"001": ['Melon','Fruta',1500],
#              "002": ['Apio','Verdura',500],
#              "003": ['Pera','Fruta',600],
#              "004": ['Papas','Verdura',1400],
#              }

# ventas = {"001":[40,'10-02-2025'],
#		    "002":[ 5,'04-05-2024'],
#		    "003":[60,'15-03-2025'],
#		    "004":[10,'01-02-2024'],
#		    "005":[33,'12-03-2024'],
#           }

# Clave = "001", Valor = ['Melon','Fruta',1500]

# ---------------------------------------------------------------------------------------------------------------------------------------

Productos = {"001": ['Melon','Fruta',1500],
             "002": ['Apio','Verdura',500],              
             "003": ['Pera','Fruta',600],
             "004": ['Papas','Verdura',1400],
            }
Ventas = {"001":[40,'10-02-2025'],
		  "002":[ 5,'04-05-2024'],
		  "003":[60,'15-03-2025'],
		  "004":[10,'01-02-2024'],
		  "005":[33,'12-03-2024'],
        }

# ---------------------------------------------------------------------------------------------------------------------------------------

def ListarVentas_Categoria(Categoria):
    
    Lista = []
    
    for clave, valor in Productos.items():
        if valor[1].lower() == Categoria.lower():
            fila = valor[0] + ' -  ' +str(Ventas[clave][0]) + ' - ' + Ventas[clave][1]
            Lista.append(fila)
    Lista.sort()
    print(Lista) 
    
def TotalizarVentas_Categoria(Categoria):
    
    Total = 0
    
    for clave, valor in Productos.items():
        if valor[1].lower() == Categoria.lower():
            Cantidad = Ventas[clave][0]
            Precio = valor[2]
            Total = Total + (Cantidad * Precio)
    if Total > 0:
        print(f"Total de Ventas de la Categoria '{Categoria}': $ {Total}  ")
    else:
        print(f"No se Encontraron Ventas para la Categoria '{Categoria}'.  ")
        
def TotalizarVentas_Años(año):
    Total = 0
    for clave, valor in Ventas.items():
        fecha_Venta = valor[1]
        año_Venta = fecha_Venta[6:10]
        if año_Venta == int(año_Venta):
            try:
                Precio = Productos[clave][2]
                Cantidad = valor[0]
                Total = Total + (Cantidad * Precio)
            except:
                print(f"El Producto con Clave '{clave}' no Existe en el Inventario.  ")
    if Total > 0:
        print(f"Total de Ventas del Año '{año}': $ {Total}  ")
    else:
        print(f"No se Encontraron Ventas para el Año '{año}'.  ")
    
def ListarVentas_Años(año):
    Lista = []
    for clave, valor in Ventas.items():
        fecha_Venta = valor[1]
        año_Venta = fecha_Venta[6:10]
        if año == año_Venta:
            try: 
                Lista.append(Productos[clave][0] + ' - ' + fecha_Venta)
            except:
                print(f"El Producto con Clave '{clave}' no Existe en el Inventario.  ")
    Lista.sort()
    print(Lista)
    
def ListarVentas_Rango(minimo, maximo):
    Lista = []
    for clave, valor in Productos.items():
         if valor[2] >= minimo and valor[2] <= maximo:
             print(valor[0] + ' - ' + valor[1] + ' - ' + str(valor[2]) + ' - ' + str(Ventas[clave][0]) + ' - ' + Ventas[clave][1])
    Lista.sort()
    print(Lista)
             
def CambiarPrecio_Producto(Nombre_Producto):
    for clave, valor in Productos.items():
        if valor[2].lower() == Nombre_Producto.lower():
            try:
                Precio = int(input(f"Ingrese el Nuevo Precio para el Producto '{Nombre_Producto}':  "))
                Productos[clave][2] = Precio
                print(f"El Precio del Producto '{Nombre_Producto}' ha sido Actualizado a $ {Precio}.  ")
            except:
                print("Error, el Precio Debe ser un Numero Entero.  ")
                return
    print(f"Producto '{Nombre_Producto}' no Encontrado en el Inventario.  ")
          
# ---------------------------------------------------------------------------------------------------------------------------------------

# Menu
Ciclo = True

while Ciclo:
    print("- - MENU VERDULERIA 'OVALLINO' - -")
    print("")
    print("1.- Listar Ventas por Categoria.  ")
    print("2.- Totalizar Ventas por Categoria.  ")
    print("3.- Venta en un Año.  ")
    print("4.- Totalizar Ventas de una Categoria.  ")
    print("5.- Cantidad de Ventas en Rangos de Precios.  ")
    print("6.- Cambiar Precio de un Producto.  ")
    print("7.- Salir.  ")
    
    try:
        OP1 = int(input("Ingrese una Opcion (1-6):  "))
        match OP1:
            case 1:
                Categoria = input("Ingrese Categoria.  ")
                ListarVentas_Categoria(Categoria)
            case 2: 
                Categoria = input("Ingrese Categoria a Totalizar Ventas.  ")
                TotalizarVentas_Categoria(Categoria)
            case 3:
                try:
                    año = int(input("Ingrese el Año.  "))
                    TotalizarVentas_Años(año)
                except BaseException as error:
                    print(error)
            case 4:
                try: 
                    año = int(input("Ingrese el Año.  "))
                    ListarVentas_Años(año)
                except BaseException as error:
                    print(error)
            case 5:
                try: 
                    minimo = int(input("Ingrese el Precio Producto Minimo:  ")) 
                    maximo = int(input("Ingrese el Precio Producto Maximo:  "))
                    ListarVentas_Rango(minimo, maximo)
                except BaseException as error:
                    print(error)
            case 6: 
                Nombre_Producto = input("Ingrese el Nombre del Producto.  ")
                CambiarPrecio_Producto(Nombre_Producto)
            case 7:
                print("<Saliendo> - No Apague el Dispositivo.  ")
                Ciclo = False
            case _:
                print("Opcion Invalida. Por Favor Ingrese una Opcion Valida (1-6).  ")
    except ValueError as error:
        print(error)
