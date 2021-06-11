from django.test import TestCase

from .models import Student, Classroom


def create_student():
    """Create a sample student"""
    Student.objects.create(
        first_name="Testuser",
        last_name="Doe",
        admission_number=20,
        is_qualified=False,
        average_score=90.5
    )


class TestStudentModel(TestCase):

    def test_add_a_plus(self):
        a = 1
        b = 2
        c = a + b

        self.assertEqual(c, 3)

    def test_creating_a_student(self):
        """Test that a student can be created."""
        create_student()
        student_result = Student.objects.last()

        self.assertEqual(student_result.first_name, "Testuser")

    def test_str_representation(self):
        """Test the str representation."""

        create_student()
        student_result = Student.objects.last()

        self.assertTrue(str(student_result.first_name))

