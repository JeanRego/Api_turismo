# Generated by Django 4.1.7 on 2023-07-04 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pontoturistico',
            options={'verbose_name': 'Ponto Turistico', 'verbose_name_plural': 'Pontos Turisticos'},
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]
