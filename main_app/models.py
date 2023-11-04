from django.contrib import admin
from django.db import models

# Create your models here.
from django_choices_field import TextChoicesField


class Student(models.Model):
    class TextEnum(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    gender = TextChoicesField(choices_enum=TextEnum, default=TextEnum.FEMALE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}  {}".format(self.first_name, self.last_name)
