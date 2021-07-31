from django.contrib import admin
from .models import Item, ItemImage
# Register your models here.


class ItemInline(admin.TabularInline):
    model = ItemImage

class PostAdmin(admin.ModelAdmin):
    inlines = [ItemInline, ]

admin.site.register(Item, PostAdmin)