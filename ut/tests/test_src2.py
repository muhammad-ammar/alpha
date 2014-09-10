from unittest import TestCase
from ..src.src2 import Feature2

class Feature2Test(TestCase):

    def setUp(self):
        self.feature = Feature2()
        self.info = 'I am an awesome feature, The next trillion dollar idea'

    def test_feature_info(self):
        self.assertEqual(self.feature.info(), self.info)

