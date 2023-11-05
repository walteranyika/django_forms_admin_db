import hashlib
import random
import time
from functools import partial

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


def make_file_path(field_name, instance, filename):
    now = time.time() * 1000 * random.randint(1, 10000000)
    str2hash = str(now)
    unique_name = hashlib.md5(str2hash.encode('utf-8')).hexdigest()
    new_file_name = f"{unique_name}.{filename.split('.')[-1]}"
    print(new_file_name)
    print(unique_name)
    # Produces [model_name]/[field_name]/[file_name]
    return '/'.join([instance.__class__.__name__.lower(), field_name, new_file_name])


class Employee(models.Model):
    name = models.CharField(max_length=50)
    employment_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    gender = models.CharField(max_length=15)
    profile = models.ImageField(upload_to=partial(make_file_path, 'image'))

    def __str__(self):
        return self.name


class UploadImages(models.Model):
    caption = models.CharField(max_length=20)
    image = models.ImageField(upload_to=partial(make_file_path, 'image'))

    def __str__(self):
        return self.caption
