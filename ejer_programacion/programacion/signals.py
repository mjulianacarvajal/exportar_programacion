"""
    Mayor información en:
    https://docs.djangoproject.com/en/5.0/ref/signals/
"""

from typing import Any

from django.db.models.signals import (
    post_delete, post_init, post_save,
    pre_delete, pre_init, pre_save
)
from django.dispatch import receiver

from programacion.models import Sede


@receiver(signal=post_save, sender=Sede) # Using --> Base de datos que se está usando.
def registro_cambios(sender: Sede, instance: Sede, created: bool, *args, **kwargs) -> None:
    """
        En esta función es donde debes realizar los procesos posteriores a la edición de una instancia,
        en este caso es `Sede`, pero puedes hacer el registro que necesites, esta función se ejecuta
        despues de guardar cualquier modelo.
    """
    print('Función ejecutada después de guardar')
    return

