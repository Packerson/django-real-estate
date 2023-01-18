

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='+48123456789', max_length=30, region=None, verbose_name='Phone Number')),
                ('about_me', models.TextField(default='Say something about yourself', verbose_name='ABout_me')),
                ('license', models.CharField(blank=True, max_length=20, null=True, verbose_name='Real Estate license')),
                ('profile_photo', models.ImageField(default='/profile_default.png', upload_to='', verbose_name='Profile Photo')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=20, verbose_name='Gender')),
                ('country', django_countries.fields.CountryField(default='PL', max_length=2, verbose_name='Country')),
                ('city', models.CharField(default='Radom', max_length=180, verbose_name='City')),
                ('is_buyer', models.BooleanField(default=False, help_text='Are you looking to Buy a Property?', verbose_name='Buyer')),
                ('is_seller', models.BooleanField(default=False, help_text='Are you looking to sell a Property?', verbose_name='Seller')),
                ('is_agent', models.BooleanField(default=False, help_text='Are you an agent?', verbose_name='Agent')),
                ('top_agent', models.BooleanField(default=False, verbose_name='Top Agent')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('num_reviews', models.IntegerField(blank=True, default=0, null=True, verbose_name='Numbers of reviews')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
