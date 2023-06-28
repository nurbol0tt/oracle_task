from OracleDigital.celery import app
from django.core.mail import send_mail
from .models import Student


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


def send_newsletter():
    newsletter_subject = "Monthly Newsletter"
    newsletter_message = "Dear students, here is your monthly newsletter. Stay tuned for exciting updates and events!"
    students = Student.objects.all()
    for student in students:
        send_mail(
            newsletter_subject,
            newsletter_message,
            "settings.EMAIL_HOST_USER",  # Replace with your email address or a valid sender
            [student.email],
        )
