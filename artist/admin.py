from django.contrib import admin
from .models import Details, Product

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'store_name', 'store_email', 'city', 'state', 'country', 'shop_type', 'art_specialization')
    search_fields = ('store_name', 'store_email', 'city', 'state', 'country', 'shop_type', 'art_specialization')
    list_filter = ('shop_type', 'art_specialization', 'country', 'state')
    raw_id_fields = ('user',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'price', 'availability', "ar_model_ref",'upload_date_time')
    search_fields = ('title', 'artist__store_name', 'artist__user__first_name', 'artist__user__last_name')
    list_filter = ('availability', 'artist__art_specialization')
    raw_id_fields = ('artist',)

# Optionally, register the models without custom admin classes
# admin.site.register(Details, DetailsAdmin)
# admin.site.register(Product, ProductAdmin)
