# Generated by Django 4.2.2 on 2023-06-22 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maquiagem', models.CharField(max_length=100)),
                ('extra', models.CharField(max_length=50)),
                ('data_horario', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.usuario')),
            ],
        ),
    ]
