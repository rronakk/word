import unittest
from sentence import Sentence


class TestSentence(unittest.TestCase):

    def test_longest_word(self):
        sentence = Sentence("Hello InRhythm")
        self.assertEqual(sentence.longest_word(), ("InRhythm", 8))

    def test_longest_word_with_one_word(self):
        sentence = Sentence("one")
        self.assertEqual(sentence.longest_word(), ("one", 3))

    def test_longest_word_with_punctuation(self):
        sentence = Sentence("what? are You!!! to achieve.....")
        self.assertEqual(sentence.longest_word(), ("achieve", 7))

    def test_longest_word_with_empty_sting(self):
        sentence = Sentence(" ")
        with self.assertRaises(ValueError):
            sentence.longest_word()

if __name__ == '__main__':
    unittest.main()
