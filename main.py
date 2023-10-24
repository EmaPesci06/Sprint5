from Tarjeta import (
    TarjetaDebito,
    TarjetaCredito,
)  # Importa las clases de tarjetas necesarias
from Clientes.Black import (
    Black,
)  # Asegúrate de importar la clase Black desde su ubicación correcta
from Clientes.Cliente import Cliente
from Clientes.Classic import Classic
from Cuentas.CuentaCorrientePesos import CuentaCorrientePesos
from Cuentas.CuentaCorrienteDolares import CuentaCorrienteDolares
from Cuentas.CajaAhorroDolares import CajaAhorroDolares
from Cuentas.CajaAhorroPesos import CajaAhorroPesos
import json

# Crear un objeto de la clase Cliente (asegúrate de que tengas la clase Cliente definida)
cliente = Cliente(nombre="Nombre", apellido="Apellido", dni="123456789", tipo="Classic")

# Número de tarjeta de débito del cliente
num_tarjeta_debito = (
    "1234-5678-9101-1121"  # Reemplaza esto con el número real de la tarjeta
)

# Crear un objeto de la clase CuentaCorrientePesos con los argumentos necesarios
cuenta_pesos = CuentaCorrientePesos(
    num_cuenta="123456", saldo=1000, comision_mensual=10, monto=500
)
# Crear un objeto de la clase CuentaCorrienteDolares con los argumentos necesarios
cuenta_dolares = CuentaCorrienteDolares(
    num_cuenta="567890", saldo=500, comision_mensual=5, monto=100
)

# Crear un cliente Classic con la cuenta de ahorros en pesos y dólares proporcionadas
cliente_classic = Classic(
    cliente=cliente,
    num_tarjeta_debito=num_tarjeta_debito,
    cuenta_ahorro_pesos=cuenta_pesos,  # Pasa la cuenta de ahorros en pesos como un argumento
    tiene_caja_ahorro_dolares=True,
    cuenta_ahorro_dolares=cuenta_dolares,  # Pasa la cuenta de ahorros en dólares como un argumento
)


# Crear un objeto de la clase Cliente
cliente = Cliente(
    nombre="Nombre del Cliente",
    apellido="Apellido del Cliente",
    dni="123456789",
    tipo="Black",
)

# Crear tarjetas de débito y crédito si es necesario
tarjeta_debito = TarjetaDebito(123431234312, "Debito-123", 200000, "VISA")
tarjeta_credito = TarjetaCredito(12331234312, "Credito-456", 140000, "MASTERCARD")

# Crear cuentas de ahorro y cuentas corrientes si es necesario
caja_ahorro_pesos = CajaAhorroPesos(
    num_cuenta="123456", saldo=1000, comision_mensual=5, monto=100
)
caja_ahorro_dolares = CajaAhorroDolares(
    num_cuenta="3312312", saldo=200000, comision_mensual=5, monto=124312
)
cuenta_corriente = CuentaCorrientePesos(
    num_cuenta="132345",
    saldo=21343,
    monto=132312323,
    comision_mensual=5,
)

# Crear un cliente Black usando el objeto de la clase Cliente y otros detalles necesarios
cliente_black = Black(
    cliente=cliente,
    num_tarjetas_debito=2,  # Número de tarjetas de débito
    tarjetas_credito=[tarjeta_credito],  # Lista de tarjetas de crédito
    cajas_ahorro_pesos=[caja_ahorro_pesos],  # Lista de cuentas de ahorro en pesos
    cajas_ahorro_dolares=[caja_ahorro_dolares],  # Lista de cuentas de ahorro en dólares
    cuentas_corrientes=[cuenta_corriente],  # Lista de cuentas corrientes
    retiros_diarios=100000,  # Límite de retiros diarios
    cuentas_inversion=[],  # Lista de cuentas de inversión (vacía en este ejemplo)
    chequeras=2,  # Número de chequeras
)

# Ahora puedes usar el objeto cliente_black para realizar operaciones específicas para clientes Black
