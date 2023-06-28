from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.school.managers import UserManager


class Teacher(AbstractBaseUser, PermissionsMixin):
    number_phone = models.CharField(max_length=25, unique=True)
    subject = models.CharField(max_length=25)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    classroom = models.ForeignKey(
        "Class",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_query_name="teachers_classroom"
    )
    USERNAME_FIELD = 'number_phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.number_phone


class School(models.Model):
    title = models.CharField(max_length=100)
    classrooms = models.ManyToManyField(
        "Class",
        related_query_name="schools",
        blank=True,
    )

    def __str__(self):
        return self.title


class Class(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_query_name="classes",
        blank=True,
        null=True,
    )
    student = models.ManyToManyField(
        "Student",
        related_query_name="classes",
        blank=True,
    )

    def __str__(self):
        return self.title


class Student(models.Model):
    fio = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()
    classroom = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="student_of_classroom"
    )
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    photo = models.ImageField(
        upload_to='student_photos/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.fio}'
