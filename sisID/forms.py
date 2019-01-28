from django.forms import ModelForm
from .models import CrtHumanoNetMes, CrtHumano_SPLesteNet, imagemCrt, \
    at1Diario, at1Mes, tecCertificado, envMsg, node, anot, rreip, dispMovel,dispMovelCN, dispAgendanet



class RegionalForm(ModelForm):
    class Meta:
        model = CrtHumanoNetMes
        fields = ['regional', 'capital', 'oeste', 'centro', 'leste','santos', 'sao_jose', 'meta', 'mes']

class RegionalForm_SPLeste(ModelForm):
    class Meta:
        model = CrtHumano_SPLesteNet
        fields = ['leste', 'santos', 'sao_jose', 'data_nota']


class fotosCrtForm(ModelForm):
    class Meta:
        model = imagemCrt
        fields = ['mes', 'photo01', 'photo02']

# AT1 ----------------------------------------------------------------

class at1MensalForm(ModelForm):
    class Meta:
        model = at1Mes
        fields = ['regional', 'capital', 'oeste', 'centro', 'leste','santos', 'sao_jose', 'meta', 'mes']

class at1DiarioForm(ModelForm):
    class Meta:
        model = at1Diario
        fields = ['leste', 'santos', 'sao_jose', 'data_nota']

# TEC CERTIFICADO ----------------------------------------------------------------

class at1MensalForm(ModelForm):
    class Meta:
        model = tecCertificado
        fields = ['regional', 'capital', 'oeste', 'centro', 'leste', 'santos', 'sao_jose', 'meta', 'mes']


# ENVIO DE MSG ----------------------------------------------------------------

class envMsgForm(ModelForm):
    class Meta:
        model = envMsg
        fields = ['regional', 'capital', 'oeste', 'centro', 'leste', 'santos', 'sao_jose', 'meta', 'mes']

# NODE CERTIFICADO ----------------------------------------------------------------

class nodeForm(ModelForm):
    class Meta:
        model = node
        fields = ['regional', 'capital', 'oeste', 'centro', 'leste', 'santos', 'sao_jose', 'meta', 'mes']

# ANOT ----------------------------------------------------------------

class anotForm(ModelForm):
    class Meta:
        model = anot
        fields = ['regional', 'capital', 'oeste', 'centro', 'leste', 'santos', 'sao_jose', 'meta', 'mes']

# RREIP ----------------------------------------------------------------

class rreipForm(ModelForm):
    class Meta:
        model = rreip
        fields = ['regional', 'capital', 'oeste', 'centro', 'leste', 'santos', 'sao_jose', 'meta', 'mes']

# DISP MOVEL ----------------------------------------------------------------

class movelForm(ModelForm):
    class Meta:
        model = dispMovel
        fields = ['g2', 'g3', 'g4', 'meta', 'mes']


class movelCNForm(ModelForm):
    class Meta:
        model = dispMovelCN
        fields = ['cn12G2', 'cn12G3', 'cn12G4', 'cn13G2', 'cn13G3', 'cn13G4', 'meta', 'mes']


#DISP AGENDA-------------------------------------------------------------------

class agendaForm(ModelForm):
    class Meta:
        model = dispAgendanet
        fields = ['santos', 'bertioga', 'cubatao', 'guaruja', 'praiaGrande', 'saoVicente', 'saoJose', 'jacarei',
                  'cacapava', 'pinda', 'taubate', 'vale', 'tremembe', 'mongagua']