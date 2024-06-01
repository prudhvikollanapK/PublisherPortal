from django.contrib import admin
from .models import ContentOffering, Transaction

@admin.register(ContentOffering)
class ContentOfferingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'document')
    search_fields = ('title', 'description')
    list_filter = ('price',)
    ordering = ('title',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    filter_horizontal = ('content_offerings',)
