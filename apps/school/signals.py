import os

from celery import shared_task
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Student


@shared_task
def send_notification(student_id):
    try:
        student = Student.objects.get(id=student_id)
        subject = 'New Student Created'
        message = f'A new student with the ID {student_id} has been created.'
        from_email = os.getenv("EMAIL_HOST_USER")
        recipient_list = [os.getenv("RECIPIENT")]
        send_mail(subject, message, from_email, recipient_list)
    except Student.DoesNotExist:
        pass


@receiver(post_save, sender=Student)
def trigger_send_notification(sender, instance, created, **kwargs):
    if created:
        send_notification.delay(instance.id)
