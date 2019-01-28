# Generated by Django 2.1.5 on 2019-01-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisID', '0013_dispagenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='dispAgendanet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('santos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bertioga', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cubatao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('guaruja', models.DecimalField(decimal_places=2, max_digits=5)),
                ('praiaGrande', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saoVicente', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saoJose', models.DecimalField(decimal_places=2, max_digits=5)),
                ('jacarei', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cacapava', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pinda', models.DecimalField(decimal_places=2, max_digits=5)),
                ('taubate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vale', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tremembe', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mongagua', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='dispAgenda',
        ),
    ]
