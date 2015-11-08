import pandas as pd
import time
from collections import Counter
import operator

x = 7

def GetWeights():
	print 'Fetching from file...'
	start =time.time()
	freq = pd.read_csv('Data/Frequency.csv')
	end = time.time()
	print 'Fetched data in :',end-start
	print 'Fetched',freq.shape[0],'lines.'

	return freq

def GetDwellTime():
	print 'Fetching dwell times...'
	start = time.time()
	clickdat = pd.read_csv('Data/Click.csv')
	end = time.time()
	print 'Data fetched in :',end-start
	print 'Fetched',clickdat.shape[0],'lines'

	return clickdat

def GetQueries():
	print 'Fetching Query Data...'
	start = time.time()
	querydat = pd.read_csv('Data/Queries.csv')
	end = time.time()
	print 'Data fetched in :',end-start
	print 'Fetched',querydat.shape[0],'lines'

	return querydat

def ReRank():

	freq = GetWeights()
	clickdat = GetDwellTime()
	querydat = GetQueries()

	weight = {}
	rank0 = []
	print 'Re ranking URLs...'
	start = time.time()
	k = 0
	for query in querydat['ListOfURLsAndDomains']:
		url = query.split(':')[0]
		if not url in rank0:
			rank0 += [url]

		beta = 4

		for i in rank0:
			try:
				indexlist = clickdat[clickdat['URLID']==float(i)].index.tolist()
				dwellsum = 0
				for i in indexlist:
					dwellsum += clickdat['TimePassed'][i]
			except IndexError:
				print 'Value not found for',i,':('
		
		for i in rank0:
			weight[i] = float(float(float(beta)/float(rank0.index(i) + 1)) * dwellsum)

		k+=1
		if k>x:
			break

	rank = sorted(weight.items(), key=operator.itemgetter(1))
	end = time.time()
	print 'Ranks calculated in :',end-start

	print 'Initial Ranks :'
	for i in rank0:
		print i,':',rank0.index(i)+1

	print 'Re ranked to : (Printed in ascending order)'
	for i in rank:
		print i


if __name__ == '__main__':
	ReRank()

