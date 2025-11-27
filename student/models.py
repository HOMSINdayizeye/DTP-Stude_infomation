from django.db import models

# My model to create Student
class Student(models.Model):
    full_name = models.CharField(max_length= 100)
    reg_number = models.CharField(max_length= 10, unique=True)

def __str__(self):
    return self.full_name

