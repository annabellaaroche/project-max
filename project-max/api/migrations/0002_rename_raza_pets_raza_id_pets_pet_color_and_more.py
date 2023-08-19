# Generated by Django 4.2.4 on 2023-08-19 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pets',
            old_name='raza',
            new_name='raza_id',
        ),
        migrations.AddField(
            model_name='pets',
            name='pet_color',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pets',
            name='pet_gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pets',
            name='pet_size_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.petsize'),
            preserve_default=False,
        ),
    ]
