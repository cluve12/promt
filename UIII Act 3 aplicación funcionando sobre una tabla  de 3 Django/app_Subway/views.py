from django.shortcuts import render, redirect, get_object_or_404
from .models import Sucursal, Empleado # Importa Empleado
from django.http import HttpResponse # Para respuestas simples, aunque se usará render

# VISTA: Inicio del Sistema Subway
def inicio_subway(request):
    return render(request, 'inicio.html')

# ==========================================
# VISTAS PARA SUCURSALES
# ==========================================

# VISTA: Agregar Sucursal
def agregar_sucursal(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        horario_apertura = request.POST['horario_apertura']
        horario_cierre = request.POST['horario_cierre']
        direccion = request.POST['direccion']

        Sucursal.objects.create(
            nombre=nombre,
            telefono=telefono,
            horario_apertura=horario_apertura,
            horario_cierre=horario_cierre,
            direccion=direccion
        )
        return redirect('ver_sucursales') # Redirige a la lista de sucursales
    return render(request, 'sucursal/agregar_sucursal.html')

# VISTA: Ver Sucursales
def ver_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursales.html', {'sucursales': sucursales})

# VISTA: Actualizar Sucursal (muestra el formulario con datos existentes)
def actualizar_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id=id_sucursal)
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal})

# VISTA: Realizar Actualización de Sucursal (maneja el POST del formulario de actualización)
def realizar_actualizacion_sucursal(request, id_sucursal):
    if request.method == 'POST':
        sucursal = get_object_or_404(Sucursal, id=id_sucursal)
        sucursal.nombre = request.POST['nombre']
        sucursal.telefono = request.POST['telefono']
        sucursal.horario_apertura = request.POST['horario_apertura']
        sucursal.horario_cierre = request.POST['horario_cierre']
        sucursal.direccion = request.POST['direccion']
        sucursal.save()
        return redirect('ver_sucursales')
    return redirect('ver_sucursales') # En caso de acceso directo sin POST

# VISTA: Borrar Sucursal
def borrar_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id=id_sucursal)
    if request.method == 'POST': # Se asume confirmación por POST
        sucursal.delete()
        return redirect('ver_sucursales')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': sucursal}) # Mostrar confirmación

# ==========================================
# VISTAS PARA EMPLEADOS (Actualizar Foto de Perfil)
# ==========================================

# VISTA: Actualizar Foto de Perfil de Empleado
def actualizar_foto_perfil_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    if request.method == 'POST':
        if 'foto_perfil' in request.FILES:
            empleado.foto_perfil = request.FILES['foto_perfil']
            empleado.save()
            return redirect('ver_empleados') # Redirige a una vista de empleados (aún no creada)
                                            # Por ahora, puedes redirigir a inicio o ver_sucursales
        # Si no se subió un archivo o hubo otro error, puedes manejarlo aquí
        return redirect('actualizar_foto_perfil_empleado', id_empleado=id_empleado) # Recargar el formulario

    return render(request, 'empleados/actualizar_foto_perfil.html', {'empleado': empleado})

# Nota: Necesitarás crear vistas para 'ver_empleados', 'agregar_empleado', etc. para una funcionalidad completa de Empleados.
# Por ahora, solo tenemos la funcionalidad de actualizar foto de perfil.
def ver_empleados(request): # Vista placeholder para redirección
    empleados = Empleado.objects.all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados}) # Necesitarás crear este template