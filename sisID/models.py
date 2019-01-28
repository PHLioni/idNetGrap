from django.db import models
from datetime import datetime

formato = '%Y-%m-%d'

class CrtHumanoNetMes(models.Model):
    regional = models.DecimalField(max_digits=5, decimal_places=2)
    capital = models.DecimalField(max_digits=5, decimal_places=2)
    oeste = models.DecimalField(max_digits=5, decimal_places=2)
    centro = models.DecimalField(max_digits=5, decimal_places=2)
    leste = models.DecimalField(max_digits=5, decimal_places=2)
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    sao_jose = models.DecimalField(max_digits=5, decimal_places=2)
    meta = models.DecimalField(max_digits=5, decimal_places=2)
    mes = models.CharField(max_length=15)


    def save(self, force_insert=False, force_update=False):
        self.mes = self.mes.upper()

        super(CrtHumanoNetMes, self).save(force_insert, force_update)

    def __str__(self):
        return 'Mês: ' + ' ' + str(self.mes)

class CrtHumano_SPLesteNet(models.Model):
    leste = models.DecimalField(max_digits=5, decimal_places=2)
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    sao_jose = models.DecimalField(max_digits=5, decimal_places=2)
    data_nota = models.DateField('Data Nota')


    def save(self, force_insert=False, force_update=False):
        self.data_nota = datetime.strftime(self.data_nota, formato)
        super(CrtHumano_SPLesteNet, self).save(force_insert, force_update)

    def __str__(self):
        return 'Data: ' + ' ' + str(self.data_nota)

class imagemCrt(models.Model):
    mes = models.CharField(max_length=15)
    photo01 = models.ImageField(upload_to='imagens', null=True, blank=True)
    photo02 = models.ImageField(upload_to='imagens', null=True, blank=True)


    def save(self, force_insert=False, force_update=False):


        super(imagemCrt, self).save(force_insert, force_update)

    def __str__(self):
        return 'Imagem ' + ' ' + str(self.mes)

# AT1-----------------------------------------------------------------

class at1Mes(models.Model):
    regional = models.DecimalField(max_digits=5, decimal_places=2)
    capital = models.DecimalField(max_digits=5, decimal_places=2)
    oeste = models.DecimalField(max_digits=5, decimal_places=2)
    centro = models.DecimalField(max_digits=5, decimal_places=2)
    leste = models.DecimalField(max_digits=5, decimal_places=2)
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    sao_jose = models.DecimalField(max_digits=5, decimal_places=2)
    meta = models.DecimalField(max_digits=5, decimal_places=2)
    mes = models.CharField(max_length=15)


    def save(self, force_insert=False, force_update=False):
        self.mes = self.mes.upper()

        super(at1Mes, self).save(force_insert, force_update)

    def __str__(self):
        return 'Mês: ' + ' ' + str(self.mes)


class at1Diario(models.Model):
    leste = models.DecimalField(max_digits=5, decimal_places=2)
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    sao_jose = models.DecimalField(max_digits=5, decimal_places=2)
    data_nota = models.DateField('Data Nota')


    def save(self, force_insert=False, force_update=False):
        self.data_nota = datetime.strftime(self.data_nota, formato)
        super(at1Diario, self).save(force_insert, force_update)

    def __str__(self):
        return 'Data: ' + ' ' + str(self.data_nota)


#TEC CERTIFICADO ------------------------

class tecCertificado(models.Model):
    regional = models.DecimalField(max_digits=5, decimal_places=2)
    capital = models.DecimalField(max_digits=5, decimal_places=2)
    oeste = models.DecimalField(max_digits=5, decimal_places=2)
    centro = models.DecimalField(max_digits=5, decimal_places=2)
    leste = models.DecimalField(max_digits=5, decimal_places=2)
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    sao_jose = models.DecimalField(max_digits=5, decimal_places=2)
    meta = models.DecimalField(max_digits=5, decimal_places=2)
    mes = models.CharField(max_length=15)


    def save(self, force_insert=False, force_update=False):
        self.mes = self.mes.upper()

        super(tecCertificado, self).save(force_insert, force_update)

    def __str__(self):
        return 'Mês: ' + ' ' + str(self.mes)

#ENVIO DE MENSAGEM ------------------------

class envMsg(models.Model):
    regional = models.DecimalField(max_digits=5, decimal_places=2)
    capital = models.DecimalField(max_digits=5, decimal_places=2)
    oeste = models.DecimalField(max_digits=5, decimal_places=2)
    centro = models.DecimalField(max_digits=5, decimal_places=2)
    leste = models.DecimalField(max_digits=5, decimal_places=2)
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    sao_jose = models.DecimalField(max_digits=5, decimal_places=2)
    meta = models.DecimalField(max_digits=5, decimal_places=2)
    mes = models.CharField(max_length=15)


    def save(self, force_insert=False, force_update=False):
        self.mes = self.mes.upper()

        super(envMsg, self).save(force_insert, force_update)

    def __str__(self):
        return 'Mês: ' + ' ' + str(self.mes)


#NODE CERTIFICADO ------------------------

class node(models.Model):
    regional = models.DecimalField(max_digits=5, decimal_places=2)
    capital = models.DecimalField(max_digits=5, decimal_places=2)
    oeste = models.DecimalField(max_digits=5, decimal_places=2)
    centro = models.DecimalField(max_digits=5, decimal_places=2)
    leste = models.DecimalField(max_digits=5, decimal_places=2)
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    sao_jose = models.DecimalField(max_digits=5, decimal_places=2)
    meta = models.DecimalField(max_digits=5, decimal_places=2)
    mes = models.CharField(max_length=15)


    def save(self, force_insert=False, force_update=False):
        self.mes = self.mes.upper()

        super(node, self).save(force_insert, force_update)

    def __str__(self):
        return 'Mês: ' + ' ' + str(self.mes)


#ANOT ------------------------

class anot(models.Model):
    regional = models.DecimalField(max_digits=5, decimal_places=2)
    capital = models.DecimalField(max_digits=5, decimal_places=2)
    oeste = models.DecimalField(max_digits=5, decimal_places=2)
    centro = models.DecimalField(max_digits=5, decimal_places=2)
    leste = models.DecimalField(max_digits=5, decimal_places=2)
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    sao_jose = models.DecimalField(max_digits=5, decimal_places=2)
    meta = models.DecimalField(max_digits=5, decimal_places=2)
    mes = models.CharField(max_length=15)


    def save(self, force_insert=False, force_update=False):
        self.mes = self.mes.upper()

        super(anot, self).save(force_insert, force_update)

    def __str__(self):
        return 'Mês: ' + ' ' + str(self.mes)

#RREIP ------------------------

class rreip(models.Model):
    regional = models.DecimalField(max_digits=5, decimal_places=2)
    capital = models.DecimalField(max_digits=5, decimal_places=2)
    oeste = models.DecimalField(max_digits=5, decimal_places=2)
    centro = models.DecimalField(max_digits=5, decimal_places=2)
    leste = models.DecimalField(max_digits=5, decimal_places=2)
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    sao_jose = models.DecimalField(max_digits=5, decimal_places=2)
    meta = models.DecimalField(max_digits=5, decimal_places=2)
    mes = models.CharField(max_length=15)


    def save(self, force_insert=False, force_update=False):
        self.mes = self.mes.upper()

        super(rreip, self).save(force_insert, force_update)

    def __str__(self):
        return 'Mês: ' + ' ' + str(self.mes)

#DISP MOVEL---------------------------------------------
class dispMovel(models.Model):
    g2 = models.DecimalField(max_digits=5, decimal_places=2)
    g3 = models.DecimalField(max_digits=5, decimal_places=2)
    g4 = models.DecimalField(max_digits=5, decimal_places=2)
    meta = models.DecimalField(max_digits=5, decimal_places=2)
    mes = models.CharField(max_length=15)


    def save(self, force_insert=False, force_update=False):
        self.mes = self.mes.upper()

        super(dispMovel, self).save(force_insert, force_update)

    def __str__(self):
        return 'Mês: ' + ' ' + str(self.mes)


#DISP MOVEL---------------------------------------------
class dispMovelCN(models.Model):
    cn12G2 = models.DecimalField(max_digits=5, decimal_places=2)
    cn12G3 = models.DecimalField(max_digits=5, decimal_places=2)
    cn12G4 = models.DecimalField(max_digits=5, decimal_places=2)
    cn13G2 = models.DecimalField(max_digits=5, decimal_places=2)
    cn13G3 = models.DecimalField(max_digits=5, decimal_places=2)
    cn13G4 = models.DecimalField(max_digits=5, decimal_places=2)
    meta = models.DecimalField(max_digits=5, decimal_places=2)
    mes = models.CharField(max_length=15)


    def save(self, force_insert=False, force_update=False):
        self.mes = self.mes.upper()

        super(dispMovelCN, self).save(force_insert, force_update)

    def __str__(self):
        return 'Mês: ' + ' ' + str(self.mes)


#DISP AGENDA--------------------------------------------------

class dispAgendanet(models.Model):
    santos = models.DecimalField(max_digits=5, decimal_places=2)
    bertioga = models.DecimalField(max_digits=5, decimal_places=2)
    cubatao = models.DecimalField(max_digits=5, decimal_places=2)
    guaruja = models.DecimalField(max_digits=5, decimal_places=2)
    praiaGrande = models.DecimalField(max_digits=5, decimal_places=2)
    saoVicente = models.DecimalField(max_digits=5, decimal_places=2)
    saoJose = models.DecimalField(max_digits=5, decimal_places=2)
    jacarei = models.DecimalField(max_digits=5, decimal_places=2)
    cacapava = models.DecimalField(max_digits=5, decimal_places=2)
    pinda = models.DecimalField(max_digits=5, decimal_places=2)
    taubate = models.DecimalField(max_digits=5, decimal_places=2)
    vale = models.DecimalField(max_digits=5, decimal_places=2)
    tremembe = models.DecimalField(max_digits=5, decimal_places=2)
    mongagua = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.CharField(max_length=15)

    def save(self, force_insert=False, force_update=False):

        super(dispAgenda, self).save(force_insert, force_update)

    def __str__(self):
        return 'Data: ' + ' ' + str(self.data)


