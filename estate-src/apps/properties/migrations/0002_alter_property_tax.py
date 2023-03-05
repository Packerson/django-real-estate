# Generated by Django 3.2.7 on 2023-03-05 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='tax',
            field=models.DecimalField(decimal_places=6, default=0.15, help_text='15% property tax charged', max_digits=8, verbose_name='Property Tax'),
        ),
    ]
