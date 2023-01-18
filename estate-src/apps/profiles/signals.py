import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from real_estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)

"""
    when the User model is saved, a signal is fired called 
    create_profile which creates a Profile instance with 
    a foreign key pointing to the instance of the user. 
    The other method save_profile just saves the instance.
    
    need to write method in apps.py,
    later register in admin.py
    
    More about signals:
    https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/
"""


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s profile created")
