class Transaccion:
    def __init__(
        self,
        num_transferencia,
        estado,
        fecha,
        monto,
        tipo,
        numero,
        permitido_actual_para_transaccion,
    ):
        self.num_transferencia = num_transferencia
        self.estado = estado
        self.monto = monto
        self.fecha = fecha
        self.tipo = tipo
        self.numero = numero
        self.permitido_actual_para_transaccion = permitido_actual_para_transaccion
