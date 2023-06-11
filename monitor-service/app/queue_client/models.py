from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class QueueConnection(models.Model):
    
    # class DataSourceType(models.TextChoices):
    #     KAFKA = 'KAFKA', _('KAFKA')
    #     RABBITMQ = 'RABBITMQ', _('RABBITMQ')
    #     MYSQL = 'MYSQL', _('MYSQL')
    
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    url = models.CharField(max_length=100, blank=True, default='')
    active = models.BooleanField(default=True)
    # dataSourceType = models.TextField(choices=DataSourceType.choices)