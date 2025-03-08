from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1  # Number of extra forms to show for image uploads

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'property_type', 'location', 'created_at', 'updated_at']
    search_fields = ['title', 'location', 'price']
    list_filter = ['property_type']
    inlines = [PropertyImageInline]

admin.site.register(Property, PropertyAdmin)
