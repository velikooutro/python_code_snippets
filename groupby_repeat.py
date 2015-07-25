'''
rep.txt =   1,a
			1,b
			2,a
			3,a
			3,b
			4,a
			5,a
			5,c
			6,c
			6,d
'''

from pprint import pprint
from itertools import groupby
import codecs
from textblob import TextBlob as tb

with open('rep.txt','r') as f:
	line = f.read()

tag_dict = {}
tag_dict_values = []
ww = []
def input_tags(infile):
    with codecs.open(infile,'r',encoding='utf-8',errors='ignore') as f:
        x = []
        for line in f:
            pid = line.split(',')[0]
            tag = line.split(',')[1]
            try:
                x = tb(str(pid)) + '\t' + tb(str(tag))
            except:
                x = tb(str(pid))
            try:
                both = {pid: x.split('\t')[1]}
            except:
                continue
            tag_dict.update(both)
            tag_dict_values.append(tag)
            words_tuple = pid,tag
            ww.append(words_tuple)

infile = 'rep.txt'
input_tags(infile)
outfile = 'rep_out.txt'

with codecs.open(outfile,'w',encoding='utf-8',errors='ignore') as f:
	for key, group in groupby(ww,lambda x: x[0]):
		listofThings = ','.join(['%s' %thing[1] for thing in group])
		tags = [t.strip() for t in listofThings.split(',')]
		# tags = tags.decode('utf-8')
		str1 = ','.join(tags).decode('utf-8')
		print key,' -- ',str1
		print >> f,'[',key,',[',str1,']]'

'''
RESULT
-------
[ 1 ,[ a,b ]]
[ 2 ,[ a ]]
[ 3 ,[ a,b ]]
[ 4 ,[ a ]]
[ 5 ,[ a,c ]]
[ 6 ,[ c,d ]]
'''
