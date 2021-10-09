import unittest
from translator import english_to_french, french_to_english

class TestEnglistToFrench(unittest.TestCase):
    def test1(self):
        # test when "englishToFrench("Hello")" is given as input the output is "Bonjour".
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test2(self):
        # test when "" is given as input the output is "Method failed with status code 400:
        # Unable to validate payload size, the parameter 'text' is null or empty.".
        self.assertEqual(english_to_french(""), "Method failed with status code 400: Unable to validate payload size, the parameter 'text' is null or empty.")

class TestFrenchToEnglish(unittest.TestCase):
    # test when "frenchToEnglish("Bonjour")" is given as input the output is "Hello".
    def test3(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test4(self):
        # test when "" is given as input the output is "Method failed with status code 400:
        # Unable to validate payload size, the parameter 'text' is null or empty.".
        self.assertEqual(french_to_english(""), "Method failed with status code 400: Unable to validate payload size, the parameter 'text' is null or empty.")

unittest.main()
