from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    jurusan = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    deleted_date = models.DateTimeField()
    created_by = models.IntegerField(null=True, default=None)
    updated_by = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 'user'