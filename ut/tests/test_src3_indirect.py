from unittest import TestCase
from indirect import f3

class Feature3IndirectTest(TestCase):

    def setUp(self):
        self.feature = f3()
        self.info = 'I am an awesome feature, The next zillion dollar idea'

    def test_feature_info(self):
        self.assertEqual(self.feature.info(), self.info)

