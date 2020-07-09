from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali, date2jalali

# Register your models here.
from mailroom.apps.documents.models import Document



@admin.register(Document)
class DocumentAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = (
        'jalali_created_at', 'typ', 'requester','receiver','subsystem','subject','code','jalali_date'
    )


    def jalali_created_at(self, obj):
        return datetime2jalali(obj.created_at).strftime('%y/%m/%d %H:%M:%S')

    def jalali_date(self, obj):
        return date2jalali(obj.date).strftime('%y/%m/%d')