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
        (TYPE_PUBLIC, _('public')),
        (TYPE_PRIVATE, _('private'))
    )
    created_at = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    file = models.FileField(upload_to='docs/')
    typ = models.IntegerField(choices=TYPE_CHOICES, default=TYPE_PUBLIC)
    requester = models.CharField(max_length=255, null=True, blank=True)
    receiver = models.CharField(max_length=255, null=True, blank=True)
    subsystem = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(default=timezone.now)
