from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=3000)
    status = models.BooleanField(default=False)
    public_flag = models.BooleanField(default=False)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    user_id = models.IntegerField()
    message = models.CharField(max_length=3000)
    status = models.BooleanField(default=True)
    public_flag = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
