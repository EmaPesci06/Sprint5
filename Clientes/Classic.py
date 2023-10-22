from Tarjeta import TarjetaDebito
from Cuentas import CuentaDeAhorroPesos, CuentaDeAhorroDolares
from Cliente import Cliente


class Classic(Cliente):
    def __init__(
        self,
        cliente,
        num_tarjeta_debito,
        saldo_caja_ahorro_pesos,
        num_cuenta_ahorro_dolares=None,
    ):
        super().__init__(cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo)
        self.tarjeta_de_debito = TarjetaDebito(
            num_tarjeta_debito, tipo="Débito", limite=10000, marca="Visa"
        )
        self.caja_ahorro_pesos = CuentaDeAhorroPesos(
            num_cuenta="12345",
            saldo=saldo_caja_ahorro_pesos,
            comision_mensual=10,
            monto=500,
        )
        self.caja_ahorro_dolares = None
        if num_cuenta_ahorro_dolares:
            self.caja_ahorro_dolares = CuentaDeAhorroDolares(
                num_cuenta=num_cuenta_ahorro_dolares,
                saldo=0,
                comision_mensual=5,
                monto=0,
            )

    def realizar_retiro(self, monto):
        if monto <= 10000:
            if monto <= self.caja_ahorro_pesos.saldo:
                self.caja_ahorro_pesos.saldo -= monto
                return f"Retiro de {monto} pesos exitoso."
            else:
                return "Fondos insuficientes en la cuenta de ahorro en pesos."
        else:
            return (
                "El límite diario de retiro es de 10,000 pesos para clientes Classic."
            )

    def realizar_transferencia(self, monto, cuenta_destino):
        comision = monto * 0.01  # Comisión del 1% por transferencias salientes
        monto_con_comision = monto + comision
        if monto_con_comision <= self.caja_ahorro_pesos.saldo:
            self.caja_ahorro_pesos.saldo -= monto_con_comision
            cuenta_destino.depositar(monto)
            return f"Transferencia de {monto} pesos realizada con éxito."
        else:
            return "Fondos insuficientes para realizar la transferencia."
