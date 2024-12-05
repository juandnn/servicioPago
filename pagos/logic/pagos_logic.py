from .. import models

def get_pagos():
    return models.Pago.objects.all()

def get_pagos_by_usuario(usuario):
    return models.Pago.objects.filter(usuario=usuario)
