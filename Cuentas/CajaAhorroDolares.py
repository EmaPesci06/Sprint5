from Cuentas.Cuentas import Cuenta


class CajaAhorroDolares(Cuenta):
    def __init__(self, num_cuenta, saldo, comision_mensual, monto):
        super().__init__(
            num_cuenta,
            tipo="Ahorro Dolares",
            saldo=saldo,
            comision_mensual=comision_mensual,
        )
        self.monto = monto
