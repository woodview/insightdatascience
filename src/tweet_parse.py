"""
Methods to parse a tweet and count the words used
"""

import numpy


class TweetParse:

    def __init__(self):
        self.uniquewordscountlist = []
        self.wordstweeted = {}

    @staticmethod
    def split(tweet):
        """
        Return the tweet in a list of 'words' using whitespace as the delimiter
        """
        return tweet.split()

    @staticmethod
    def uniquewords(tweet):
        """
        Return the tweet unique words used
        """
        return set(TweetParse.split(tweet))

    @staticmethod
    def numunique(tweet):
        """
        Return the number of unique words used in the tweet
        """
        return len(TweetParse.uniquewords(tweet))

    def addtouniquecounts(self, tweet):
        """
        Add the tweet unique words count to the list of unique words count
        """
        self.uniquewordscountlist.append(TweetParse.numunique(tweet))

    def getmedianunique(self):
        """
        Return the median of the unique words per tweet
        When no tweet has been parsed, return -1
        """
        if self.uniquewordscountlist:
            return numpy.median(self.uniquewordscountlist)
        else:
            return -1

    def addtowordscounter(self, tweet):
        """
        Parse the tweet and add the word count
        """
        words = TweetParse.split(tweet)
        for w in words:
            self.incrementwordcount(w)

    def incrementwordcount(self, word):
        """
        Increase the count of the word counter
        """
        self.wordstweeted[word] = self.wordstweeted.get(word, 0) + 1

    def getwordcount(self, word):
        """
        Return the count of the word used
        """
        return self.wordstweeted.get(word, 0)

    def alltweetedwords(self):
        """
        Return all the words used in all tweets in sorted order
        """
        sortedwords = self.wordstweeted.keys()
        sortedwords.sort()
        return sortedwords
