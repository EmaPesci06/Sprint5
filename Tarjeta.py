class Tarjeta:
    def __init__(self, num_tarjeta, tipo, limite):
        self.num_tarjeta = num_tarjeta
        self.tipo = tipo
        self.limite = limite


class TarjetaDebito(Tarjeta):
    def __init__(self, num_tarjeta, tipo, limite, marca):
        super().__init__(num_tarjeta, tipo, limite)
        self.marca = marca


class TarjetaCredito(Tarjeta):
    def __init__(self, num_tarjeta, tipo, limite, marca):
        super().__init__(num_tarjeta, tipo, limite)
        self.marca = marca
