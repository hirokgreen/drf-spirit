from django.test import TestCase
from rest_framework.test import APIClient
from drf_spirit.models import Category

class CategoryTest(TestCase):

    def setUp(self):
        Category.objects.create(title='Alice',)
        self.client = APIClient()

    def test_get(self):
        resp = self.client.get('/category/1/',)
        self.assertEqual(resp.status_code, 200)
