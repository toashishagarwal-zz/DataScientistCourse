import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def printSentimentFileScore(fp):
	afinnfile = open(fp);
	scores = {}
	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = int(score)

	print scores.items()

def printTweets(fp):
	tweets = []
	for line in open(fp, 'r'):
		tweets.append(json.loads(line))
	print "Total Tweets read are --> " + str(len(tweets)) + " and they are -"

	for tweet in tweets:
		try:
			print tweet['text']
		except:
			pass

def tokenize(w):
	print ""

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    # printSentimentFileScore(sys.argv[1])
    printTweets(sys.argv[2]);

if __name__ == '__main__':
    main()
