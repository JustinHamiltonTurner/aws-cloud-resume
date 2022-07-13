import unittest
import requests

class TestBackend(unittest.TestCase):

    def test_count(self):
        # Calls api to get visitor count and assigns the numeric value to var first.
        r = requests.get('https://55cf017q25.execute-api.us-east-1.amazonaws.com/Prod/count')
        first = r.json()['message']
        # Calls api again and assigns new value to second.
        r2 = requests.get('https://55cf017q25.execute-api.us-east-1.amazonaws.com/Prod/count')
        second = r2.json()['message']
        # Message displayed if test fails.
        message = "test_count failed. Visitor count is not working."

        self.assertLess(first, second, message)

if __name__ == '__main__':
    unittest.main()