# Generated by Django 4.2.2 on 2023-07-01 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0019_selecthorarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario10',
        ),
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario2',
        ),
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario3',
        ),
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario4',
        ),
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario5',
        ),
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario6',
        ),
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario7',
        ),
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario8',
        ),
        migrations.RemoveField(
            model_name='dataagendamento',
            name='horario9',
        ),
    ]
