from django.urls import path
from . import views



urlpatterns = [
    path('', views.agendamento, name='agendamento'),
    path('cancelar_agendamento/<int:id>', views.cancelar_agendamento, name='cancelar_agendamento'),
    path('cadastrar_horario/', views.cadastrar_horario, name='cadastrar_horario'),
    path('cadastrar_data/', views.cadastrar_data, name='cadastrar_data'),
    path('verHorario/', views.verHorario, name='verHorario'),
    path('verDatas/', views.verDatas, name='verDatas'),

]
