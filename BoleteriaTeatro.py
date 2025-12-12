obras_disponibles = [

    {"obra":"1. Hamlet - 7:00 PM",
     "asientos":["A1","A2","A3","B1","B2","B3"],
     "precio":50,
     "sala":"Sala Principal",
     "ocupados":[]},
     {"obra":"2. La Casa de Bernarda Alba - 8:30 PM",
     "asientos":["A1","A2","A3","B1","B2","B3"],
     "precio":30,
     "sala":"Sala Blanca",
     "ocupados":[]},
     {"obra":"3. El Rey Lear - 9:00 PM",
     "asientos":["A1","A2","A3","B1","B2","B3"],
     "precio":15,
     "sala":"Sala Roja",
     "ocupados":[]}
]

orden_abecedario=[
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

tickets_comprados=[]

def mostrar_cartelera():
    print("Cartelera de Obras Disponibles:")
    for obra in obras_disponibles:
        print(f"{obra['obra']} - Precio: ${obra['precio']}")
       
def mostrar_sala_y_butacas(obra_seleccionada):
   if obra_seleccionada < 1 or obra_seleccionada > len(obras_disponibles):
        print("Obra no válida.")
        return  
   obra = obras_disponibles[obra_seleccionada - 1]
   print(f"Sala: {obra['sala']}")
   print("Butacas Disponibles:")
   for asiento in obra['asientos']:  
        if(asiento == (orden_abecedario[orden_abecedario.index(asiento[0])]+'1') 
           and orden_abecedario[orden_abecedario.index(asiento[0])]!='Z'
           and orden_abecedario[orden_abecedario.index(asiento[0])]!='A'):
                print("\n")
        if asiento in obra['ocupados']:
            print("XX", end=" ")
        else:
            print(asiento, end=" ")
   print("\n")

def comprar_boletos(nombre,obra,cantidad_boletos,asientos_seleccionados):
    obras_disponibles[obra-1]['ocupados'].extend(asientos_seleccionados)
    tickets_comprados.append((nombre,obras_disponibles[obra-1]['obra'],cantidad_boletos,asientos_seleccionados))
    return
      

def ver_compras(nombre):
    for ticket in tickets_comprados:
        if ticket[0].lower()==nombre.lower():
            print(f"Compras de {nombre.upper()}: Obra: {ticket[1]}, Cantidad de Boletos: {ticket[2]}, Asientos: {', '.join(ticket[3])}")

def verificar_asientos_disponibles(obra,asiento_seleccionado,asientos_seleccionados):
    if(asiento_seleccionado in asientos_seleccionados):
        return False
    if asiento_seleccionado in obras_disponibles[obra-1]['asientos']:
        if asiento_seleccionado in obras_disponibles[obra-1]['ocupados']:
                return False
        else:
                return True
    else:
        return False

def validar_obra(obra):
    if obra < 1 or obra > len(obras_disponibles):
        return False
    return True

def traer_obra(obra):
    return f"{obras_disponibles[obra-1]['obra']}  Precio:${obras_disponibles[obra-1]['precio']}"

def validar_cantidad_asientos_libre(obra,cantidad_boletos):
    if(not cantidad_boletos.isdigit()):
        return False    
    cantidad_boletos=int(cantidad_boletos)
    asientos_libres = len(obras_disponibles[obra-1]['asientos']) - len(obras_disponibles[obra-1]['ocupados'])
    if cantidad_boletos > asientos_libres or cantidad_boletos <=0:
        return False
    return True

def validar_nombre(nombre):
    if len(nombre.strip())<4:
        return False
    return True


def pagar_compra(obra,cantidad_boletos,pago):
    total = obras_disponibles[obra-1]['precio'] * cantidad_boletos
    if pago >= total:
        cambio = pago - total
        return True, cambio
    else:
        return False, 0

while True:
    print("-------------------------------")
    print("TEATRO FENIX - MENU PRINCIPAL")
    print("-------------------------------")
    opcion = input("Seleccione una opción:\n1. Ver cartelera\n2. Ver Sala y Butacas\n3. Comprar Boletos\n4. Ver mis compras\n5. Salir\n")

    if opcion == "1":
        mostrar_cartelera() 
    elif opcion == "2":
        obra_seleccionada = int(input("Ingrese el número de la obra para ver la sala y butacas: "))
        while(not validar_obra(obra_seleccionada)):
            print("Obra no válida, por favor seleccione otra.")
            obra_seleccionada = int(input("Ingrese el número de la obra que desea comprar: "))
        print("______",traer_obra(obra_seleccionada),"______")
        mostrar_sala_y_butacas(obra_seleccionada) 
    elif opcion == "3": 
        mostrar_cartelera()              
        obra = int(input("Ingrese el número de la obra que desea comprar: "))        
        while(not validar_obra(obra)):
            print("Obra no válida, por favor seleccione otra.")
            obra = int(input("Ingrese el número de la obra que desea comprar: "))
        print("______",traer_obra(obra),"______")
        mostrar_sala_y_butacas(obra) 
        nombre = input("Ingrese su nombre para registrar la compra: ")
        while(not validar_nombre(nombre)):
            print("Nombre no válido, debe tener al menos 4 caracteres.")
            nombre = input("Ingrese su nombre para registrar la compra: ")
        cantidad_boletos = input("Ingrese la cantidad de boletos que desea comprar: ")
        while(not validar_cantidad_asientos_libre(obra,cantidad_boletos)):
            print("Cantidad de boletos no válida o excede los asientos disponibles, por favor ingrese otra cantidad.")
            cantidad_boletos = input("Ingrese la cantidad de boletos que desea comprar: ")
        cantidad_boletos = int(cantidad_boletos)
        asientos_seleccionados = []
        for _ in range(cantidad_boletos):
            asiento = input("Ingrese el asiento que desea (ejemplo A1): ")
            while(not verificar_asientos_disponibles(obra,asiento,asientos_seleccionados)):
                print("Asiento no disponible, por favor seleccione otro.")
                asiento = input("Ingrese el asiento que desea (ejemplo A1): ")
            asientos_seleccionados.append(asiento)
        total_a_pagar = obras_disponibles[obra-1]['precio'] * cantidad_boletos
        print(f"Total a pagar: ${total_a_pagar}")
        pago = float(input("Ingrese el monto con el que va a pagar: $"))
        pago_valido, cambio = pagar_compra(obra,cantidad_boletos,pago)
        while(not pago_valido):
            print("Monto insuficiente, por favor ingrese un monto válido.")
            pago = float(input("Ingrese el monto con el que va a pagar: $"))
            pago_valido, cambio = pagar_compra(obra,cantidad_boletos,pago)
        print(f"Pago exitoso. Su cambio es: ${cambio}")
        comprar_boletos(nombre,obra,cantidad_boletos,asientos_seleccionados) 
    elif opcion == "4":
        nombre = input("Ingrese su nombre para ver sus compras: ")
        ver_compras(nombre) 
    elif opcion == "5":
        print("Gracias por visitar el Teatro Fenix. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
