from django.contrib import admin

from apps.school.models import Teacher, Class, Student, School

admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(School)
admin.site.register(Student)
