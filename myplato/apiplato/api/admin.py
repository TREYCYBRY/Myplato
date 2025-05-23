from django.contrib import admin
from .models import (
    CategoriaExtra,
    Extras,
    CategoriaPlato,
    Plato,
    CategoriaCliente,
    Usuarios,
    Cliente,
    Rol,
    Empleado,
    Mesa,
    Pedido,
    Pago,
    PlatoPedido,
    ExtrasPlatoPedido,

)

# Register your models here.
admin.site.register(CategoriaExtra)
admin.site.register(Extras)
admin.site.register(Pedido)
admin.site.register(Rol)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(CategoriaCliente)
admin.site.register(CategoriaPlato)
admin.site.register(Usuarios)
admin.site.register(Mesa)
admin.site.register(Plato)
admin.site.register(Pago)
admin.site.register(PlatoPedido)
admin.site.register(ExtrasPlatoPedido)