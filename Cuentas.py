class Cuenta:
    def __init__(self, num_cuenta, tipo, saldo, comision_mensual):
        self.num_cuenta = num_cuenta
        self.tipo = tipo
        self.saldo = saldo
        self.comision_mensual = comision_mensual


class CuentaDeAhorroPesos(Cuenta):
    def __init__(self, num_cuenta, saldo, comision_mensual, monto):
        super().__init__(
            num_cuenta,
            tipo="Ahorro Pesos",
            saldo=saldo,
            comision_mensual=comision_mensual,
        )
        self.monto = monto


class CuentaDeAhorroDolares(Cuenta):
    def __init__(self, num_cuenta, saldo, comision_mensual, monto):
        super().__init__(
            num_cuenta,
            tipo="Ahorro Dolares",
            saldo=saldo,
            comision_mensual=comision_mensual,
        )
        self.monto = monto


class CuentaCorrientePesos(Cuenta):
    def __init__(self, num_cuenta, saldo, comision_mensual, monto):
        super().__init__(
            num_cuenta,
            tipo="Corriente Pesos",
            saldo=saldo,
            comision_mensual=comision_mensual,
        )
        self.monto = monto


class CuentaCorrienteDolares(Cuenta):
    def __init__(self, num_cuenta, saldo, comision_mensual, monto):
        super().__init__(
            num_cuenta,
            tipo="Corriente Dolares",
            saldo=saldo,
            comision_mensual=comision_mensual,
        )
        self.monto = monto


class CuentaInversion(Cuenta):
    def __init__(self, num_cuenta, saldo, comision_mensual, monto):
        super().__init__(
            num_cuenta, tipo="Inversion", saldo=saldo, comision_mensual=comision_mensual
        )
        self.monto = monto
