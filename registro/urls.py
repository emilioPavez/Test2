from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('registro/', views.registro, name = "registro"),
    path('registro/crear', views.crear, name = "crear"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar")
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

