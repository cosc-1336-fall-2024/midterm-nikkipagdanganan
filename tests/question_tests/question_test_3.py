#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import test_config, get_miles_per_hour

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_miles_per_hour(self):
        self.assertEqual(19.883872, get_miles_per_hour(32,60))

