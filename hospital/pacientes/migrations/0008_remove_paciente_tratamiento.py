# Generated by Django 5.0.6 on 2024-07-10 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0007_alter_paciente_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='tratamiento',
        ),
    ]
