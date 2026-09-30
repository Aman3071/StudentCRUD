from django.contrib import admin
from django.urls import path

from students import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.add_student, name="add_student"),
    path("students/", views.student_list, name="student_list"),
    path("student-edit/<int:id>/", views.edit_student, name="edit_student"),
    path("student-delete/<int:id>/", views.delete_student, name="delete_student"),
]
