from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')
    list_filter = ('status', ) #what you're going to filter by
    search_fields = ('meal', 'descirption') #what you're going to search by 

admin.site.register(Item, MenuItemAdmin)


