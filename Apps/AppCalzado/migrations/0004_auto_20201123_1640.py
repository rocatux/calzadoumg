# Generated by Django 3.0.8 on 2020-11-23 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCalzado', '0003_auto_20201123_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrarfilialmodel',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
