from Tarjeta import TarjetaDebito, TarjetaCredito
from Cuentas import (
    CuentaDeAhorroPesos,
    CuentaDeAhorroDolares,
    CuentaCorriente,
    CuentaInversion,
    Transaccion,
)
from Cliente import Cliente


class Gold(Cliente):
    def __init__(
        self,
        cliente,
        num_tarjeta_debito,
        caja_ahorro_pesos,
        caja_ahorro_dolares=None,
        cuenta_corriente=None,
        tarjetas_credito=[],
        retiros_diarios=20000,
        cuentas_inversion=[],
        chequera=False,
    ):
        super().__init__(cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo)
        self.tarjeta_de_debito = TarjetaDebito(
            num_tarjeta_debito, tipo="Débito", limite=20000, marca="Visa"
        )
        self.caja_ahorro_pesos = caja_ahorro_pesos
        self.caja_ahorro_dolares = caja_ahorro_dolares
        self.cuenta_corriente = cuenta_corriente
        self.tarjetas_credito = tarjetas_credito
        self.retiros_diarios = retiros_diarios
        self.cuentas_inversion = cuentas_inversion
        self.chequera = chequera

    def realizar_retiro(self, monto):
        if monto <= self.retiros_diarios:
            if monto <= self.caja_ahorro_pesos.saldo:
                self.caja_ahorro_pesos.saldo -= monto
                return f"Retiro de {monto} pesos exitoso."
            else:
                return "Fondos insuficientes en la cuenta de ahorro en pesos."
        else:
            return "El límite diario de retiro es de $20,000 para clientes Gold."

    def realizar_transferencia(self, monto, cuenta_destino):
        comision = monto * 0.005  # Comisión del 0.5% por transferencias salientes
        monto_con_comision = monto + comision
        transaccion = Transaccion(
            num_transferencia="T125",
            estado="Completa",
            fecha="2023-10-21",
            monto=monto_con_comision,
            tipo="Transferencia Saliente",
            numero=self.tarjeta_de_debito.num_tarjeta,
            permitido_actual_para_transaccion=True,
        )
        if (
            transaccion.permitido_actual_para_transaccion
            and monto_con_comision <= self.caja_ahorro_pesos.saldo
        ):
            self.caja_ahorro_pesos.saldo -= monto_con_comision
            cuenta_destino.depositar(monto)
            return f"Transferencia de {monto} pesos realizada con éxito."
        else:
            return "Fondos insuficientes para realizar la transferencia."
