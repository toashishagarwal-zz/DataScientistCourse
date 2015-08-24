import sys
import json

scores = {}

def lines(fp):
    print str(len(fp.readlines()))

def printSentimentFileScore(fp):
	afinnfile = open(fp);
	global scores 
	score = {}
	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = int(score)

def printTweets(fp):
	tweets = []
	for line in open(fp, 'r'):
		tweets.append(json.loads(line))
	print "Total Tweets read are --> " + str(len(tweets)) + " and they are -"

	for tweet in tweets:
		try:
			tokenizeAndPrintScore(tweet['text'])
		except:
			pass

def tokenizeAndPrintScore(w):
	words = w.split()
	oneTweetScore = 0
	for word in words:
		try:
			oneTweetScore = oneTweetScore + scores[word]
		except:
			pass
	print "TWEET = " + w + "\t SCORE = " + str(oneTweetScore)

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	printSentimentFileScore(sys.argv[1])
	printTweets(sys.argv[2])

if __name__ == '__main__':
    main()
