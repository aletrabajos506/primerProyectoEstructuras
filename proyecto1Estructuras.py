import hashlib
from typing import List
from datetime import datetime



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
    
    
    
    
import hashlib
from typing import Optional

class Auth:
    def __init__(self):
        
        self.__clientes: list[Cliente] = []

    def hashClave(self, clave: str) -> str:
        
        return hashlib.sha256(clave.encode()).hexdigest()

    def registrarCliente(self, cliente: Cliente):
        
        self.__clientes.append(cliente)

    def login(self, idCliente: str, clave: str) -> Optional[Cliente]:
        
        for cliente in self.__clientes:
            if cliente.idCliente == idCliente and cliente.autenticar(clave):
                return cliente
        return None

class Ticket:
    def __init__(self, idTicket: str, idEvento: str, idCliente: str, sector: str, 
                 precio: int, estado: str, fechaCompra: str):
        self.__idTicket = idTicket
        self.__idEvento = idEvento
        self.__idCliente = idCliente
        self.__sector = sector
        self.__precio = precio
        self.__estado = estado       # Ej: "Válido", "Cancelado", "Usado"
        self.__fechaCompra = fechaCompra
        self.__usado = False         # Atributo interno para marcar si fue utilizado

    # --- Getters ---
    @property
    def idTicket(self) -> str:
        return self.__idTicket

    @property
    def idEvento(self) -> str:
        return self.__idEvento

    @property
    def idCliente(self) -> str:
        return self.__idCliente

    @property
    def sector(self) -> str:
        return self.__sector

    @property
    def precio(self) -> int:
        return self.__precio

    @property
    def estado(self) -> str:
        return self.__estado

    @property
    def fechaCompra(self) -> str:
        return self.__fechaCompra

    @property
    def usado(self) -> bool:
        return self.__usado

    
    def usar(self):
        if not self.__usado and self.__estado == "Válido":
            self.__usado = True
            self.__estado = "Usado"
            print(f"Ticket {self.__idTicket} usado con éxito.")
        elif self.__estado != "Válido":
            print(f"El ticket {self.__idTicket} no es válido (Estado: {self.__estado}).")
        else:
            print(f"El ticket {self.__idTicket} ya fue usado.")

    def esValido(self) -> bool:
        """Verifica si el ticket aún es válido para usarse"""
        return self.__estado == "Válido" and not self.__usado

    
    def __str__(self):
        return (f"Ticket({self.__idTicket}, Evento:{self.__idEvento}, Cliente:{self.__idCliente}, "
                f"Sector:{self.__sector}, Precio:{self.__precio}, Estado:{self.__estado}, "
                f"FechaCompra:{self.__fechaCompra})")

class MergeSort:
    @staticmethod
    def ordenarEventos(listaEventos: List[Evento]) -> List[Evento]:
        if len(listaEventos) <= 1:
            return listaEventos

        mid = len(listaEventos) // 2
        izquierda = MergeSort.ordenarEventos(listaEventos[:mid])
        derecha = MergeSort.ordenarEventos(listaEventos[mid:])

        return MergeSort._merge(izquierda, derecha)

    @staticmethod
    def _merge(izquierda: List[Evento], derecha: List[Evento]) -> List[Evento]:
        resultado = []
        i = j = 0

        while i < len(izquierda) and j < len(derecha):
            # Comparar por fecha (asumiendo formato YYYY-MM-DD)
            fecha_izq = datetime.strptime(izquierda[i].fecha, "%Y-%m-%d")
            fecha_der = datetime.strptime(derecha[j].fecha, "%Y-%m-%d")

            if fecha_izq <= fecha_der:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        # agregar sobrantes
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado


class QuickSort:
    @staticmethod
    def ordenarEventos(listaEventos: List[Evento]) -> List[Evento]:
        if len(listaEventos) <= 1:
            return listaEventos

        pivote = listaEventos[len(listaEventos) // 2]
        fecha_pivote = datetime.strptime(pivote.fecha, "%Y-%m-%d")

        menores = [e for e in listaEventos if datetime.strptime(e.fecha, "%Y-%m-%d") < fecha_pivote]
        iguales = [e for e in listaEventos if datetime.strptime(e.fecha, "%Y-%m-%d") == fecha_pivote]
        mayores = [e for e in listaEventos if datetime.strptime(e.fecha, "%Y-%m-%d") > fecha_pivote]

        return QuickSort.ordenarEventos(menores) + iguales + QuickSort.ordenarEventos(mayores)

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



