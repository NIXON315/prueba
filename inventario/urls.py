from django.urls import path
from . import views

app_name = "inventario"

urlpatterns = [
path('login', views.Login.as_view(), name='login'),
path('panel', views.Panel.as_view(), name='panel'),
path('salir', views.Salir.as_view(), name='salir'),
path('perfil/<str:modo>/<int:p>', views.Perfil.as_view(), name='perfil'),
path('eliminar/<str:modo>/<int:p>', views.Eliminar.as_view(), name='eliminar'),

path('listarProductos', views.ListarProductos.as_view(), name='listarProductos'),
path('agregarProducto', views.AgregarProducto.as_view(), name='agregarProducto'),
path('importarProductos', views.ImportarProductos.as_view(), name='importarProductos'),
path('exportarProductos', views.ExportarProductos.as_view(), name='exportarProductos'),
path('editarProducto/<int:p>', views.EditarProducto.as_view(), name='editarProducto'),

path('crearUsuario',views.CrearUsuario.as_view(), name='crearUsuario'),
path('listarUsuarios', views.ListarUsuarios.as_view(), name='listarUsuarios'),

]

