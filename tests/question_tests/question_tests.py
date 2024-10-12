#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, get_assessment_value, get_tax_assessed
from src.question_b.question_b import test_config, get_person_category
from src.question_c.question_c import test_config, get_miles_per_hour
from src.question_d.question_d import test_config, is_prime 

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_assessment_value(self):
        self.assertEqual(6000, get_assessment_value(10000))
        self.assertEqual(12000, get_assessment_value(20000))

    def test_get_tax_assessed(self):
        self.assertEqual(43.20, get_tax_assessed(6000))
        self.assertEqual(72, get_tax_assessed(10000))

    def test_get_person_category(self):
        self.assertEqual('infant', get_person_category(1).lower())
        self.assertEqual('child', get_person_category(2).lower())
        self.assertEqual('teenager', get_person_category(14).lower())
        self.assertEqual('adult', get_person_category(20).lower())

    def test_get_miles_per_hour(self):
        self.assertEqual(19.883872, get_miles_per_hour(32,60))

    def test_is_prime(self):
        self.assertEqual(False, is_prime(4))
        self.assertEqual(True, is_prime(5))
        self.assertEqual(True, is_prime(11))
