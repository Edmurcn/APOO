# Generated by Django 5.1.2 on 2024-12-20 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_estabelecimento_cnpj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campanha',
            name='cnpj_estabelecimento',
        ),
    ]
