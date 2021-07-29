from django.urls import path
from .views import register_student

urlpatterrns= [
    path("register", register_student, name="register_student")
    path("admin/",admin.site.urls),
    path("student/",include(student.urls)),
]
