# example of program that calculates the median number of unique words per tweet.

import argparse
from tweet_parse import TweetParse


def main():

    # add and parse the command line arguments requirement, infile and outfile
    argparser = argparse.ArgumentParser(description='Calculates the median number of unique words per tweet.')
    argparser.add_argument('infile', type=argparse.FileType('r'), help='text file containing tweets')
    argparser.add_argument('outfile', type=argparse.FileType('w'), help='output file the median number writes to')
    args = argparser.parse_args()

    # TweetParse object for finding the number of unique words per tweet
    # and storing the numbers for calculating the median number
    tp = TweetParse()

    # read each tweet
    # add the number of unique words to the TweetParse object
    # get the new median number from the TweetParse object
    # print result to the outfile
    for line in args.infile:
        tp.addtouniquecounts(line)
        newmedian = tp.getmedianunique()
        args.outfile.write('{:.1f}\n'.format(newmedian))

    # close the files
    args.infile.close()
    args.outfile.close()


# start program
main()

