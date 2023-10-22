from Tarjeta import Tarjeta


class Cliente:
    def __init__(self, nombre, apellido, dni, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo

    def __str__(self):
        return f"Nombre: {self.nombre} \n Apellido: {self.apellido} \n DNI: {self.dni} \n Tipo: {self.tipo}"

    def asignar_tarjeta(self, num_tarjeta, tipo, limite):
        self.tarjeta = Tarjeta(num_tarjeta, tipo, limite)
