# Generated by Django 2.1 on 2018-08-26 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookrequest', '0004_auto_20180826_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='state',
            field=models.IntegerField(choices=[(0, 'Enviada'), (1, 'Aceptada'), (2, 'Finalizada')], default=0),
        ),
    ]
