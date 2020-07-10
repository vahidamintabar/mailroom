from django.contrib import admin
from django.utils.safestring import mark_safe
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali, date2jalali

# Register your models here.
from mailroom.apps.documents.models import Document


@admin.register(Document)
class DocumentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    search_fields = (
        'subject', 'content', 'code', 'requester', 'receiver', 'subsystem',
    )
    list_display = (
        'jalali_created_at', 'jalali_date', 'typ', 'requester', 'receiver', 'subsystem', 'subject', 'code', 'file_path'
    )

    readonly_fields = ('created_at', 'creator')

    def jalali_created_at(self, obj):
        return datetime2jalali(obj.created_at).strftime('%y/%m/%d %H:%M:%S')

    jalali_created_at.short_description = 'زمان ایجاد'

    def jalali_date(self, obj):
        return date2jalali(obj.date).strftime('%y/%m/%d')

    jalali_date.short_description = 'تاریخ نامه'

    def file_path(self, obj):
        return mark_safe(f'<a href="{obj.file.url}">{obj.file.name}</a>')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        super(DocumentAdmin, self).save_model(request, obj, form, change)
