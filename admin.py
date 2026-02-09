from django.contrib import admin
from .models import AvailableProduct,order,employee,department
admin.site.register(AvailableProduct)
admin.site.register(order)
admin.site.register(employee)
admin.site.register(department)

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('av_name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('av_name',)

