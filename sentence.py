import re


class Sentence(object):
    """
    This class contains a sentence, a collection of words
    Attributes:
        sentence (str) : words separated with space
    """

    def __init__(self, sentence):
        self.sentence = sentence

    def longest_word(self):
        """returns longest word (str) and its length (int) in a sentence
        """
        # removing punctuation from sentence, to calculate word correctly
        just_words = re.sub(r'[^\w\s]', '', self.sentence)
        each_word = just_words.split()
        if not each_word:
            raise ValueError("Please provide sentence with atleast one character")
        if len(each_word) > 1:
            # if there are more than 2 words in a sentence
            longest_word = max(each_word, key=len)
            # if multiple words are of same length, it returns word with lowest index
            return longest_word, len(longest_word)
        # if sentence contains only 1 word, return word, and its length
        return each_word[0], len(each_word[0])
