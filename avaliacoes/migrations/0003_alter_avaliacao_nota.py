# Generated by Django 4.1.7 on 2023-07-04 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_alter_avaliacao_options_alter_avaliacao_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
