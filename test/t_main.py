import unittest

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main
from main import main

class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_callHello(self):
        self.assertEqual(main().callHello('domo'), 'hello from domo.api.Domo')
        self.assertEqual(main().callHello('datadog'), 'hello from datadog.api.Datadog')


if __name__ == '__main__':
    unittest.main()
