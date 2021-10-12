import Main
import unittest
import json

class APITest(unittest.TestCase):
    def setUp(self):
        Main.app.testing = True
        self.app = Main.app.test_client()

    def test_home(self):
        response = self.app.get('/')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Available Routes'], ["GET /api/ping", "GET /api/posts"])
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()