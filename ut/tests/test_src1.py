from unittest import TestCase
from ..src.src1 import Feature1 

class Feature1Test(TestCase):

    def setUp(self):	
        self.feature = Feature1()   
        self.info = 'I am an awesome feature, The next billion dollar idea'

    def test_feature_info(self):
        self.assertEqual(self.feature.info(), self.info)
