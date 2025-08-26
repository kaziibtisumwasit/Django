from django.db import models
from students.models import Student

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"
