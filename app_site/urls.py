from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('privacidade', views.privacidade, name='privacidade'),
    path('central_atendimento', views.central_atendimento, name='central_atendimento'),
    path('administrador', views.administrador, name='administrador'),
    path('cadastrar_make', views.cadastrar_make, name='cadastrar_make'),
    path('sobremakes/<int:id>', views.sobremakes, name='sobremakes'),
]

