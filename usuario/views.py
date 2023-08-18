from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from .models import Usuario, ImgUsuario
from hashlib import sha256
from agendamento.models import Agendamento, DataAgendamento, SelectDay, SelectHorarios
from .forms import LoginCaptcha
from django.core.serializers import serialize
import json

def register(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastro_usuario.html', {'status': status})
    
    elif request.method == 'POST':
        
        imagem = request.FILES.get('img_perfil')
        nome = request.POST.get('nome')
        # sobrenome = request.POST.get('sobrenome')
        # cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # data = request.POST.get('data_nascimento')
        # numero = request.POST.get('numero')
        # cidade = request.POST.get('cidade')
        # estado = request.POST.get('estado')
        # cep = request.POST.get('cep')

        #verificar se usuario ja existe
        user = Usuario.objects.filter(email=email).first()
        
        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            return redirect(f'/usuario/register/?status=3')
        
        if len(senha.strip()) <8:
            return redirect(f'/usuario/register/?status=4')
        
        if user:
            #TODO: redirecionar para pagina de cadastro com message do django
            return redirect(f'/usuario/register/?status=5')
        
        try:
            senha_criptografada = sha256(senha.encode()).hexdigest()
            user = Usuario(nome = nome, email = email, senha = senha_criptografada)
            user.save()
            request.session['user'] = user.id
            return redirect(reverse('perfil'))
        except:

            return redirect(f'/usuario/register/?status=6')
    
    
def login(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        
        status = request.GET.get('status')
        return render(request, 'login.html', {'status':status})
    
    elif request.method == 'POST':
        try:
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            nova_senha = sha256(senha.encode()).hexdigest()
            user = Usuario.objects.get(email=email)

            if user:
                if user.senha == nova_senha:
                   
                
                    request.session['user'] = user.id
                    #return redirect(f'home/?id_usuario={request.session["user"]}')
                    return redirect(reverse('perfil'))
                    #return HttpResponse('usuario ou senha invalidos')
                return redirect(f'/usuario/login/?status=1')
            return redirect(f'/usuario/register/?status=2')
        except:
            return redirect(f'/usuario/register/?status=2')
        
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

def perfil(request):
    if request.session.get('user'):
        usuario = Usuario.objects.get(id = request.session['user'])
        agendamentos = Agendamento.objects.filter(usuario = usuario)
        imagem = ImgUsuario.objects.get(img_user=usuario)
        return render(request,'perfil.html', {'agendamentos': agendamentos,'usuario':usuario, 'imagem':imagem})
    else:
        return redirect(reverse('login'))
    


def img_perfil(request, id):
    if request.session.get('user'):
        try:
            usuario_id = Usuario.objects.get(id = request.session['user'])
            if id == 1:
                img_perfil = ImgUsuario.objects.filter(img_user=int(usuario_id.id)).update(img='fotos_perfil/img_perfil1.jpg')
                return redirect(reverse('perfil'))
            if id == 2:
                img_perfil = ImgUsuario.objects.filter(img_user=int(usuario_id.id)).update(img='fotos_perfil/img_perfil2.jpg')
                return redirect(reverse('perfil'))
            if id == 3:
                img_perfil = ImgUsuario.objects.filter(img_user=int(usuario_id.id)).update(img='fotos_perfil/img_perfil3.jpg')
                return redirect(reverse('perfil'))
            if id == 4:
                img_perfil = ImgUsuario.objects.filter(img_user=int(usuario_id.id)).update(img='fotos_perfil/img_perfil4.jpg')
                return redirect(reverse('perfil'))
            if id == 5:
                img_perfil = ImgUsuario.objects.filter(img_user=int(usuario_id.id)).update(img='fotos_perfil/img_perfil5.jpg')
                return redirect(reverse('perfil'))
            if id == 6:
                img_perfil = ImgUsuario.objects.filter(img_user=int(usuario_id.id)).update(img='fotos_perfil/img_perfil6.jpg')
                return redirect(reverse('perfil'))
        except:
            return redirect(reverse('perfil'))
    
    else:
        return redirect(reverse('login'))
    
def foto_perfil(request):
    if request.session.get('user'):
        try:
            usuario = Usuario.objects.get(id = request.session['user'])
            imagem = request.FILES.get('input_file_perfil')
            foto_usuario = ImgUsuario.objects.get(img_user=usuario)
            if foto_usuario:
                foto_usuario.delete()
                foto = ImgUsuario(img = imagem, img_user=usuario)
                foto.save()
            else:

                foto = ImgUsuario(img = imagem, img_user=usuario)
                foto.save()
            #foto_Alterada = ImgUsuario.objects.filter(img_user=usuario)
            # foto_Alterada = ImgUsuario.objects.filter(img_user=usuario).update(img = f'fotos_perfil/{imagem}')
            return redirect(reverse('perfil'))
        except:
            return redirect(reverse('perfil'))
    
    else:
        return redirect(reverse('login'))


def update_user(request, id):
    if request.session.get('user'):
        if request.method == 'GET':
            gera = 123456
            usuario = Usuario.objects.get(id = request.session['user'])
            print('email enviado')

            return render(request, 'update_user.html', {'usuario': usuario, 'id':id})
        
        elif request.method == 'POST':
            gera = 123456
            codigo = request.POST.get('codigo')
            if int(codigo) == gera:
                return redirect(f'/usuario/update/{id}')
            return HttpResponse('teste ok django')
        
    
    return redirect(f'/usuario/register/?status=2')


def update(request, id):
    if request.session.get('user'):
        if request.method == 'GET':
            status = request.GET.get('status')
            print(status)
            if id == 'nome':
                usuario = Usuario.objects.get(id = request.session['user'])
                return render(request, 'update.html', {'usuario': usuario, 'id':id, 'status':status})
            if id == 'email':
                usuario = Usuario.objects.get(id = request.session['user'])
                return render(request, 'update.html', {'usuario': usuario, 'id':id, 'status':status})
            if id == 'senha':
                usuario = Usuario.objects.get(id = request.session['user'])
                return render(request, 'update.html', {'usuario': usuario, 'id':id, 'status':status})
        elif request.method == 'POST':
            
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            confirmar_senha = request.POST.get('confirmar_senha')
            encode_senha = sha256(senha.encode()).hexdigest()


            usuario = Usuario.objects.get(id=request.session['user'])
            emails_users = Usuario.objects.filter(email=email).first()

            if id == 'email':
                if len(email.strip()) == 0:
                    return redirect(f'/usuario/update/{id}/?status=0')
                if email == usuario.email:
                    # return HttpResponse('Email não pode ser igual')
                    return redirect(f'/usuario/update/{id}/?status=1')
                elif emails_users:
                    # return HttpResponse('email já cadastrado')
                    return redirect(f'/usuario/update/{id}/?status=2')
                else:
                    if encode_senha == usuario.senha:
                        usuario = Usuario.objects.filter(id=request.session['user']).update(email=email)
                        return redirect(reverse('perfil'))
                    else:
                        return redirect(f'/usuario/update/{id}/?status=3')
                    
            if id == 'nome':
                if len(nome.strip()) == 0:
                    return redirect(f'/usuario/update/{id}/?status=0')
                if nome == usuario.nome:
                    return redirect(f'/usuario/update/{id}/?status=4')
                else:
                    if encode_senha == usuario.senha:
                        usuario = Usuario.objects.filter(id=request.session['user']).update(nome=nome)
                        return redirect(reverse('perfil'))
                    else:
                        return redirect(f'/usuario/update/{id}/?status=3')
                    
            if id == 'senha':
                if len(senha.strip()) == 0:
                    return redirect(f'/usuario/update/{id}/?status=0')
                if len(senha.strip()) <= 8:
                    return redirect(f'/usuario/update/{id}/?status=7')
                if senha == confirmar_senha:
                    if encode_senha == usuario.senha:
                        return redirect(f'/usuario/update/{id}/?status=6')
                    else:
                        usuario = Usuario.objects.filter(id=request.session['user']).update(senha=encode_senha)
                        return redirect(reverse('perfil'))
                else:
                    return redirect(f'/usuario/update/{id}/?status=5')
    return redirect(f'/usuario/register/?status=2')



def validarAgendamento(request):
    id_data = request.POST.get('data_id')
    id_horario = request.POST.get('horario_id')
    select_days = SelectDay.objects.filter(data_agendada_id=id_data)
    data = DataAgendamento.objects.get(data=id_data)
    select_horario = SelectHorarios.objects.filter(data_agendada_id=data.id)
    
    if int(id_horario) == 1:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=9 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=9).update(descricao='agendado')

        json_agendamento = select_horario.filter(horario=9).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']
        print(data_agendada, 'agendamento ok')
        return redirect('/agendamento/', JsonResponse(data_agendada))
    elif int(id_horario) == 2:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=10 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=10).update(descricao='agendado')

        json_agendamento = select_horario.filter(horario=10).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']
    elif int(id_horario) == 3:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=11 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=11).update(descricao='agendado')

        json_agendamento = select_horario.filter(horario=11).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']

    elif int(id_horario) == 4:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=13 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=13).update(descricao='agendado')
        json_agendamento = select_horario.filter(horario=13).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']
    elif int(id_horario) == 5:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=14 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=14).update(descricao='agendado')
        json_agendamento = select_horario.filter(horario=14).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']
    elif int(id_horario) == 6:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=15 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=15).update(descricao='agendado')
        json_agendamento = select_horario.filter(horario=15).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']
    elif int(id_horario) == 7:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=16 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=16).update(descricao='agendado')
        json_agendamento = select_horario.filter(horario=16).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']
    elif int(id_horario) == 8:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=17 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=17).update(descricao='agendado')
        json_agendamento = select_horario.filter(horario=17).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']
    elif int(id_horario) == 9:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=18 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=18).update(descricao='agendado')
        json_agendamento = select_horario.filter(horario=18).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']
    elif int(id_horario) == 10:
        select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=19 , data_agendada_id=data.id)
        select_data.save()

        horario = select_horario.filter(horario=19).update(descricao='agendado')
        json_agendamento = select_horario.filter(horario=19).all()
        data_agendada = json.loads(serialize('json', json_agendamento))[0]['fields']

    return redirect('/agendamento/', JsonResponse(data_agendada))



















def login_captcha(request):
    if request.method == 'POST':
        form = LoginCaptcha(request.POST)
        if form.is_valid():
            return HttpResponse('ok django recaptcha')
        return render(request, 'login_captcha.html', {'form': form})
    else:
        form = LoginCaptcha()
        return render(request, 'login_captcha.html', {'form': form})