from Clientes.Cliente import Cliente
from Clientes.Classic import Classic
from Cuentas.CuentaCorrienteDolares import CuentaCorrienteDolares
import json

cliente_classic = Classic(
    Cliente("NombreCliente", "ApellidoCliente", "12345678", "Classic"),
    num_tarjeta_debito="1234 5678 9012 3456",
    tiene_caja_ahorro_dolares=CuentaCorrienteDolares(134432145543, 12431221, 12, 21332),
    retiros_diarios_sin_comision=5,
    limite_retiro_diario=10000,
)

print(cliente_classic)
