from unittest import TestCase
from ..src.src3 import Feature3

class Feature3Test(TestCase):

    def setUp(self):
        self.feature = Feature3()
        self.info = 'I am an awesome feature, The next zillion dollar idea'

    def test_feature_info(self):
        self.assertEqual(self.feature.info(), self.info)

