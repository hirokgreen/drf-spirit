from django.test import TestCase
from rest_framework.test import APIClient
from drf_spirit.models import Category

class CategoryTest(TestCase):

    def setUp(self):
        Category.objects.create(title='alice',)
        self.client = APIClient()

    def test_get(self):
        resp = self.client.get('/category/alice/',)
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        resp = self.client.post(
            '/category/', {'title': 'someone', 'description': 'hello world'}, format='json')
        item = Category.objects.filter(slug='someone').exists()
        self.assertEqual(item, True)   
