from atexit import register
from django.contrib import admin

from onlinefood.models import Item

# Register your models here.
admin.site.site_header = "Online Food"
from .models import Item, CartItems

class itemAdmin(admin.ModelAdmin):
    list_display=('title','price')
    prepopulated_fields = {'slug': ('title',)}


class cartitemsAdmin(admin.ModelAdmin):
    list_display=('item','quantity','status')    




admin.site.register(Item, itemAdmin)
admin.site.register(CartItems,cartitemsAdmin)
