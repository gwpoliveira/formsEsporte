# Generated by Django 5.1.1 on 2024-09-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioesporte',
            name='unidade',
            field=models.CharField(choices=[('Primavera', 'Magister Primavera')], max_length=20),
        ),
    ]
