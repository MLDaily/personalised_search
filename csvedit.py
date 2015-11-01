import pandas as pd

filereader = pd.read_csv('test.csv', chunksize=1000, sep='\t', \
    names=['SessionID','TimePassed','TypeOfRecord','SERPID',\
    'QueryID','ListOfTerms','ListOfURLsAndDomains'])

count = 0

columns = ['SessionID','TimePassed','TypeOfRecord','SERPID','QueryID',\
        'ListOfTerms','ListOfURLsAndDomains']

ls = []

for row in filereader:
    row = row[columns]
    for k in row.itertuples():
        k = list(k)
        if 'Q' in k or 'T' in k:
            temp = str(k[6]).split(',')
            k[6] = ':'.join(temp)
            temp = str(k[7]).split(',')
            k[7] = ':'.join(temp)
            ls += [k[1:]]


df = pd.DataFrame (ls, columns=columns)

df.to_csv('Queries.csv',header=True,index=0)

# print df