# Generated by Django 4.2.2 on 2023-06-28 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0004_remove_dataagendamento_horario_horaagendamento_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horaagendamento',
            old_name='data',
            new_name='data_id',
        ),
        migrations.AlterField(
            model_name='dataagendamento',
            name='data',
            field=models.CharField(max_length=31),
        ),
    ]
