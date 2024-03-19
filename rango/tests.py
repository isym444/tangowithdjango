from django.test import TestCase
from django.urls import reverse

from rango.models import Category


# Create your tests here.

class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        category = Category(name='test', views=-1, likes=0)
        category.save()
        self.assertEqual((category.views >= 0), True)

    def test_slug_line_creation(self):
        category = Category(name='Random Category String')
        category.save()
        self.assertEqual(category.slug, 'random-category-string')

class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
        add_category('Python', 1, 1)
        add_category('C++', 1, 1)
        add_category('Erlang', 1, 1)
        response = self.client.get(reverse('rango:index'))
        print(response.context)
        print(response.context['categories'])
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")
        self.assertContains(response, "C++")
        self.assertContains(response, "Erlang")
        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 3)



def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes
    category.save()
    return category
