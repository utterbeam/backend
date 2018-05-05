import requests
from bs4 import BeautifulSoup as bs
import difflib
import timeit



def crawlWeb(text):
	## crawl the web to similar document structure 
	search_string = ' '.join(text.split()[:32])
	req=requests.get("https://www.google.com/search?q="+search_string)
	soup=bs(req.text,'html.parser')
	results_temp=soup.find_all('span',class_="st")
	results=[]
	for i in results_temp:
		s=i.text
		s=s.replace('\n','')
		results.append(s)
	get_best_similarilty_score=getBestMatchGoogle(results,text)
	return get_best_similarilty_score

def getBestMatchGoogle(results,text):
	maximum=-1
	for i in results:
		if text in i: 
			maximum=100
		i = ' '.join(i.split()[:32])
		text = ' '.join(text.split()[:32])
		score=difflib.SequenceMatcher(None,i,text).ratio()*100
		if score>maximum:
			maximum=score
	return maximum

def getPlagiarismScore(text):
	## invoke all algorithms to get the final score for plagiarism
	score=crawlWeb(text)
	return score

start = timeit.default_timer()
b=getPlagiarismScore("The Universal Product Code (UPC) was adopted by the grocery industry in April 1973 as the standard barcode for all grocers, though it was not introduced at retailing locations until 1974.[2] This helped drive down costs for inventory management because retailers in the United States and Canada didn't have to purchase multiple barcode readers to scan competing barcodes. There was now one primary barcode for grocers and other retailers to buy one type of reader for.")
print(b)
stop = timeit.default_timer()
print(stop - start) 