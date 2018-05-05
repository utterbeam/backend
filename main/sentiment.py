import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer


def calculateSentimentScores(message_text):
	sid = SentimentIntensityAnalyzer()
	scores = sid.polarity_scores(message_text)
	scoreArray = {}
	for key in sorted(scores):
		scoreArray[key] = scores[key]*100
		# scoreArray.append('{0}: {1}, '.format(key, scores[key]))
	return scoreArray


if __name__ == '__main__':
	text = '''Cars is a 2006 American computer-animated comedy-adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures. Directed and co-written by John Lasseter, it is Pixar's final independently-produced motion picture before its purchase by Disney in May 2006. Set in a world populated entirely by anthropomorphic cars and other vehicles, the film stars the voices of Owen Wilson, Paul Newman (in his final acting role), Bonnie Hunt, Larry the Cable Guy, Tony Shalhoub, Cheech Marin, Michael Wallis, George Carlin, Paul Dooley, Jenifer Lewis, Guido Quaroni, Michael Keaton, Katherine Helmond and John Ratzenberger. Race car drivers Dale Earnhardt, Jr., Mario Andretti, Michael Schumacher and car enthusiast Jay Leno (as "Jay Limo") voice themselves.'''
	a = calculateSentimentScores(text)
	print(a)
