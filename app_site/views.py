from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import FotoMaquiagens, Maquiagem

# Create your views here.

def home(request):
    # if request.session.get('user'):

    #     return render(request, 'home.html')
    
    # return redirect(reverse('login'))
    return render(request, 'home.html')

def privacidade(request):
    return render(request, 'privacidade.html')

def central_atendimento(request):
    return render(request, 'central.html')

def administrador(request):
    if request.method == 'GET':
        
        return render(request, 'administrador.html')
    
    elif request.method == 'POST':
        id_makes = request.POST.get('id_make')
        imagem = request.FILES.get('img_make')
        maquiagem = Maquiagem.objects.get(id=id_makes)
        foto_makes = FotoMaquiagens(img=imagem, make=maquiagem)
        foto_makes.save()
        
        return HttpResponse('teste')
    

def cadastrar_make(request):
    nome = request.POST.get('nome')
    valor = request.POST.get('valor')
    maquiagem = Maquiagem(nome=nome,valor=valor)
    maquiagem.save()
    return HttpResponse('make cadastrada')

def sobremakes(request, id):
    if request.session.get('user'):
        try:
            make = Maquiagem.objects.get(id=id)
            if make:
                make = Maquiagem.objects.get(id=id)
                fotos = FotoMaquiagens.objects.filter(make=id)
            
                return render(request,'sobremakes.html' ,{'foto':fotos,'make':make})
        except:
            return redirect(reverse('home'))
    else:
        return redirect(reverse('login'))




def not_found(request, exception):
    return render(request, 'not_found.html')