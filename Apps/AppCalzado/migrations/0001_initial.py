# Generated by Django 3.0.8 on 2020-11-26 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrarFilialModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('telefono', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('tipo', models.CharField(choices=[('Fabricadora', 'Fabricadora'), ('Distribuidora y Ventas', 'Distribuidora y Ventas')], default='Fabricadora', max_length=22)),
                ('direccion', models.CharField(max_length=200)),
                ('fechaCreacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistrarTrabajadoresModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.PositiveIntegerField(blank=True, null=True)),
                ('celular', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('tipo', models.CharField(choices=[('Trabajador Base', 'Trabajador Base'), ('Directivo', 'Directivo'), ('Presidente Directivo', 'Presidente Directivo')], default='Trabajador Base', max_length=30)),
                ('dpi', models.PositiveIntegerField()),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fechaCreacion', models.DateField()),
                ('filialBase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCalzado.RegistrarFilialModel')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroExtrasModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('cantidadHorasExtras', models.IntegerField()),
                ('filialExtras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCalzado.RegistrarFilialModel')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCalzado.RegistrarTrabajadoresModel')),
            ],
        ),
    ]
