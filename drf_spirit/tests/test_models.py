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

    def test_post(self):
        resp = self.client.post(
            '/category/', {'title': 'someone', 'slug': 'lol'}, format='json')
        item = Category.objects.filter(title='someone').exists()
        self.assertEqual(item, True)   
