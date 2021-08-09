from django.test import TestCase

from todos.models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.title = 'first todo'
        cls.body = 'a body here'
        Todo.objects.create(title=cls.title, body=cls.body)

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, self.title)
        expected_object_body = f'{todo.body}'
        self.assertEqual(expected_object_body, self.body)
