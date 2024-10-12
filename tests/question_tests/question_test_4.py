#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_d.question_d import test_config, is_prime 

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_is_prime(self):
        self.assertEqual(False, is_prime(4))
        self.assertEqual(True, is_prime(5))
        self.assertEqual(True, is_prime(11))