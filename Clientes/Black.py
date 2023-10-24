from Tarjeta import TarjetaDebito, TarjetaCredito, Tarjeta
from Cuentas.CajaAhorroPesos import CajaAhorroPesos
from Cuentas.CajaAhorroDolares import CajaAhorroDolares
from Cuentas.CuentaCorrientePesos import CuentaCorrientePesos
from Clientes.Cliente import Cliente
from Transacciones import Transaccion


class Black(Cliente):
    def __init__(
        self,
        cliente,
        num_tarjetas_debito=5,
        cajas_ahorro_pesos=5,
        cajas_ahorro_dolares=5,
        cuentas_corrientes=3,
        tarjetas_credito=[],
        retiros_diarios=100000,
        cuentas_inversion=[],
        chequeras=2,
    ):
        super().__init__(cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo)
        self.tarjetas_de_debito = [
            TarjetaDebito(f"Debito-{i+1}", tipo="Débito", limite=10000, marca="Visa")
            for i in range(num_tarjetas_debito)
        ]
        self.cajas_ahorro_pesos = [
            CajaAhorroPesos(
                num_cuenta=f"Cuenta-{i+1}",
                comision_mensual=5,
                saldo=123321,
                monto=12333,
            )
            for i in range(len(cajas_ahorro_pesos))
        ]
        self.cajas_ahorro_dolares = [
            CajaAhorroDolares(
                num_cuenta=f"Cuenta-{_+1}",
                comision_mensual=5,
                saldo=123321,
                monto=12333,
            )
            for _ in range(cajas_ahorro_dolares)
        ]
        self.cuentas_corrientes = [
            CuentaCorrientePesos(
                num_cuenta=f"Cuenta-{_+1}",
                comision_mensual=5,
                saldo=123321,
                monto=12333,
            )
            for _ in range(cuentas_corrientes)
        ]
        self.tarjetas_credito = tarjetas_credito
        self.retiros_diarios = retiros_diarios
        self.cuentas_inversion = cuentas_inversion
        self.chequeras = chequeras

    def realizar_retiro(self, monto):
        if monto <= self.retiros_diarios:
            for caja_pesos in self.cajas_ahorro_pesos:
                if monto <= caja_pesos.saldo:
                    caja_pesos.saldo -= monto
                    return f"Retiro de {monto} pesos exitoso."
            for caja_dolares in self.cajas_ahorro_dolares:
                if monto <= caja_dolares.saldo:
                    caja_dolares.saldo -= monto
                    return f"Retiro de {monto} dólares exitoso."
            return "Fondos insuficientes en todas las cuentas."
        else:
            return "El límite diario de retiro es de $100,000 para clientes Black."
