from Tarjeta import TarjetaCredito, TarjetaDebito
from Cuentas.Cuentas import Cuenta
from Cuentas.CajaAhorroDolares import CajaAhorroDolares
from Cuentas.CajaAhorroPesos import CajaAhorroPesos
from Cuentas.CuentaCorrienteDolares import CuentaCorrienteDolares
from Cuentas.CuentaCorrientePesos import CuentaCorrientePesos
from Cuentas.CuentaInversion import CuentaInversion
from Clientes.Cliente import Cliente
from Transacciones import Transaccion


class Gold(Cliente):
    def __init__(
        self,
        cliente,
        num_tarjeta_debito,
        cajas_ahorro_pesos=2,
        cuenta_corriente=1,
        tarjetas_credito=[],
        retiros_diarios=20000,
        cuentas_inversion=[],
        chequera=True,
    ):
        super().__init__(
            cliente.numero, cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo
        )
        self.tarjeta_de_debito = TarjetaDebito(
            num_tarjeta_debito, tipo="Débito", limite=20000, marca="Visa"
        )
        self.cajas_ahorro_pesos = [
            CajaAhorroPesos(
                num_cuenta=f"Cuenta-{i+1}",
                saldo=0,  # Puedes establecer el saldo inicial a 0 o al valor que desees
                comision_mensual=5,  # Establece el valor adecuado para la comisión mensual
                monto=0,  # Establece el valor inicial del monto a 0 o al valor que desees
            )
            for i in range(cajas_ahorro_pesos)
        ]

        self.cuenta_corriente = (
            CuentaCorrientePesos(
                num_cuenta=f"Cuenta-Corriente-{cliente.dni}",  # Puedes personalizar el número de cuenta como desees
                saldo=0,  # Puedes establecer el saldo inicial a 0 o al valor que desees
                comision_mensual=5,  # Establece el valor adecuado para la comisión mensual
                monto=0,  # Establece el valor inicial del monto a 0 o al valor que desees
            )
            if cuenta_corriente > 0
            else None
        )

        self.tarjetas_credito = tarjetas_credito
        self.retiros_diarios = retiros_diarios
        self.cuentas_inversion = cuentas_inversion
        self.chequera = chequera

    def realizar_retiro(self, monto):
        if monto <= self.retiros_diarios:
            for caja_pesos in self.cajas_ahorro_pesos:
                if monto <= caja_pesos.saldo:
                    caja_pesos.saldo -= monto
                    return f"Retiro de {monto} pesos exitoso."
            return "Fondos insuficientes en las cuentas de ahorro en pesos."
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
            and monto_con_comision <= self.obtener_saldo_total()
        ):
            # Lógica para realizar la transferencia
            pass
        else:
            return "Fondos insuficientes o transacción no permitida para realizar la transferencia."
