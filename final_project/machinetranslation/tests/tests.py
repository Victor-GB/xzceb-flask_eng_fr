import unittest 
from translator import english_to_french, french_to_english

class TestFr2Eng(unittest.TestCase):

    def test1(self):
        self.assertRaises(ValueError,english_to_french,None)

    def test2(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")

    def test3(self):
        self.assertNotEqual(english_to_french("Hello"),"Voila")

class TestEng2Fr(unittest.TestCase):

    def test1(self):
        self.assertRaises(ValueError,french_to_english,None)

    def test2(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")

    def test3(self):
        self.assertNotEqual(french_to_english("Bonjour"),"good evening")


unittest.main()