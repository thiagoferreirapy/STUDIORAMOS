# Generated by Django 4.2.2 on 2023-06-29 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0011_dataagendamento_horario_alter_dataagendamento_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario10',
        ),
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario2',
        ),
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario3',
        ),
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario4',
        ),
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario5',
        ),
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario6',
        ),
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario7',
        ),
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario8',
        ),
        migrations.RemoveField(
            model_name='horaagendamento',
            name='horario9',
        ),
        migrations.AddField(
            model_name='dataagendamento',
            name='horario10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dataagendamento',
            name='horario2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dataagendamento',
            name='horario3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dataagendamento',
            name='horario4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dataagendamento',
            name='horario5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dataagendamento',
            name='horario6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dataagendamento',
            name='horario7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dataagendamento',
            name='horario8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dataagendamento',
            name='horario9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dataagendamento',
            name='horario',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
