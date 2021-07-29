from .forms import StudentRegistrationForm
from django.shortcuts import render
def register_student(request):
    form=StudentRegistrationForm()
    return render(request,"student/register_student.html",{"form".form})