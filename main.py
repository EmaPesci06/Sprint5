from Tarjeta import TarjetaDebito
from Clientes.Classic import Classic
from Clientes.Gold import Gold
from Clientes.Black import Black
from Clientes.Cliente import Cliente
from Cuentas.CajaAhorroPesos import CajaAhorroPesos
from Cuentas.CuentaCorrientePesos import CuentaCorrientePesos
import json


def crear_cliente():
    tipo_cliente = input(
        "Ingrese el tipo de cliente (Classic/Gold/Black): "
    ).capitalize()
    numero = int(input("Ingrese su numero de cliente: "))
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    dni = input("Ingrese el DNI del cliente: ")

    if tipo_cliente == "Classic":
        num_tarjeta_debito = input("Ingrese el número de tarjeta de débito: ")
        cliente = Classic(
            Cliente(numero, nombre, apellido, dni, tipo_cliente),
            num_tarjeta_debito,
            CajaAhorroPesos("12345", 0.0, 0.0, 0.0),
            CuentaCorrientePesos("67890", 0.0, 0.0, 0.0),
            5,
            10000,
        )
    elif tipo_cliente == "Gold":
        retiros_diarios = int(input("Ingrese el límite diario de retiros: "))
        caja_ahorro_pesos_saldo = float(
            input("Ingrese el saldo de la cuenta de ahorro en pesos: ")
        )
        cliente = Gold(
            Cliente(numero, nombre, apellido, dni, tipo_cliente),
            "0000-0000-0000-0000",
            cajas_ahorro_pesos=2,
            cuenta_corriente=1,
            retiros_diarios=retiros_diarios,
            cuentas_inversion=[],
            chequera=True,
        )
        for caja in cliente.cajas_ahorro_pesos:
            caja.saldo = caja_ahorro_pesos_saldo
        if cliente.cuenta_corriente:
            cliente.cuenta_corriente.saldo = caja_ahorro_pesos_saldo
    elif tipo_cliente == "Black":
        cliente = Black(
            Cliente(numero, nombre, apellido, dni, tipo_cliente),
            num_tarjetas_debito=5,
            cajas_ahorro_pesos=5,
            cajas_ahorro_dolares=5,
            cuentas_corrientes=3,
            retiros_diarios=100000,
            cuentas_inversion=[],
            chequeras=2,
        )
    else:
        print("Tipo de cliente no válido.")
        return None

    return cliente


def mostrar_cliente(cliente):
    if cliente:
        # Convertir el cliente a un diccionario
        cliente_dict = {
            "numero": cliente.numero,
            "nombre": cliente.nombre,
            "apellido": cliente.apellido,
            "dni": cliente.dni,
            "tipo": cliente.tipo,
            "transacciones": cliente.transacciones,  # Asumiendo que el cliente tiene un atributo 'transacciones'
        }

        # Convertir el diccionario a formato JSON
        cliente_json = json.dumps(cliente_dict, indent=4)

        # Crear el informe HTML
        html_reporte = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Reporte de Cliente</title>
        </head>
        <body>
            <h1>Reporte de Cliente</h1>
            <pre>{cliente_json}</pre>
        </body>
        </html>
        """

        # Guardar el informe en un archivo HTML
        with open(
            f"{cliente.nombre}_{cliente.apellido}_{cliente.dni}.html", "w"
        ) as archivo_html:
            archivo_html.write(html_reporte)

        print("Reporte generado exitosamente en el archivo 'reporte_cliente.html'.")
    else:
        print("Cliente no válido.")


# Ejemplo de uso
cliente_creado = crear_cliente()
mostrar_cliente(cliente_creado)
