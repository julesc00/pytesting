from django.test import TestCase

from mixer.backend.django import mixer

from classroom.models import Student, Classroom


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
        student = mixer.blend(Student)
        student_result = Student.objects.last()

        self.assertEqual(student_result.first_name, student.first_name)

    def test_str_representation(self):
        """Test the str representation."""

        create_student()
        student_result = Student.objects.last()

        self.assertTrue(str(student_result.first_name))

    def test_grade_fail(self):
        """Test a fail grade."""

        mixer.blend(Student, average_score=30)
        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grades(), "Fail")

    def test_grade_pass(self):
        """Test that a pass grade."""

        mixer.blend(Student, average_score=50)
        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grades(), "Pass")

    def test_grade_excellent(self):
        """Test that an excellent grade."""

        create_student()
        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grades(), "Excellent")
