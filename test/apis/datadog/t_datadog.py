import unittest

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from apis.datadog.api import Datadog

class TestBase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        res = Datadog().hello()
        self.assertEqual(res, 'hello from datadog.api.Datadog')

    def test_getApiKey(self):
        self.assertIsNotNone(Datadog()._getApiKey())

    def test_getAppKey(self):
        self.assertIsNotNone(Datadog()._getAppKey())

if __name__ == '__main__':
    unittest.main()
