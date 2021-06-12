from django.test import TestCase
import pytest

from mixer.backend.django import mixer

from classroom.models import Student, Classroom

pytestmark = pytest.mark.django_db

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

        assert str(student_result.first_name) == "Panchito"

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

    def test_grade_error(self):
        """Test that error is triggered."""

        student1 = mixer.blend(Student, average_score=101)
        student_result = Student.objects.last()

        assert student_result.get_grades() == "Error"


class TestClassroomModel:
    def test_classroom_create(self):
        """Test that a classroom entry can be created."""

        mixer.blend(Classroom, name="Physics")
        cls_result = Classroom.objects.last()

        assert str(cls_result.name) == "Physics"
