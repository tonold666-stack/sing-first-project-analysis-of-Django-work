from django.contrib import admin

from goods.models import Categories, Products

# админка переделанна на более расширенную.
# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}