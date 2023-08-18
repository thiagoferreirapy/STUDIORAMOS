from django.db import models
from usuario.models import Usuario



    







class DataAgendamento(models.Model):
    data = models.CharField(max_length=50)
    mes = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.data

class SelectDay(models.Model):
    
    dia = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50, null=True, blank=True)
    horario = models.CharField(max_length=50)
    data_agendada = models.ForeignKey(DataAgendamento, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.dia
    
class SelectHorarios(models.Model):
    
    horario = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50, null=True, blank=True)
    data_agendada = models.ForeignKey(DataAgendamento, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.horario



class Agendamento(models.Model):
    maquiagem = models.CharField(max_length=100)
    extra = models.CharField(max_length=50)
    data_horario = models.ForeignKey(DataAgendamento, on_delete = models.DO_NOTHING)
    localizacao = models.CharField(max_length=100)
    valor = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.maquiagem