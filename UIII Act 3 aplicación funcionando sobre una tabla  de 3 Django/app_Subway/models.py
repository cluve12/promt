from django.db import models

# ==========================================
# MODELO: SUCURSALES
# ==========================================
class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    direccion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: CLIENTES
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="clientes")
    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: EMPLEADOS
# ==========================================
class Empleado(models.Model):
    # Añadido un campo nombre para identificar al empleado en el sistema
    nombre = models.CharField(max_length=100, default='Empleado Sin Nombre')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="empleados")
    telefono = models.CharField(max_length=15)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    puesto = models.CharField(max_length=50)
    foto_perfil = models.ImageField(upload_to='empleados_fotos/', blank=True, null=True) # <--- ¡NUEVO CAMPO!

    def __str__(self):
        return f"{self.nombre} ({self.puesto} - {self.sucursal.nombre})"