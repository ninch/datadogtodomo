import unittest

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from apis.domo.api import Domo

class TestBase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        res = Domo().hello()
        self.assertEqual(res, 'hello from domo.api.Domo')

    def test_getClient(self):
        self.assertIsNotNone(Domo()._getClient())

    def test_getSecret(self):
        self.assertIsNotNone(Domo()._getSecret())

if __name__ == '__main__':
    unittest.main()
