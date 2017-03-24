from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from drf_spirit.models import Category

class CategoryTest(TestCase):

    def setUp(self):
        Category.objects.create(title='alice',)
        self.client = APIClient()

    def test_get(self):
        resp = self.client.get(reverse('drf_spirit:category-detail', args=['alice']))
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        data = {'title': 'someone', 'description': 'hello world'}
        resp = self.client.post(reverse('drf_spirit:category-list'), data)
        item = Category.objects.filter(slug='someone').exists()
        self.assertEqual(item, True)
