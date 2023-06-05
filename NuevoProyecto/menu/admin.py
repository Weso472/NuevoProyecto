from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')          #Para que aparezca al crear un objeto en /admin (solo mostrarlo)
    list_display = ('title', 'created', 'modified')    #Para mas detalles en /admin
    date_hierarchy = 'created'                         #Para filtrar segun la fecha creada