from django.db import models

class CategoriaExtra(models.Model):
    nombre = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    cantidadLimite = models.IntegerField()

    def __str__(self):
        return self.nombre

class Extras(models.Model):
    nombre = models.CharField(max_length=50)
    precioporPorcion = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    idcategoria_extra = models.ForeignKey(CategoriaExtra, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class CategoriaPlato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    personalizable = models.BooleanField(default=False)
    idcategoria_plato = models.ForeignKey(CategoriaPlato, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class CategoriaCliente(models.Model):
    fidelidad = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    beneficios = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return self.correo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    idusuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    idcategoria_cliente = models.ForeignKey(CategoriaCliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.cargo

class Empleado(models.Model):
    nombreEmp = models.CharField(max_length=50)
    apeEmp = models.CharField(max_length=50)
    dni=models.CharField(max_length=8)
    numeroTelefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    idusuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    idrol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombreEmp} {self.apeEmp}'

class Mesa(models.Model):
    numeroMesa = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.numeroMesa

class Pedido(models.Model):
    cantidadTotalPlatos = models.IntegerField()
    montoTotal = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateField()
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idmesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    idempleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pedido {self.id} - Cliente {self.cliente.nombre}'

class PlatoPedido(models.Model):
    idpedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    idplato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    precioBasePlato = models.DecimalField(max_digits=6, decimal_places=2)
    precioFinalPlato = models.DecimalField(max_digits=6, decimal_places=2)
    tipoPedido = models.CharField(max_length=50)

class ExtrasPlatoPedido(models.Model):
    idextra = models.ForeignKey(Extras, on_delete=models.CASCADE)
    idplato_pedido = models.ForeignKey(PlatoPedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precioPersonalizacion = models.DecimalField(max_digits=6, decimal_places=2)

class Pago(models.Model):
    montoPagado = models.DecimalField(max_digits=8, decimal_places=2)
    montoRestante = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateField()
    metodo = models.CharField(max_length=50)
    idpedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    def __str__(self):
        return f'Pago {self.id} - {self.monto}'

