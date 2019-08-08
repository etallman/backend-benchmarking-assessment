""" Test Suite for anagrams module. """
import unittest
from timeit import Timer
from anagrams import find_anagrams


class TestAnagrams(unittest.TestCase):
    """
        Bencharmking test case. We test actual functionality of find_anagrams
        with doctests, which is why this test case excludes those unit tests.
    """
    def setUp(self):
        self.short = []
        self.long = []

        with open("words/short.txt", "r") as handle:
            self.short = handle.read().split()

        with open("words/long.txt", "r") as handle:
            self.long = handle.read().split()

    def test_short(self):
        """ Test that find_anagrams runs in 5/1000 of a second or faster. """
        time = Timer(lambda: find_anagrams(self.short)).timeit(number=1)
        self.assertTrue(round(time, 3) <= 0.005,
                        "find_anagrams ran in {}, which exceeds the "
                        "threshhold of 0.005 seconds".format(round(time, 3)))

    # @unittest.skip("Remove this line once short test passes")
    def test_long(self):
        """ Test that find_anagrams runs in 1/10 of a second or faster. """
        time = Timer(lambda: find_anagrams(self.long)).timeit(number=1)
        self.assertTrue(round(time, 3) <= 0.10,
                        "find_anagrams ran in {}, which exceeds the "
                        "threshhold of 0.10 seconds".format(round(time, 3)))
