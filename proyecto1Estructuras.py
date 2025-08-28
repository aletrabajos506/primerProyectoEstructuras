import hashlib


class PilaUndo:
    def __init__(self):
        self.__items = []

    def apilar(self, item):
        self.__items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.__items.pop()
        return None

    def esta_vacia(self):
        return len(self.__items) == 0


class ColaPrioridadCompra:
    def __init__(self):
        self.__items = []

    def encolar(self, compra, prioridad):
        self.__items.append((prioridad, compra))
        self.__items.sort(key=lambda x: x[0])  

    def desencolar(self):
        if not self.esta_vacia():
            return self.__items.pop(0)[1]
        return None

    def esta_vacia(self):
        return len(self.__items) == 0


class ColaIngreso:
    def __init__(self):
        self.__items = []

    def encolar(self, cliente):
        self.__items.append(cliente)

    def desencolar(self):
        if not self.esta_vacia():
            return self.__items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.__items) == 0

class Evento:
    def __init__(self, idEvento: str, nombre: str, fechaISO: str, capGrad: int, rapGram: int, capVIP: int, precioGrad: int, precioGram: int, precioVIP: int):
        self.idEvento = idEvento
        self.nombre = nombre
        self.fechaISO = fechaISO
        self.capGrad = capGrad
        self.rapGram = rapGram
        self.capVIP = capVIP
        self.precioGrad = precioGrad
        self.precioGram = precioGram
        self.precioVIP = precioVIP


class Cliente:
    def __init__(self, idCliente: str, nombre: str, esPlatinum: bool, hashClave: str):
        self.idCliente = idCliente
        self.nombre = nombre
        self.esPlatinum = esPlatinum
        self.hashClave = hashClave
        
        
    def autenticar(self, clave: str) -> bool:
        """Verifica si la clave dada coincide con la clave hasheada del cliente."""
        clave_hash = hashlib.sha256(clave.encode()).hexdigest()
        return self.__hashClave == clave_hash




class Tiquetera:
    def __init__(self):
        self.__listaEventos: list[Evento] = []
        self.__listaClientes: list[Cliente] = []
        self.__listaTickets: list[Ticket] = []
        self.__pilaUndo = PilaUndo()
        self.__comprasPendientes = ColaPrioridadCompra()
        self.__ingresoEvento = ColaIngreso()

    
    def agregarEvento(self, evento: Evento):
        self.__listaEventos.append(evento)
        self.__pilaUndo.apilar(("agregarEvento", evento))

    def agregarCliente(self, cliente: Cliente):
        self.__listaClientes.append(cliente)
        self.__pilaUndo.apilar(("agregarCliente", cliente))

    def venderTicket(self, ticket: Ticket):
        self.__listaTickets.append(ticket)
        self.__pilaUndo.apilar(("venderTicket", ticket))

    def deshacerUltimaOperacion(self):
        operacion = self.__pilaUndo.desapilar()
        if operacion:
            accion, obj = operacion
            if accion == "agregarEvento":
                self.__listaEventos.remove(obj)
            elif accion == "agregarCliente":
                self.__listaClientes.remove(obj)
            elif accion == "venderTicket":
                self.__listaTickets.remove(obj)
            print(f"Deshecha la operación: {accion}")
        else:
            print("No hay operaciones para deshacer")



