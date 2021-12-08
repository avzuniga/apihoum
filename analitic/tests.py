from rest_framework.test import APITestCase


class AnaliticTests(APITestCase):
    def test_get_visits(self):
        """
        Ensure we can obtein some list answer from this endpoint
        """
        url = '/api/v1/analitic/visit/obtein_visits/?houmer=angie&date=2021-12-08'
        response = self.client.get(url)
        self.assertIsInstance(response.data, list)
        
    def test_get_moments_velocity(self):
        """
        Ensure we can obtein some list answer from this endpoint
        """
        url = '/api/v1/analitic/coordinate/obtein_coordenates_velocity/?velocity=15&houmer=angie&date=2021-12-08'
        response = self.client.get(url)
        self.assertIsInstance(response.data, list)
        