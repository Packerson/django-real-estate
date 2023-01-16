import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

"""
    The PermissionsMixin [Django-doc] is a mixin for Django models. 
    If you add the mixin to one of your models, it will add fields 
    that are specific for objects that have permissions, 
    like is_superuser, groups, and user_permissions. 
    It also provides a set of utility methods to check if 
    the model with this mixin has a given permission (
    for example with has_perm [Django-doc]. 
    A typical model that subclasses this mixin is the User model [Django-doc].
    
    The PermissionRequiredMixin [Django-doc] mixin on the other
     hand is a mixin that provides a convenient way to check 
     if the user that is logged in, has the required permission(s).
"""


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)

    """uuid makes id encrypted"""
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=255,
                                unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_short_name(self):
        return self.username

