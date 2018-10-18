from django.db import models

# Create your models here.


class ssh(models.Model):
    id = models.AutoField(primary_key=True)
    ip_address = models.GenericIPAddressField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login_time = models.DateTimeField(auto_now=True)
    introduction = models.TextField(null=True)
    removed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.ip_address
