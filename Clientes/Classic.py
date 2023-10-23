from Tarjeta import TarjetaDebito
from Cuentas import CajaAhorroPesos, CajaAhorroDolares, Transaccion
from Cliente import Cliente


class Classic(Cliente):
    def __init__(
        self,
        cliente,
        num_tarjeta_debito,
        tiene_caja_ahorro_dolares=False,
        retiros_diarios_sin_comision=5,
        limite_retiro_diario=10000,
    ):
        super().__init__(cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo)
        self.tarjeta_de_debito = TarjetaDebito(
            num_tarjeta_debito, tipo="Débito", limite=limite_retiro_diario, marca="Visa"
        )
        self.caja_ahorro_pesos = CajaAhorroPesos()
        self.caja_ahorro_dolares = (
            CajaAhorroDolares() if tiene_caja_ahorro_dolares else None
        )
        self.retiros_diarios_sin_comision = retiros_diarios_sin_comision
        self.limite_retiro_diario = limite_retiro_diario

    def realizar_retiro(self, monto):
        if monto <= self.limite_retiro_diario:
            if self.retiros_diarios_sin_comision > 0:
                self.retiros_diarios_sin_comision -= 1
                return f"Retiro de {monto} pesos exitoso. Te quedan {self.retiros_diarios_sin_comision} retiros gratuitos."
            else:
                tarifa = (
                    0.02 * monto
                )  # Aplicar una tarifa del 2% por retiros adicionales
                monto_con_tarifa = monto + tarifa
                if monto_con_tarifa <= self.caja_ahorro_pesos.saldo:
                    self.caja_ahorro_pesos.saldo -= monto_con_tarifa
                    return f"Retiro de {monto} pesos exitoso. Se aplicó una tarifa de {tarifa} pesos por el retiro."
                else:
                    return "Fondos insuficientes para realizar el retiro."
        else:
            return f"El límite diario de retiro es de {self.limite_retiro_diario} pesos para clientes Classic."

    def realizar_transferencia(self, monto, cuenta_destino):
        comision = monto * 0.01  # Comisión del 1% por transferencias salientes
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
            return "Fondos insuficientes o transacción no permitida para realizar la transferencia."
