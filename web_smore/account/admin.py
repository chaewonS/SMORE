from django.contrib import admin
from .models import User, UserPaper

# Register your models here.
class UserInline(admin.TabularInline):
    model = UserPaper

class UserAdmin(admin.ModelAdmin):
    inlines = [UserInline, ]

admin.site.register(User, UserAdmin)