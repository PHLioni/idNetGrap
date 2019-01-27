from django.urls import path
from .views import logout
from .views import crtHumano
from .views import inserir_crtHumano, inserir_crtHumano_SPLeste, update_regional, update_regional_SPLeste, at1, anotsp, rreipsp, agenda
from .views import menu, get_data, DadosGrafico, deletarImagem01, inserir_imagem, tCertificado, envioMsg, nodeCertificado, movel


urlpatterns = [

    path('logout/', logout, name='logout'),
    path('menu', menu, name='menu'),

    path('update_regional/<int:id>', update_regional, name="update_regional"),
    path('update_regional_SPLeste/<int:id>', update_regional_SPLeste, name="update_regional_SPLeste"),
    #PAGINAS
    path('crt_humano', crtHumano, name='crt_humano'),
    path('at1', at1, name='at1'),
    path('tecCertificado', tCertificado, name='tecCertificado'),
    path('envMsg', envioMsg, name='envMsg'),
    path('nodeCertificado', nodeCertificado, name='nodeCertificado'),
    path('anot', anotsp, name='anot'),
    path('rreip', rreipsp, name='rreip'),
    path('dispMovel', movel, name='dispMovel'),
    path('dispAgenda', agenda, name='dispAgenda'),


    path('inserir_crt_humano', inserir_crtHumano, name='inserir_crt_humano'),
    path('inserir_crthumano_spleste', inserir_crtHumano_SPLeste, name='inserir_crthumano_SPLeste'),
    path('inserir_imagem', inserir_imagem, name='inserir_imagem'),
    path('dadosGrafi', DadosGrafico, name='DadosGrafico'),

    path('api/data', get_data, name='api-data'),
    path('api/chart/data', DadosGrafico.as_view()),
    path('deletarImagem01/<int:id>', deletarImagem01, name='deletarImagem01'),
]