from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.school.views import student_views, auth_views, class_views

urlpatterns = [
    path("student/create/", student_views.StudentCreateView.as_view()),
    path("student/list/", student_views.StudentListView.as_view()),
    path("student/<int:id>/detail/", student_views.StudentDetailView.as_view()),
    path("student/<int:id>/patch/", student_views.StudentPatchView.as_view()),
    path("student/<int:id>/delete/", student_views.StudentDeleteView.as_view()),

    path("register/", auth_views.RegisterView.as_view(), name='register'),
    path("login/", auth_views.LoginView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    
    path("class/create/", class_views.ClassCreateView.as_view()),
    path("mailing/create/", class_views.MailingCreateView.as_view())
]
