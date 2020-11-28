# Generated by Django 3.0.8 on 2020-11-28 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCalzado', '0002_auto_20201126_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculoSueldoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horasTrabajadasMes', models.PositiveIntegerField()),
                ('sueldoHora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horasExtrasMes', models.PositiveIntegerField()),
                ('totalPagar', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('horasExtras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCalzado.RegistroExtrasModel')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCalzado.RegistrarTrabajadoresModel')),
            ],
        ),
    ]
