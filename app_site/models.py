from django.db import models

# Create your models here.


class Maquiagem(models.Model):
    nome = models.CharField(max_length=60)
    valor = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class FotoMaquiagens(models.Model):
    img = models.FileField(upload_to='fotos_makes', null=True, blank=True)
    make = models.ForeignKey(Maquiagem, on_delete = models.DO_NOTHING)
    

    def __str__(self) -> str:
        return self.make