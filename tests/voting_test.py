from voting import app
import unittest

class ErrorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_unhandledexception_code(self):
        result = self.app.put('/ce-results')

        self.assertEqual(result.status_code, 500)

    def test_unhandledexception_data(self):
        result = self.app.put('/ce-results')

        self.assertIn('Something Went Wrong', result.data)