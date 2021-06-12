from django.db import models


class Student(models.Model):
    """Create a student model."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admission_number = models.IntegerField(unique=True)
    is_qualified = models.BooleanField(default=False)
    average_score = models.DecimalField(max_digits=4, decimal_places=1, null=True)

    def __str__(self):
        """Unicode representation of Student."""
        return str(self.first_name)

    def get_grades(self):
        if self.average_score < 40:
            return "Fail"
        elif 40 < self.average_score < 70:
            return "Pass"
        elif 70 < self.average_score < 100:
            return "Excellent"

        else:
            return "Error"


class Classroom(models.Model):
    """Create a classroom model."""
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField(default=0)
    students = models.ManyToManyField("classroom.Student")

    def __str__(self):
        return str(self.name)

