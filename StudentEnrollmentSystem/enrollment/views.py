from django.shortcuts import render, redirect
from .models import Enrollment
from .forms import EnrollmentForm

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, "enrolment_list.html", {"enrollments": enrollments})

def add_enrollment(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("enrollment_list")
    else:
        form = EnrollmentForm()
    return render(request, "add_enrollment.html", {"form": form})
