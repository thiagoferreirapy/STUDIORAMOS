# Generated by Django 4.2.2 on 2023-06-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0006_alter_dataagendamento_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horaagendamento',
            old_name='data_id',
            new_name='data',
        ),
        migrations.AlterField(
            model_name='dataagendamento',
            name='data',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='horaagendamento',
            name='horario',
            field=models.CharField(max_length=50),
        ),
    ]