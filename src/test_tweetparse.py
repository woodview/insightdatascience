"""
unit tests for tweet_parse.py
"""


import unittest
from tweet_parse import TweetParse


class TweetParseTestCase(unittest.TestCase):

    def test_white_space(self):
        """
        Test white space delimiter
        """
        self.assertEqual(TweetParse.split('a b  c'), ['a', 'b', 'c'])

    def test_num_unique(self):
        """
        Test the counting of unique words
        """
        self.assertEqual(TweetParse.numunique('a b a c'), 3)

    def test_median_unique(self):
        """
        Test the calculation of median number
        """
        tp = TweetParse()
        tp.addtouniquecounts('a b a c')
        self.assertEqual(tp.getmedianunique(), 3)
        tp.addtouniquecounts('123')
        self.assertEqual(tp.getmedianunique(), 2)

    def test_word_count(self):
        """
        Test the word count
        """
        tp = TweetParse()
        tp.addtowordscounter('a b a c')
        self.assertEqual(tp.getwordcount('a'), 2)
        self.assertEqual(tp.getwordcount('c'), 1)
        self.assertEqual(tp.getwordcount('d'), 0)
        tp.addtowordscounter('ad a')
        self.assertEqual(tp.getwordcount('a'), 3)
        self.assertEqual(tp.getwordcount('ad'), 1)

    def test_words_sort(self):
        """
        Test the word sort order
        """
        tp = TweetParse()
        tweet = '~ } | { z a ` _ ^ ] \ [ @ ? > = < ; : 9 0 / . - , + * ) ( \' & % $ # " ! '
        tp.addtowordscounter(tweet)
        self.assertEqual(tp.alltweetedwords()[0], '!')
        # reverse the test tweet for the expected order
        revtweet = tweet.split()
        revtweet.reverse()
        self.assertEqual(''.join(tp.alltweetedwords()), ''.join(revtweet))


if __name__ == '__main__':
    unittest.main()
