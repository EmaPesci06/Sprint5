class Tarjeta:
    def __init__(self, num_tarjeta, tipo, monto):
        self.num_tarjeta = num_tarjeta
        self.tipo = tipo
        self.monto = monto


class TarjetaDebito(Tarjeta):
    def __init__(self, num_tarjeta, tipo, monto, marca):
        super().__init__(num_tarjeta, tipo, monto)
        self.marca = marca


class TarjetaCredito(Tarjeta):
    def __init__(self, num_tarjeta, tipo, monto, marca):
        super().__init__(num_tarjeta, tipo, monto)
        self.marca = marca
