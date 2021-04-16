from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=50, default="")
    email = models.EmailField(default="")
    parent_email = models.EmailField(default="")
    parent_number = models.CharField(max_length=50, default="")
    teacher_email = models.EmailField(default="")
    student_id = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.student_id) + " : " + str(self.first_name) + " " + str(self.last_name) + " : " + str(self.email)
