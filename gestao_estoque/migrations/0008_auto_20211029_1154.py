# Generated by Django 3.2.8 on 2021-10-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_estoque', '0007_alter_movimentacao_localizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_material',
            name='criado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lotes',
            name='criado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='criado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='atualizado',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='criado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='atualizado',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='criado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='situacao_material',
            name='criado',
            field=models.DateField(auto_now_add=True),
        ),
    ]
