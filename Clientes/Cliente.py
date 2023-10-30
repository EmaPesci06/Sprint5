from Tarjeta import Tarjeta


class Cliente:
    def __init__(self, numero, nombre, apellido, dni, tipo):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.transacciones = []

    def __str__(self):
        return f"Nombre: {self.nombre} \n Apellido: {self.apellido} \n DNI: {self.dni} \n Tipo: {self.tipo}"

    def asignar_tarjeta(self, num_tarjeta, tipo, limite):
        self.tarjeta = Tarjeta(num_tarjeta, tipo, limite)
