from django.test import TestCase
from app.models import Task, Priority
import factory
from django.contrib.auth import get_user_model


class PriorityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Priority
    name = 'URGENT'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    username = 'user'
    password = '1234'


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task
    name = 'test done'
    priority = factory.SubFactory(PriorityFactory)
    user = factory.SubFactory(UserFactory)

class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task
    name = 'test done'
    priority = factory.SubFactory(PriorityFactory)
    user = factory.SubFactory(UserFactory)


class TaskTestCase(TestCase):
    def setUp(self):
        test_task = TaskFactory()
        print(get_user_model())
        
    def test_task_name(self):
        task = Task.objects.get(name='test done')
        self.assertEqual(task.name, 'test done')


class PriorityTestCase(TestCase):
    def setUp(self):
        test_priority = PriorityFactory()
        priority_number = PriorityFactory.build(name=2)
        print(test_priority.name)
        
    def test_priority_name(self):
        name = Priority.objects.get(name='URGENT')
        self.assertEqual(name.name, 'URGENT')
