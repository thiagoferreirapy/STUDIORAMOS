from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login_captcha/', views.login_captcha, name='login_captcha'),
    path('perfil/', views.perfil, name='perfil'),
    path('update_user/<str:id>', views.update_user, name='update_user'),
    path('update/<str:id>/', views.update, name='update'),
    path('img_perfil/<int:id>', views.img_perfil, name='img_perfil'),
    path('foto_perfil', views.foto_perfil, name='foto_perfil'),
    path('logout', views.logout, name='logout'),
    path('validarAgendamento/', views.validarAgendamento, name='validarAgendamento'),
]