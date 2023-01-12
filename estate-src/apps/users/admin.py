from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAadmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class UserAdmin(BaseUserAadmin):
    ordering = []