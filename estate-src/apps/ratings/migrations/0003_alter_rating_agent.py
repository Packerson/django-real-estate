# Generated by Django 3.2.7 on 2023-01-23 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_id'),
        ('ratings', '0002_rating_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_reviews', to='profiles.profile', verbose_name='Agent being rated'),
        ),
    ]
