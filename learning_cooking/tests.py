# -*- coding: utf-8 -*-
"""
Tests for learning_cooking app
"""
from django.test import TestCase
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Course, Chef, Registration, Student


class ChefModelTestCase(TestCase):
    """
    Test Chef model
    """
    def setUp(self):
        self.chef = Chef(name="test chef", email="test_chef@email.com")
        self.chef.save()

    def test_create(self):
        """
        Test new chef
        """
        chef = Chef(name="test chef 2", email="test_chef2@email.com")
        chef.save()
        self.assertTrue(isinstance(chef, Chef))
        self.assertEquals(chef, Chef.objects.get(pk=chef.id))

    def test_update(self):
        """
        Test update chef
        """
        self.chef.name = "Other chef"
        self.chef.save()
        self.assertEquals(self.chef.name, "Other chef")

    def test_string_repr(self):
        """
        Test str repr
        """
        self.assertEquals(str(self.chef), self.chef.name)

    def test_unicode_repr(self):
        """
        Test unicode repr
        """
        self.assertEqual(unicode(self.chef), self.chef.name)

    def test_delete(self):
        """
        Test delete chef
        """
        self.chef.delete()
        self.assertEqual(len(Chef.objects.filter(name="Other chef")), 0)


class StudentModelTestCase(TestCase):
    """
    Test Student model
    """
    def setUp(self):
        self.student = Student(name="test", email="test@email.com",
                               surname="testsurname", zip="123456",
                               country="ES")
        self.student.save()

    def test_create(self):
        """
        Test new student
        """
        student = Student(name="test student 2",
                          email="test_student2@email.com",
                          surname="testsurname2", zip="1234560", country="FR")
        student.save()
        self.assertTrue(isinstance(student, Student))
        self.assertEquals(student, Student.objects.get(pk=student.id))

    def test_update(self):
        """
        Test update student
        """
        self.student.name = "Other student"
        self.student.save()
        self.student.refresh_from_db()
        self.assertEquals(self.student.name, "Other student")

    def test_string_repr(self):
        """
        Test str repr
        """
        self.assertEquals(str(self.student), self.student.name)

    def test_unicode_repr(self):
        """
        Test unicode repr
        """
        self.assertEqual(unicode(self.student), self.student.name)

    def test_delete(self):
        """
        Test delete student
        """
        self.student.delete()
        self.assertEqual(len(Student.objects.filter(name="Other student")), 0)


class CourseModelTestCase(TestCase):
    """
    Test Course model
    """
    def setUp(self):
        self.chef = Chef(name="chef test", email="chef_test@email.com")
        self.chef.save()
        self.course = Course(name="test course", description="test course",
                             chef=self.chef)
        self.course.save()

    def test_create(self):
        """
        Test new course
        """
        course = Course(name="test course 2", description="test_course2",
                        chef=self.chef)
        course.save()
        self.assertTrue(isinstance(course, Course))
        self.assertEquals(course, Course.objects.get(pk=course.id))

    def test_update(self):
        """
        Test update course
        """
        self.course.name = "Other course"
        self.course.save()
        self.course.refresh_from_db()
        self.assertEquals(self.course.name, "Other course")

    def test_string_repr(self):
        """
        Test str repr
        """
        self.assertEquals(str(self.course), self.course.name)

    def test_unicode_repr(self):
        """
        Test unicode repr
        """
        self.assertEqual(unicode(self.course), self.course.name)

    def test_delete(self):
        """
        Test delete course
        """
        self.course.delete()
        self.assertEqual(len(Course.objects.filter(name="Other course")), 0)


class RegistrationModelTestCase(TestCase):
    """
    Test Registration model
    """
    def setUp(self):
        self.chef = Chef(name="chef test", email="chef_test@email.com")
        self.chef.save()
        self.course = Course(name="test course", description="test course",
                             chef=self.chef)
        self.course.save()
        self.student = Student(name="test", email="test@email.com",
                               surname="testsurname", zip="123456",
                               country="ES")
        self.student.save()
        self.registration = Registration(course=self.course,
                                         student=self.student)
        self.registration.save()

    def test_create(self):
        """
        Test new registration
        """
        registration = Registration(course=self.course, student=self.student)
        self.assertRaises(IntegrityError, registration.save)

    def test_string_repr(self):
        """
        Test str repr
        """
        name = "%s - %s" % (self.course.name, self.student.name)
        self.assertEquals(str(self.registration), name)

    def test_unicode_repr(self):
        """
        Test unicode repr
        """
        name = u"%s - %s" % (self.course.name, self.student.name)
        self.assertEqual(unicode(self.registration), name)

    def test_delete(self):
        """
        Test delete registration
        """
        self.registration.delete()
        reg = Registration.objects.filter(student=self.student,
                                          course=self.course)
        self.assertEqual(len(reg), 0)


class CourseViewTestCase(APITestCase):
    """
    Test api Course
    """
    def setUp(self):
        self.chef = Chef(name="cheftest", email="cheftest@email.com")
        self.chef.save()
        self.course = Course(name="testcourse", description="testcourse",
                             chef=self.chef)
        self.course.save()

    def test_new_course(self):
        """
        Test new course
        """
        response = self.client.post('/courses/', {'name': 'Test course',
                                                  'chef': self.chef.id},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_course(self):
        """
        Test get course
        """
        response = self.client.get('/courses/%s/' % self.course.id,
                                   format='json')
        self.assertEqual(response.data, {"id": 1, "name": "testcourse",
                                         "description": "testcourse",
                                         "start_date": None,
                                         "end_date": None,
                                         "chef": self.chef.id,
                                         "students": []})

    def test_list_courses(self):
        """
        Test list course
        """
        response = self.client.get('/courses/?fields=id,name', format='json')
        data = response.data
        result = data["results"][0]
        self.assertEqual(result, {"id": 1, "name": "testcourse"})

    def test_list_courses_email_view(self):
        """
        Test list course email_view
        """
        response = self.client.get('/courses/email_view/', format='json')
        data = response.data[0]
        self.assertEqual(data, {"id": 1, "name": "testcourse",
                                "description": "testcourse",
                                "start_date": None, "end_date": None,
                                "chef": {"id": 1, "email": "cheftest@email.com"
                                        },
                                "students": []})

    def test_put_course(self):
        """
        Test put course
        """
        response = self.client.put('/courses/%s/' % self.course.id,
                                   {"id": 1, "name": "testcourse2",
                                    "description": "testcourse2",
                                    "chef": self.chef.id}, format='json')
        self.assertEqual(response.data, {"id": 1, "name": "testcourse2",
                                         "description": "testcourse2",
                                         "start_date": None,
                                         "end_date": None,
                                         "chef": self.chef.id,
                                         "students": []})

    def test_delete_course(self):
        """
        Test delete course
        """
        response = self.client.delete('/courses/%s/' % self.course.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class RegistrationViewTestCase(APITestCase):
    """
    Test api Registration
    """
    def setUp(self):
        self.chef = Chef(name="cheftestregistration",
                         email="cheftestregistration@email.com")
        self.chef.save()

        self.course = Course(name="testcourseregistration",
                             description="testcourse",
                             chef=self.chef)
        self.course.save()

        self.student = Student(name="testregistration",
                               email="testregistration@email.com",
                               surname="testsurname", zip="123456",
                               country="ES")
        self.student.save()

        self.registration = Registration(course=self.course,
                                         student=self.student)
        self.registration.save()

    def test_get_registration(self):
        """
        Test get registration
        """
        response = self.client.get('/registrations/%s/' % self.registration.id,
                                   format='json')
        data = response.data
        data.pop('register_date', None)
        self.assertEqual(data,
                         {'course': self.course.id,
                          'student': self.student.id,
                          'id': self.registration.id})

    def test_list_registration(self):
        """
        Test list registration
        """
        response = self.client.get('/registrations/', format='json')
        data = response.data["results"][0]
        data.pop('register_date', None)
        self.assertEqual(data,
                         {"id": self.registration.id,
                          "course": self.course.id,
                          "student": self.student.id})

    def test_delete_registration(self):
        """
        Test delete registration
        """
        response = self.client.delete('/registrations/%s/' %
                                      self.registration.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
