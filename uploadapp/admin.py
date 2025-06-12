from django.contrib import admin
from .models import CustomUser, Document
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['user', 'field_name', 'file', 'uploaded_at']
