# Generated by Django 5.0.6 on 2024-07-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0002_grupo_pacientes'),
        ('pacientes', '0002_alter_paciente_sexo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='pacientes',
        ),
        migrations.AddField(
            model_name='grupo',
            name='pacientes',
            field=models.ManyToManyField(blank=True, null=True, related_name='pacientes', to='pacientes.paciente'),
        ),
    ]
