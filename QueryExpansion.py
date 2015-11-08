import pandas as pd
import time
from collections import Counter

def FindW(query, queryset):
	count = 0
	for term in query:
		count += queryset[term]
	return count

def FindWeights():
	print 'Fetching Data...'
	start = time.time()
	QueryData = pd.read_csv('Data/Queries.csv')
	end = time.time()
	print 'Data Fetched in :',end-start

	frequencies = {}

	termlist = []

	print 'Fetching List of terms ...'
	start = time.time()
	for terms in QueryData['ListOfTerms']:
		for term in terms.split(':'):
			termlist += [term]
	# print termlist
	end = time.time()
	print "termlist in :", end-start

	print "Finding Frequency Distributuion.."
	start = time.time()
	FreqDist = Counter(termlist)
	end = time.time()
	print "FreqDist in", end-start

	print "Getting frequencies / weights...."
	start = time.time()
	for query in QueryData['ListOfTerms']:
		try:
			W = FindW(query,FreqDist)
			for term in query.split(':'):
				Wk = FreqDist[term]
				value = float(float(Wk) / float(W))
				frequencies[term] = value
		except ZeroDivisionError:
			continue
	end = time.time()
	print "Values calculated in :",end-start

	m = max(frequencies.values())

	print "Entering data into file..."
	start = time.time()
	freqlist = []
	for key in frequencies.keys():
		freqlist += [[key,float(float(frequencies[key])/float(m))]]

	df = pd.DataFrame(freqlist,columns=['Term','Frequency'])

	df.to_csv('Data/Frequency.csv',header=True,index=0)
	end = time.time()
	print "Entered into file in :",end-start

	return frequencies

if __name__ == '__main__':
	FindWeights()

