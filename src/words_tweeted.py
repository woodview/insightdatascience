# example of program that calculates the total number of times each word has been tweeted.

import argparse
from tweet_parse import TweetParse


def main():

    # add and parse the command line arguments requirement, infile and outfile
    argparser = argparse.ArgumentParser(description='Calculates the total number of times each word has been tweeted.')
    argparser.add_argument('infile', type=argparse.FileType('r'), help='text file containing tweets')
    argparser.add_argument('outfile', type=argparse.FileType('w'), help='output file showing the words counts')
    args = argparser.parse_args()

    # TweetParse object for finding and counting the words per tweet
    tp = TweetParse()

    # read each tweet
    # use the TweetParse function to find and update the frequency of words tweeted
    for line in args.infile:
        tp.addtowordscounter(line)

    # get all the words found in all the tweets in sorted order
    words = tp.alltweetedwords()

    # get the length of the longest word, use for formatting the output
    maxwordlen = len(max(words, key=len))

    # print out each word in the sorted order and its number of times tweeted
    for word in words:
        args.outfile.write('{w:<{l}}\t{c:3d}\n'.format(w=word, l=maxwordlen+1, c=tp.getwordcount(word)))

    # close the files
    args.infile.close()
    args.outfile.close()


# start program
main()
