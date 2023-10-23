def obtener_saldo_total(self):
    saldo_total = 0
    for caja_pesos in self.cajas_ahorro_pesos:
        saldo_total += caja_pesos.saldo
    for caja_dolares in self.cajas_ahorro_dolares:
        saldo_total += caja_dolares.saldo
    if self.cuenta_corriente:
        saldo_total += self.cuenta_corriente.saldo
    # Agregar lógica para sumar el saldo de cuentas de inversión, tarjetas de crédito, etc., si es necesario
    return saldo_total
