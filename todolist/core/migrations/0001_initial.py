# Generated by Django 4.2 on 2023-04-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_atividade', models.CharField(max_length=50, verbose_name='Atividade')),
                ('dia_atividade', models.IntegerField(verbose_name='Dia')),
                ('mes_atividade', models.IntegerField(verbose_name='Mês')),
            ],
        ),
    ]
