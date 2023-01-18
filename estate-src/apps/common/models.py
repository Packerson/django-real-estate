import uuid

from django.db import models


class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    """
    auto_now_add -automatically set the field when is created
    auto_now - Automatically set the field to now every time the object is saved.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        """if abstract = True, this model will not be save in database,
        but other models can inherit form this model"""

        abstract = True
