from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    name = models.CharField(max_length=20, default="", verbose_name="Name")
    mobile = models.CharField(max_length=11, default="", verbose_name="Mobile")
    email = models.EmailField(max_length=50, verbose_name="Email")
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name="Position")
    superior = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Superior")

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = verbose_name
        ordering = ['id']
        db_table = 'dev_user_profile'

    def __str__(self):
        return self.username


class Role(models.Model):
    role_choices = (
        (1, 'Saas'),
        (2, 'Customer')
    )
    name = models.CharField(max_length=10)
    type = models.IntegerField(choices=role_choices)
    user = models.ForeignKey(UserProfile, on_delete=False)
    department = models.ManyToManyField('Department')

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = verbose_name
        ordering = ['id']
        db_table = 'dev_role'


class Department(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = verbose_name
        ordering = ['id']
        db_table = 'dev_department'
