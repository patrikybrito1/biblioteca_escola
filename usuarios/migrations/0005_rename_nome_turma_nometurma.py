# Generated by Django 4.1.7 on 2023-03-20 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_rename_nome_turma_turma_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turma',
            old_name='nome',
            new_name='nometurma',
        ),
    ]