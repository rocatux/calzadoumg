# Generated by Django 3.0.8 on 2020-11-23 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCalzado', '0002_registrarfilialmodel_fechacreacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrarfilialmodel',
            name='telefono',
            field=models.IntegerField(max_length=8),
        ),
    ]