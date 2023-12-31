# Generated by Django 4.2.2 on 2023-06-30 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0014_dataagendamento_mes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=50, null=True)),
                ('horario', models.CharField(blank=True, max_length=50, null=True)),
            ],
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
        migrations.AlterField(
            model_name='dataagendamento',
            name='horario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='agendamento.horario'),
            preserve_default=False,
        ),
    ]
