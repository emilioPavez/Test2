from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = "index"),
    path('postulante/crear', views.crear, name = "crear"),
    path('postulante/eliminar/<int:id>', views.eliminar, name = "eliminar"),
    path('perro/crear', views.crear_perro, name = "crear_perro"),
    path('perro/eliminar/<int:id>', views.eliminar_perro, name = "eliminar_perro"),
    path('perro/editar/<int:id>', views.editar_perro, name = "editar_perro"),
    path('perro/editado/<int:id>', views.editado_perro, name = "editado_perro"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar"),
    path('login/recuperar',views.recuperar,name="recuperar"),
    path('login/recuperado',views.recuperado,name="recuperado")
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

