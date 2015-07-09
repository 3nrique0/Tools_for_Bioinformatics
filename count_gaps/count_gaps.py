#! /usr/local/bioinfo/python/3.4.3/bin/python

## import libraries
from Bio import SeqIO
import re, argparse, sys

## Parse options
parser = argparse.ArgumentParser()

parser.add_argument("-f", "--fasta", dest="fastafile", type=str, default=None, help="Fasta file")
parser.add_argument("-o", "--output", dest="outfile", type=str, default=None, help="Output file")
parser.add_argument("-n", "--nucleotide", dest="nucleotide", type=str, default=None, help="Nucleotides you want to know the lenght")

args=parser.parse_args()



## Declare variables
spanlist = []
dicospan = {}
totaloccurrences = 0
#DEBUG:a = 0


## Import fasta and return a list with tuples containing
## the "start" and the "stop" of the stretch of one letter nucleotide
## The list for each fasta entry will be concatenated in a bigger list
with open(args.fastafile, 'rU') as handle:
	for record in SeqIO.parse(handle, "fasta") :
#DEBUG:		while a < 1 :
#DEBUG:			print(a)
#DEBUG:			a += 1
#DEBUG:			print(record.seq)
			spanlist = spanlist + [m.span() for m in re.finditer("["+args.nucleotide+"]+", str(record.seq))]
#DEBUG:			print(spanlist)


## Parse the list containing tuples (start, stop)
## Calculate the lenght of the stretch (stop-start)
## Add it to a dictionary, key = lenght of the stretch; value = number of occurences
for i in spanlist:
	diff = i[1]-i[0]
	totaloccurrences = totaloccurrences + diff
	if diff in dicospan.keys():
		dicospan[diff] = dicospan[diff] + 1
	else:
		dicospan[diff] = 1

#DEBUG:print(dicospan)


## Save to file
with open(args.outfile, 'w') as df:
	df.write('#Stretch_of_{0}\tNumber_of_occurrences\n'.format(args.nucleotide))
	for i in sorted(dicospan.keys()):
		df.write('{0}\t{1}\n'.format(i, dicospan[i]))
	df.write('#Total_{0}\t{1}\n'.format(args.nucleotide, totaloccurrences))
	
