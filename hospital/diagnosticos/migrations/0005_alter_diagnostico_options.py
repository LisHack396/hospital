# Generated by Django 5.0.6 on 2024-07-07 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0004_alter_diagnostico_paciente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnostico',
            options={'ordering': ['especialidad'], 'permissions': (('es_doctor', 'Puede administrar diagnósticos'),), 'verbose_name': 'diagnostico', 'verbose_name_plural': 'diagnosticos'},
        ),
    ]