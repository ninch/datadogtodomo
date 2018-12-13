import unittest

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import apis
from apis import base
from apis.base import Api

class TestBase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        res = Api().hello()
        self.assertEqual(res, 'hello from api class')

    def test_readApiKeys(self):
        res = Api()._readApiKeys()
        self.assertIsNotNone(res.get('DATADOG', 'api_key'))

if __name__ == '__main__':
    unittest.main()
