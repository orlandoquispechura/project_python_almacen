from django.contrib import admin
from .models import Category
from .models import Product
from .models import Customer
from .models import Sale
from .models import DetailSale


# Register your models here. Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    ordering = ["id"]
    search_fields = ["name"]
    list_filter = ["name"]


admin.site.register(Category, CategoryAdmin)


# Register your models here. Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "stock", "price", "status", "category")
    ordering = ["id"]
    search_fields = ["name"]
    list_filter = ["status"]
admin.site.register(Product, ProductAdmin)


# Register your models here. Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "dni", "address", "phone", "email")
    ordering = ["id"]
    search_fields = ["name", "dni"]
    list_filter = ["name"]
admin.site.register(Customer, CustomerAdmin)

# REgister your models here. DetailSale
class DetailSale(admin.TabularInline):
    model = DetailSale

# REgister your models here. Sale
class SaleAdmin(admin.ModelAdmin):
    list_display = ("date_sale", "total", "customer")
    inlines = (DetailSale,)     
      
admin.site.register(Sale, SaleAdmin)


