# Generated by Django 4.2.2 on 2023-06-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0013_selectday_delete_horaagendamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataagendamento',
            name='mes',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
