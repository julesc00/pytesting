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
        average_score=90.5)


class TestStudentModel(TestCase):

    def test_add(self):
        a = 5
        b = 5
        c = a + b

        assert c == 10

    def test_creating_a_student(self):
        """Test that a student can be created."""
        student = mixer.blend(Student)
        student_result = Student.objects.last()

        assert student_result.first_name == student.first_name

    def test_str_representation(self):
        """Test the str representation."""
        mixer.blend(Student, first_name="Panchito")
        student_result = Student.objects.last()

        assert student_result.first_name == "Panchito"

    def test_grade_fail(self):
        """Test a fail grade."""

        mixer.blend(Student, average_score=35)
        student_result = Student.objects.last()

        assert student_result.get_grades() == "Fail"

    def test_grade_pass(self):
        """Test a pass grade."""

        mixer.blend(Student, average_score=60)
        student_result = Student.objects.last()

        assert student_result.get_grades() == "Pass"

    def test_grade_excellent(self):
        """Test an excellent grade."""

        create_student()
        student_result = Student.objects.last()

        assert student_result.get_grades() == "Excellent"
