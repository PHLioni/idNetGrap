from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import CrtHumanoNetMes, CrtHumano_SPLesteNet, imagemCrt, at1Diario, at1Mes, tecCertificado,\
    envMsg, node, anot, rreip, dispMovel, dispMovelCN, dispAgenda
from .forms import RegionalForm, RegionalForm_SPLeste, fotosCrtForm
from datetime import datetime, date
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import os


dadosfilIn = ''


@login_required
def logout(request):
    return redirect('login')


@login_required
def menu(request):
    return render(request, 'menu.html')


@login_required
def crtHumano(request):
    global dadosfilIn
    dados = CrtHumanoNetMes.objects.all()
    dados_SPLeste = CrtHumano_SPLesteNet.objects.all()
    imagem01 = imagemCrt.objects.all()
    listaData = []
    format = '%m/%d/%Y'
    nvDado = dados_SPLeste.values('data_nota')
    for data in nvDado:
        listaData.append(datetime.strftime(data['data_nota'], format))
    dataFormat = listaData


    return render(request, 'crt_humano.html', {'dados': dados, 'dataFormat': dataFormat, 'dados_SPLeste': dados_SPLeste,
                                               'imagem01': imagem01})


@login_required
def inserir_crtHumano(request):
    form = RegionalForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('crt_humano')
    return render(request, 'inserir_crt_humano.html', {'form': form})

@login_required
def inserir_crtHumano_SPLeste(request):
    form = RegionalForm_SPLeste(request.POST, None)

    if form.is_valid():
        form.save()
        return redirect('crt_humano')
    return render(request, 'inserir_crthumano_spleste.html', {'form': form})



@login_required
def inserir_imagem(request):
    form = fotosCrtForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('crt_humano')
    return render(request, 'inserir_imagem.html', {'form': form})


@login_required
def update_regional(request, id):
    dados = CrtHumanoNetMes.objects.all()
    dado = get_object_or_404(CrtHumanoNetMes, pk=id)
    form = RegionalForm(request.POST or None, instance=dado)

    if form.is_valid():
        form.save()
        return redirect('crt_humano')
    return render(request, 'inserir_crt_humano.html', {'form': form, 'dados': dados})

@login_required
def update_regional_SPLeste(request, id):
    dado = get_object_or_404(CrtHumano_SPLesteNet, pk=id)
    form = RegionalForm_SPLeste(request.POST or None, instance=dado)
    if form.is_valid():
        form.save()
        return redirect('crt_humano')
    return render(request, 'inserir_crt_humano.html', {'form': form})

@login_required
def get_data(request):
    listaDados = []
    dados = CrtHumanoNetMes.objects.all()
    format = '%d/%m/%Y'
    for data in dados:
        listaDados.append(datetime.strftime(data.data_nota, format))
    d = {'data': listaDados}
    return JsonResponse(d)

def deletarImagem01(request, id):
    item = get_object_or_404(imagemCrt, pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('crt_humano')
    return render(request, 'delete_confirm.html', {'item': item})


#AT1
@login_required
def at1(request):
    dados = at1Mes.objects.all()
    dados_SPLeste = at1Diario.objects.all()

    listaData = []
    format = '%m/%d/%Y'
    nvDado = dados_SPLeste.values('data_nota')
    for data in nvDado:
        listaData.append(datetime.strftime(data['data_nota'], format))
    dataFormat = listaData


    return render(request, 'at1.html', {'dados': dados, 'dataFormat': dataFormat, 'dados_SPLeste': dados_SPLeste})

#TEC CERTIFICADO
@login_required
def tCertificado(request):
    dados = tecCertificado.objects.all()
    return render(request, 'tecCertificado.html', {'dados': dados})

#ENV MSG
@login_required
def envioMsg(request):
    dados = envMsg.objects.all()
    return render(request, 'envMsg.html', {'dados': dados})


#NODE CERTIFICADO
@login_required
def nodeCertificado(request):
    dados = node.objects.all()
    return render(request, 'nodeCertificado.html', {'dados': dados})

#ANOT
@login_required
def anotsp(request):
    dados = anot.objects.all()
    return render(request, 'anot.html', {'dados': dados})

#RREIP
@login_required
def rreipsp(request):
    dados = rreip.objects.all()
    return render(request, 'rreip.html', {'dados': dados})

#DISP MOVEL
@login_required
def movel(request):
    dados = dispMovel.objects.all()
    return render(request, 'dispMovel.html', {'dados': dados})

#DISP AGENDA
@login_required
def agenda(request):
    dados = dispAgenda.objects.all()
    return render(request, 'dispAgenda.html', {'dados': dados})

#API REST PARA COSUMO DOS DADOS
class DadosGrafico(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        global dadosfilIn
        listaDados = []
        listaSPlesteDia = []
        listaSantosDia = []
        listaSaoJoseDia = []
        listaLeste = []
        listaSantos = []
        listaSantos2 = []
        listaSaoJose = []
        listaSaoJose2 = []
        listaMes = []
        listaMeta = []

        at1Dados =[]
        at1Leste = []
        at1Santos2 = []
        at1taSaoJose2 = []
        at1MesLista = []
        at1SPlesteDia = []
        at1SantosDia = []
        at1SaoJoseDia = []
        at1Meta = []

        tecLeste =[]
        tecSantos2 =[]
        tecSaoJose2 = []
        tecMesLista = []
        tecMeta = []

        msgLeste = []
        msgSantos2 = []
        msgSaoJose2 = []
        msgMesLista = []
        msgMeta = []

        nodeLeste =[]
        nodeSantos2 = []
        nodeSaoJose2 = []
        nodeMesLista = []
        nodeMeta = []

        anotLeste = []
        anotSantos2 = []
        anotSaoJose2 = []
        anotMesLista = []
        anotMeta = []

        rrLeste = []
        rrSantos2 = []
        rrSaoJose2 = []
        rrMesLista = []
        rrMeta = []

        movel2g = []
        movel3g = []
        movel4g = []
        movelMesLista = []
        movelMeta = []
        movelAll = []

        movelcn12g2 = []
        movelcn12g3 = []
        movelcn12g4 = []
        movelcn13g2 = []
        movelcn13g3 = []
        movelcn13g4 = []

        #CRT ------------------------------------------
        dados_spleste = CrtHumano_SPLesteNet.objects.all()
        format = '%m/%d/%Y'
        for data_spleste in dados_spleste:
            dataGeral = data_spleste.data_nota
            listaDados.append(datetime.strftime(dataGeral, format))
            listaDados.sort()
            listaSantos.append(data_spleste.santos)
            listaSaoJose.append(data_spleste.sao_jose)

        dados = CrtHumanoNetMes.objects.all()[:13]

        for data in dados:
            mes = data.mes

            listaLeste.append(data.leste)
            listaSantos2.append(data.santos)
            listaSaoJose2.append(data.sao_jose)
            listaMes.append(mes)
            listaMeta.append(data.meta)

        dadoDia = CrtHumano_SPLesteNet.objects.all()

        for dataDia in dadoDia:
            listaSPlesteDia.append(dataDia.leste)
            listaSantosDia.append(dataDia.santos)
            listaSaoJoseDia.append(dataDia.sao_jose)

        #AT1----------------------------------------

        dados_spleste = at1Diario.objects.all()
        format = '%m/%d/%Y'
        for data_spleste in dados_spleste:
            dataGeral = data_spleste.data_nota
            at1Dados.append(datetime.strftime(dataGeral, format))
            at1Dados.sort()

        dados = at1Mes.objects.all()[:13]

        for data in dados:
            mes = data.mes

            at1Leste.append(data.leste)
            at1Santos2.append(data.santos)
            at1taSaoJose2.append(data.sao_jose)
            at1MesLista.append(mes)
            at1Meta.append(data.meta)

        dadoDia = at1Diario.objects.all()

        for dataDia in dadoDia:
            at1SPlesteDia.append(dataDia.leste)
            at1SantosDia.append(dataDia.santos)
            at1SaoJoseDia.append(dataDia.sao_jose)

        # TEC CERTIFICADO----------------------------------------
        dados = tecCertificado.objects.all()[:13]

        for data in dados:
            mes = data.mes

            tecLeste.append(data.leste)
            tecSantos2.append(data.santos)
            tecSaoJose2.append(data.sao_jose)
            tecMesLista.append(mes)
            tecMeta.append(data.meta)

        # Env MSG----------------------------------------
        dados = envMsg.objects.all()[:13]

        for data in dados:
            mes = data.mes
            msgLeste.append(data.leste)
            msgSantos2.append(data.santos)
            msgSaoJose2.append(data.sao_jose)
            msgMesLista.append(mes)
            msgMeta.append(data.meta)

        # Env MSG----------------------------------------
        dados = node.objects.all()[:13]

        for data in dados:
            mes = data.mes
            nodeLeste.append(data.leste)
            nodeSantos2.append(data.santos)
            nodeSaoJose2.append(data.sao_jose)
            nodeMesLista.append(mes)
            nodeMeta.append(data.meta)

        # Env MSG----------------------------------------
        dados = anot.objects.all()[ :13 ]

        for data in dados:
            mes = data.mes
            anotLeste.append(data.leste)
            anotSantos2.append(data.santos)
            anotSaoJose2.append(data.sao_jose)
            anotMesLista.append(mes)
            anotMeta.append(data.meta)

        # RREIP----------------------------------------
        dados = rreip.objects.all()[ :13 ]

        for data in dados:
            mes = data.mes
            rrLeste.append(data.leste)
            rrSantos2.append(data.santos)
            rrSaoJose2.append(data.sao_jose)
            rrMesLista.append(mes)
            rrMeta.append(data.meta)

        # dispMovel----------------------------------------
        dados = dispMovel.objects.all()

        for data in dados:
            mes = data.mes
            movel2g.append(data.g2)
            movel3g.append(data.g3)
            movel4g.append(data.g4)
            movelMesLista.append(mes)
            movelMeta.append(data.meta)
        movelAll = (movel2g, movel3g, movel4g)

        dados = dispMovelCN.objects.all()

        for data in dados:
            mes = data.mes
            movelcn12g2.append(data.cn12G2)
            movelcn12g3.append(data.cn12G3)
            movelcn12g4.append(data.cn12G4)
            movelcn13g2.append(data.cn13G2)
            movelcn13g3.append(data.cn13G3)
            movelcn13g4.append(data.cn13G4)
            movelMesLista.append(mes)
            movelMeta.append(data.meta)
        movelAllCN12 = [movelcn12g2, movelcn12g3, movelcn12g4]
        movelAllCN13 = [movelcn13g2, movelcn13g3, movelcn13g4]




        d = {'at1Data': listaDados,
            'mesLeste': listaLeste,
            'mesSantos': listaSantos2,
            'mesSaoJose': listaSaoJose2,
            'listaMes': listaMes,
            'listaSPlesteDia': listaSPlesteDia,
            'listaSantosDia': listaSantosDia,
            'listaSaoJoseDia': listaSaoJoseDia,
            'listaMeta': listaMeta,

            'at1Leste': at1Leste,
            'at1Santos': at1Santos2,
            'at1SaoJose': at1taSaoJose2,
            'at1Mes': at1MesLista,
            'at1SPlesteDia': at1SPlesteDia,
            'at1SantosDia': at1SantosDia,
            'at1SaoJoseDia': at1SaoJoseDia,
            'at1Meta': at1Meta,

            'tecLeste': tecLeste,
            'tecSantos2': tecSantos2,
            'tecSaoJose2': tecSaoJose2,
            'tecMesLista': tecMesLista,
            'tecMeta': tecMeta,

            'msgLeste': msgLeste,
            'msgSantos2': msgSantos2,
            'msgSaoJose2': msgSaoJose2,
            'msgMesLista': msgMesLista,
            'msgMeta': msgMeta,

            'nodeLeste': nodeLeste,
            'nodeSantos2': nodeSantos2,
            'nodeSaoJose2': nodeSaoJose2,
            'nodeMesLista': nodeMesLista,
            'nodeMeta': nodeMeta,

            'anotLeste': anotLeste,
            'anotSantos2': anotSantos2,
            'anotSaoJose2': anotSaoJose2,
            'anotMesLista': anotMesLista,
            'anotMeta': anotMeta,

            'rrLeste': rrLeste,
            'rrSantos2': rrSantos2,
            'rrSaoJose2': rrSaoJose2,
            'rrMesLista': rrMesLista,
            'rrMeta': rrMeta,

            'movel2g': movel2g,
            'movel3g': movel3g,
            'movel4g': movel4g,
            'movelMesLista': movelMesLista,
            'movelMeta': movelMeta,
            'movelAll': movelAll,
            'movelAllCN12': movelAllCN12,
            'movelAllCN13': movelAllCN13,

             }

        return Response(d)

