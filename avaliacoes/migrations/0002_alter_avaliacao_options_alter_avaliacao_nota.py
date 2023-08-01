# Generated by Django 4.1.7 on 2023-07-04 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'verbose_name': 'Avaliação', 'verbose_name_plural': 'Avaliações'},
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
    ]
