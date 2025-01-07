from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    list_per_page = 30
    readonly_fields = ('balance', )

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('title', 'cost', 'size')
    list_filter = ('size', 'cost')
    list_per_page = 20