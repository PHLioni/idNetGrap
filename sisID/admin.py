from django.contrib import admin
from .models import CrtHumanoNetMes, CrtHumano_SPLesteNet, imagemCrt, at1Diario, at1Mes, \
    tecCertificado, envMsg, node, anot, rreip, dispMovel, dispMovelCN, dispAgendanet



class at1MesAdmin(admin.ModelAdmin):
    list_display = ['mes', 'regional', 'capital', 'oeste', 'centro', 'leste','santos', 'sao_jose', 'meta']

class at1DiarioAdmin(admin.ModelAdmin):
    list_display = ['leste', 'santos', 'sao_jose']

admin.site.register(at1Mes, at1MesAdmin)
admin.site.register(at1Diario, at1DiarioAdmin)
admin.site.register(CrtHumanoNetMes)
admin.site.register(CrtHumano_SPLesteNet)
admin.site.register(imagemCrt)
admin.site.register(tecCertificado)
admin.site.register(envMsg)
admin.site.register(node)
admin.site.register(anot)
admin.site.register(rreip)
admin.site.register(dispMovel)
admin.site.register(dispMovelCN)
admin.site.register(dispAgendanet)





