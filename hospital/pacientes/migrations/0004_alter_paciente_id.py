# Generated by Django 5.0.6 on 2024-07-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_paciente_id_alter_paciente_historia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='id',
            field=models.BigIntegerField(default=True, primary_key=True, serialize=False),
        ),
    ]
