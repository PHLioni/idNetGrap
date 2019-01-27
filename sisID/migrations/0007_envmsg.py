# Generated by Django 2.1.5 on 2019-01-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisID', '0006_teccertificado'),
    ]

    operations = [
        migrations.CreateModel(
            name='envMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regional', models.DecimalField(decimal_places=2, max_digits=5)),
                ('capital', models.DecimalField(decimal_places=2, max_digits=5)),
                ('oeste', models.DecimalField(decimal_places=2, max_digits=5)),
                ('centro', models.DecimalField(decimal_places=2, max_digits=5)),
                ('leste', models.DecimalField(decimal_places=2, max_digits=5)),
                ('santos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sao_jose', models.DecimalField(decimal_places=2, max_digits=5)),
                ('meta', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mes', models.CharField(max_length=15)),
            ],
        ),
    ]
