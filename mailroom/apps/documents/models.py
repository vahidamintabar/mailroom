from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.utils import timezone


class Document(models.Model):
    TYPE_PUBLIC = 1
    TYPE_PRIVATE = 2
    TYPE_CHOICES = (
        (TYPE_PUBLIC, 'عمومی'),
        (TYPE_PRIVATE, 'شخصی')
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    creator = models.ForeignKey(get_user_model(), on_delete=CASCADE, verbose_name='ایجاد کننده')
    file = models.FileField(upload_to='docs/', verbose_name='فایل')
    typ = models.IntegerField(choices=TYPE_CHOICES, default=TYPE_PUBLIC, verbose_name='نوع درخواست')
    requester = models.CharField(max_length=255, null=True, blank=True, verbose_name='متقاضی')
    receiver = models.CharField(max_length=255, null=True, blank=True, verbose_name='گیرنده')
    subsystem = models.CharField(max_length=255, null=True, blank=True, verbose_name='زیرمجموعه')
    subject = models.CharField(max_length=255, null=True, blank=True, verbose_name='موضوع')
    content = models.TextField(null=True, blank=True, verbose_name='متن')
    code = models.CharField(max_length=255, null=True, blank=True, verbose_name='شماره نامه')
    date = models.DateField(default=timezone.now, verbose_name='تاریخ نامه')
