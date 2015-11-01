import pandas as pd
import time
from collections import Counter


def FindW(query, queryset):
	count = 0
	# print 
	for term in query:
		count += queryset[term]

	# print query,count
	return count

def FindWeights():
	QueryData = pd.read_csv('Queries.csv')

	frequencies = {}

	termlist = []

	start = time.time()
	for terms in QueryData['ListOfTerms']:
		for term in terms.split(':'):
			termlist += [term]
	# print termlist
	end = time.time()
	print "termlist in", end-start

	start = time.time()
	FreqDist = Counter(termlist)

	end = time.time()
	print "FreqDist in", end-start

	for query in QueryData['ListOfTerms']:
		# start = time.time()
		try:
			W = FindW(query,FreqDist)
			# print W
			for term in query.split(':'):
				Wk = FreqDist[term]
				value = float(float(Wk) / float(W))
				if value < float(1):
					frequencies[term] = value
				else:
					frequencies[term] = float(0)
			# end = time.time()
		except ZeroDivisionError:
			continue
		# print query, 'in :',end-start

	freqlist = []
	for key in frequencies.keys():
		freqlist += [[key,frequencies[key]]]

	df = pd.DataFrame(freqlist,columns=['Term','Frequency'])

	df.to_csv('Frequency.csv',header=True,index=0)

	return frequencies

if __name__ == '__main__':
	FindWeights()

