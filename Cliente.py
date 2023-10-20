class Classic:
    def __init__(self, cliente, tarjetaDeDebito, cajaAhorroDolar, retiros, comisiones):
        self.cliente = cliente
        self.tarjetaDeDebito = tarjetaDeDebito
        self.cajaAhorroDolar = cajaAhorroDolar
        self.retiros = retiros
        self.comisiones = comisiones


class Gold:
    def __init__(
        self,
        cliente,
        tarjetaDebito,
        cajaDeAhorro,
        tarjetaCredito,
        retiro,
        cuentaDeInversion,
        chequera,
        comision,
    ):
        self.cliente = cliente
        self.tarjetaDebito = tarjetaDebito
        self.cajaDeAhorro = cajaDeAhorro
        self.tarjetaCredito = tarjetaCredito
        self.retiro = retiro
        self.cuentaDeInversion = cuentaDeInversion
        self.chequera = chequera
        self.comision = comision


class Black:
    def __init__(
        self,
        cliente,
        tarjetaDebito,
        cajaDeAhorro,
        cuentaCorriente,
        tarjetaCredito,
        retiro,
        cuentaDeInversion,
        chequera,
    ):
        self.cliente = cliente
        self.tarjetaDebito = tarjetaDebito
        self.cajaDeAhorro = cajaDeAhorro
        self.cuentaCorriente = cuentaCorriente
        self.tarjetaCredito = tarjetaCredito
        self.retiro = retiro
        self.cuentaDeInversion = cuentaDeInversion
        self.chequera = chequera
