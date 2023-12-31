# Generated by Django 4.2.4 on 2023-08-19 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_pets_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id_vacuna', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name_vacuna', models.CharField(max_length=100)),
                ('date_vacuna', models.DateField()),
                ('next_vacuna_date', models.DateField()),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pets')),
            ],
        ),
        migrations.CreateModel(
            name='citaMedica',
            fields=[
                ('id_cita', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('fecha_cita', models.DateField()),
                ('motivo_cita', models.CharField(max_length=100)),
                ('notas_cita', models.TextField()),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pets')),
            ],
        ),
    ]
