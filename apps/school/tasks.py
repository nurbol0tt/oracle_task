from OracleDigital.celery import app
from django.core.mail import send_mail
from .models import Student
from celery import shared_task


def send_invitation(email):
    email_body = "Hello, your account has been created, " \
                 "study well and good luck it will be useful to you"
    send_mail("Hi, Oracle Digital",
              email_body,
              "settings.EMAIL_HOST_USER",
              [email])


@app.task
def send_message_email(email):
    send_invitation(email)


@shared_task
def send_mailing(title, description):
    students = Student.objects.all()
    for student in students:
        send_mail(
            title,
            description,
            "settings.EMAIL_HOST_USER",  # Replace with your email address or a valid sender
            [student.email],
        )
