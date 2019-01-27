# Generated by Django 2.1.5 on 2019-01-27 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisID', '0008_node'),
    ]

    operations = [
        migrations.CreateModel(
            name='anot',
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
