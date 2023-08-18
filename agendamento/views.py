from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from .models import Agendamento, Usuario, DataAgendamento, SelectDay, SelectHorarios
import time
from datetime import date
from django.core.serializers import serialize
import json



def agendamento(request):
    if request.session.get('user'):
        if request.method == 'GET':

            return render(request, 'agendamento.html')
        
        elif request.method == 'POST':
            if request.session.get('user'):
                maquiagem = request.POST.get('confi_make')
                extra = request.POST.get('confi_extra')
                data = request.POST.get('confi_data')
                loja = request.POST.get('confi_loja')
                total = request.POST.get('total')
                print(maquiagem, extra, data, loja, total)
                user = Usuario.objects.get(id = request.session['user'])
                id_usuario = request.session['user'] = user.id
                print(user )
                agenda_make = Agendamento(maquiagem=maquiagem,extra=extra,data_horario=data,localizacao=loja,valor=total, usuario=user)
                agenda_make.save()
                time.sleep(5)
                return redirect(reverse('perfil'))
            
            return redirect(reverse('login'))
    return redirect(reverse('login'))


def cancelar_agendamento(request, id):
    usuario = Usuario.objects.get(id=request.session['user'])

    usuario = Agendamento.objects.filter(usuario=request.session['user']).get(id=id).delete()
    return redirect(reverse('perfil'))


def cadastrar_data(request):
    if request.method == 'GET':
        data = DataAgendamento.objects.all()
        semana = date(2023, 7, 1).weekday() + 1
        dia_selecionado = date.today()
        dia_selecionado = str(dia_selecionado).split('-')[-1]
        lista1 = []
        lista2 = []
        lista3 = []
        lista4 = []
        lista5 = []
        lista6 = []
        lista7 = []
        lista8 = []
        lista9 = []
        lista10 = []
        grande_lista = []
        horarios = SelectHorarios.objects.filter(data_agendada_id=1706).all()
        print(horarios[0].descricao)
        contador = 0
        for i in data:#31 dias
            id = i.id
            horarios = SelectHorarios.objects.filter(data_agendada_id=id).all()
            for j in range(len(horarios)):
                print(horarios[j])
                if str(horarios[j].descricao) != 'agendado':
                    lista1.append(j)
            
            
            

        print(lista1)
        return render(request, 'teste.html', {'data': data, 'semana': semana, 'dia_selecionado': dia_selecionado} )
    elif request.method == 'POST':
        data_auto = request.POST.get('data_auto')
        mes = request.POST.get('mes')
        horarios_auto = request.POST.get('horarios_auto')
        
        if data_auto:
                horario = request.POST.get('horario')
    
                for i in range(int(data_auto)):
                    data_cadastrado = DataAgendamento(data=i+1, mes=mes)
                    data_cadastrado.save()
                    return redirect(reverse('cadastrar_data'))
        else:
            data = request.POST.get('data')
            horario = request.POST.get('horario')
            data_cadastrado = DataAgendamento(data=data, mes=mes)
            data_cadastrado.save()
            return redirect(reverse('cadastrar_data'))

def cadastrar_horario(request):
    horario = request.POST.get('horarios')
    data = request.POST.get('data')
    mes = request.POST.get('mes')
    data_id = DataAgendamento.objects.get(data=data)
    print(data_id.id)

    select_horario = SelectHorarios(horario=horario, data_agendada_id=data_id.id)
    select_horario.save()
    return redirect(reverse('cadastrar_data'))

def verHorario(request):
    id_data = request.POST.get('data_id')
    data = DataAgendamento.objects.filter(id=id_data)
    
    horarios = SelectHorarios.objects.filter(data_agendada_id=id_data)

    if int(len(horarios)) == 1:
        data_horarios = json.loads(serialize('json', horarios))[0]['fields']
        return JsonResponse(data_horarios)
    elif int(len(horarios)) == 2:
        print('teste')
        data_horarios1 = json.loads(serialize('json', horarios))[0]['fields']
        print(data_horarios1)
        data_horarios2 = json.loads(serialize('json', horarios))[1]['fields']
        print(data_horarios2)
        return JsonResponse({'horario1': data_horarios1, 'horario2': data_horarios2, 'data':data.data})
    
    elif int(len(horarios)) == 3:
        print('teste')
        data_horarios1 = json.loads(serialize('json', horarios))[0]['fields']
        print(data_horarios1)
        data_horarios2 = json.loads(serialize('json', horarios))[1]['fields']
        print(data_horarios2)
        data_horarios3 = json.loads(serialize('json', horarios))[2]['fields']
        print(data_horarios3)
        return JsonResponse({'horario1': data_horarios1, 'horario2': data_horarios2, 'horario3': data_horarios3, 'data':data.data})
    
    elif int(len(horarios)) == 4:
        print('teste')
        data_horarios1 = json.loads(serialize('json', horarios))[0]['fields']
        print(data_horarios1)
        data_horarios2 = json.loads(serialize('json', horarios))[1]['fields']
        print(data_horarios2)
        data_horarios3 = json.loads(serialize('json', horarios))[2]['fields']
        print(data_horarios3)
        data_horarios4 = json.loads(serialize('json', horarios))[3]['fields']
        print(data_horarios4)
        return JsonResponse({'horario1': data_horarios1, 'horario2': data_horarios2, 'horario3': data_horarios3, 'horario4': data_horarios4, 'data':data.data})
    
    elif int(len(horarios)) == 5:
        print('teste')
        data_horarios1 = json.loads(serialize('json', horarios))[0]['fields']
        print(data_horarios1)
        data_horarios2 = json.loads(serialize('json', horarios))[1]['fields']
        print(data_horarios2)
        data_horarios3 = json.loads(serialize('json', horarios))[2]['fields']
        print(data_horarios3)
        data_horarios4 = json.loads(serialize('json', horarios))[3]['fields']
        print(data_horarios4)
        data_horarios5 = json.loads(serialize('json', horarios))[4]['fields']
        print(data_horarios5)
        return JsonResponse({'horario1': data_horarios1, 'horario2': data_horarios2, 'horario3': data_horarios3, 'horario4': data_horarios4, 'horario5': data_horarios5, 'data':data.data})
    
    elif int(len(horarios)) == 6:
        print('teste')
        data_horarios1 = json.loads(serialize('json', horarios))[0]['fields']
        print(data_horarios1)
        data_horarios2 = json.loads(serialize('json', horarios))[1]['fields']
        print(data_horarios2)
        data_horarios3 = json.loads(serialize('json', horarios))[2]['fields']
        print(data_horarios3)
        data_horarios4 = json.loads(serialize('json', horarios))[3]['fields']
        print(data_horarios4)
        data_horarios5 = json.loads(serialize('json', horarios))[4]['fields']
        print(data_horarios5)
        data_horarios6 = json.loads(serialize('json', horarios))[5]['fields']
        print(data_horarios6)
        return JsonResponse({'horario1': data_horarios1, 'horario2': data_horarios2, 'horario3': data_horarios3, 'horario4': data_horarios4, 'horario5': data_horarios5, 'horario6': data_horarios6, 'data':data.data})
    
    elif int(len(horarios)) == 7:
        print('teste')
        data_horarios1 = json.loads(serialize('json', horarios))[0]['fields']
        print(data_horarios1)
        data_horarios2 = json.loads(serialize('json', horarios))[1]['fields']
        print(data_horarios2)
        data_horarios3 = json.loads(serialize('json', horarios))[2]['fields']
        print(data_horarios3)
        data_horarios4 = json.loads(serialize('json', horarios))[3]['fields']
        print(data_horarios4)
        data_horarios5 = json.loads(serialize('json', horarios))[4]['fields']
        print(data_horarios5)
        data_horarios6 = json.loads(serialize('json', horarios))[5]['fields']
        print(data_horarios6)
        data_horarios7 = json.loads(serialize('json', horarios))[6]['fields']
        print(data_horarios7)
        return JsonResponse({'horario1': data_horarios1, 'horario2': data_horarios2, 'horario3': data_horarios3, 'horario4': data_horarios4, 'horario5': data_horarios5, 'horario6': data_horarios6, 'horario7': data_horarios7, 'data':data.data})
    
    elif int(len(horarios)) == 8:
        print('teste')
        data_horarios1 = json.loads(serialize('json', horarios))[0]['fields']
        print(data_horarios1)
        data_horarios2 = json.loads(serialize('json', horarios))[1]['fields']
        print(data_horarios2)
        data_horarios3 = json.loads(serialize('json', horarios))[2]['fields']
        print(data_horarios3)
        data_horarios4 = json.loads(serialize('json', horarios))[3]['fields']
        print(data_horarios4)
        data_horarios5 = json.loads(serialize('json', horarios))[4]['fields']
        print(data_horarios5)
        data_horarios6 = json.loads(serialize('json', horarios))[5]['fields']
        print(data_horarios6)
        data_horarios7 = json.loads(serialize('json', horarios))[6]['fields']
        print(data_horarios7)
        data_horarios8 = json.loads(serialize('json', horarios))[7]['fields']
        print(data_horarios8)
        return JsonResponse({'horario1': data_horarios1, 'horario2': data_horarios2, 'horario3': data_horarios3, 'horario4': data_horarios4, 'horario5': data_horarios5, 'horario6': data_horarios6, 'horario7': data_horarios7, 'horario8': data_horarios8, 'data':data.data})
    
    elif int(len(horarios)) == 9:
        print('teste')
        data_horarios1 = json.loads(serialize('json', horarios))[0]['fields']
        print(data_horarios1)
        data_horarios2 = json.loads(serialize('json', horarios))[1]['fields']
        print(data_horarios2)
        data_horarios3 = json.loads(serialize('json', horarios))[2]['fields']
        print(data_horarios3)
        data_horarios4 = json.loads(serialize('json', horarios))[3]['fields']
        print(data_horarios4)
        data_horarios5 = json.loads(serialize('json', horarios))[4]['fields']
        print(data_horarios5)
        data_horarios6 = json.loads(serialize('json', horarios))[5]['fields']
        print(data_horarios6)
        data_horarios7 = json.loads(serialize('json', horarios))[6]['fields']
        print(data_horarios7)
        data_horarios8 = json.loads(serialize('json', horarios))[7]['fields']
        print(data_horarios8)
        data_horarios9 = json.loads(serialize('json', horarios))[8]['fields']
        print(data_horarios9)
        return JsonResponse({'horario1': data_horarios1, 'horario2': data_horarios2, 'horario3': data_horarios3, 'horario4': data_horarios4, 'horario5': data_horarios5, 'horario6': data_horarios6, 'horario7': data_horarios7, 'horario8': data_horarios8, 'horario9': data_horarios9, 'data':data.data})
    elif int(len(horarios)) == 10:
        print('teste')
        data_horarios1 = json.loads(serialize('json', horarios))[0]['fields']
        print(data_horarios1)
        data_horarios2 = json.loads(serialize('json', horarios))[1]['fields']
        print(data_horarios2)
        data_horarios3 = json.loads(serialize('json', horarios))[2]['fields']
        print(data_horarios3)
        data_horarios4 = json.loads(serialize('json', horarios))[3]['fields']
        print(data_horarios4)
        data_horarios5 = json.loads(serialize('json', horarios))[4]['fields']
        print(data_horarios5)
        data_horarios6 = json.loads(serialize('json', horarios))[5]['fields']
        print(data_horarios6)
        data_horarios7 = json.loads(serialize('json', horarios))[6]['fields']
        print(data_horarios7)
        data_horarios8 = json.loads(serialize('json', horarios))[7]['fields']
        print(data_horarios8)
        data_horarios9 = json.loads(serialize('json', horarios))[8]['fields']
        print(data_horarios9)
        data_horarios10 = json.loads(serialize('json', horarios))[9]['fields']
        print(data_horarios10)
        data = DataAgendamento.objects.get(id = data_horarios1['data_agendada'])
        print(data.data , 'teste')
        return JsonResponse({'horario1': data_horarios1, 'horario2': data_horarios2, 'horario3': data_horarios3, 'horario4': data_horarios4, 'horario5': data_horarios5, 'horario6': data_horarios6, 'horario7': data_horarios7, 'horario8': data_horarios8, 'horario9': data_horarios9, 'horario10': data_horarios10, 'data':data.data})
    
def verDatas(request):
    id_data = request.POST.get('data_id')

    data = DataAgendamento.objects.all()
    dias_selecionados = SelectDay.objects.all()

    data_disponivel = json.loads(serialize('json', data))[0]['fields']
    dias_agendados = json.loads(serialize('json', dias_selecionados))[0]['fields']
    # print(data_horarios)
    print(data_disponivel, dias_agendados)
    return JsonResponse({'datas_disponiveis': data_disponivel, 'horarios_agendados': dias_agendados})


# def validarAgendamento(request):
#     id_data = request.POST.get('data_id')
#     id_horario = request.POST.get('horario_id')
#     print(id_data, id_horario)
#     data = DataAgendamento.objects.get(data=id_data)

#     if int(id_horario) == 1:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=9 , data_agendada_id=data.id)
#         select_data.save()
#     elif int(id_horario) == 2:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=10 , data_agendada_id=data.id)
#         select_data.save()
#     elif int(id_horario) == 3:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=11 , data_agendada_id=data.id)
#         select_data.save()
#     elif int(id_horario) == 4:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=13 , data_agendada_id=data.id)
#         select_data.save()
#     elif int(id_horario) == 5:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=14 , data_agendada_id=data.id)
#         select_data.save()
#     elif int(id_horario) == 6:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=15 , data_agendada_id=data.id)
#         select_data.save()
#     elif int(id_horario) == 7:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=16 , data_agendada_id=data.id)
#         select_data.save()
#     elif int(id_horario) == 8:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=17 , data_agendada_id=data.id)
#         select_data.save()
#     elif int(id_horario) == 9:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=18 , data_agendada_id=data.id)
#         select_data.save()
#     elif int(id_horario) == 10:
#         select_data = SelectDay(dia=id_data, descricao= 'agendado', horario=19 , data_agendada_id=data.id)
#         select_data.save()

#     data_agendada = SelectDay.objects.filter(dia=int(id_data))
#     print(data_agendada)
#     # data_agendada = json.loads(serialize('json', data_agendada))[0]['fields']
#     # print(data_agendada)
#     # #data = DataAgendamento.objects.filter(data=id_data).update(descricao='agendado')
#     # return JsonResponse(data_agendada)