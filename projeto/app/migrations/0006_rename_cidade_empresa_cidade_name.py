# Generated by Django 4.0.4 on 2022-06-01 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_empresa_cidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='cidade',
            new_name='cidade_name',
        ),
    ]
