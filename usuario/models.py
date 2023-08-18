from django.db import models




class Usuario(models.Model):
    nome = models.CharField(max_length=60)
    # sobrenome = models.CharField(max_length=100)
    # cpf = models.CharField(max_length=12)  
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    # data_nascimento = models.DateField()
    # numero = models.CharField(max_length=14)
    # cidade = models.CharField(max_length=150)
    # estado = models.CharField(max_length=150)
    # cep = models.CharField(max_length=20)



    def __str__(self) -> str:
        return self.nome
    
class ImgUsuario(models.Model):
    img = models.ImageField(upload_to='fotos_perfil', null=True, blank=True)
    img_user = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)
    

    def __str__(self) -> str:
        return self.img_user