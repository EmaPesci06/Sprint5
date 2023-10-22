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


def calcular_monto_total(precio_dolar, monto_deseado, impuesto_pais, ganancias):
    impuesto_total = monto_deseado * impuesto_pais
    ganancias_total = monto_deseado * ganancias
    monto_total = monto_deseado + impuesto_total + ganancias_total
    monto_total_en_pesos = monto_total * precio_dolar
    return monto_total_en_pesos


def descontar_comision(monto_original, porcentaje_comision):
    monto_descontado = monto_original - (monto_original * porcentaje_comision)
    return monto_descontado


def calcular_monto_plazo_fijo(monto_inicial, tasa_interes, tiempo_anios):
    monto_final = monto_inicial * (1 + tasa_interes * tiempo_anios)
    return monto_final
