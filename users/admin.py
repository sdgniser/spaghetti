from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    pass
#    add_form = CustomUserCreationForm
#    form = CustomUserChangeForm
#    model = CustomUser
#    list_display = ('username', 'score')

#    fieldsets = UserAdmin.fieldsets + (
#                   ('Code Golf', {'fields': ('score',)}),
#                )

admin.site.register(CustomUser, CustomUserAdmin)
