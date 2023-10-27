from django.test import TestCase


class IndexViewTest(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
