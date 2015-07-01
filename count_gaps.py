#! /usr/local/bioinfo/python/3.4.3/bin/python

# import libraries
from Bio import SeqIO
import re, argparse, sys


#outfile = "patate"
#fastafile = "/homedir/ortega-abboud/gemo/CRAC_v1.3.2/references/burkho/GY11_Burk_cdna.fasta"
#nucleotide = "A"




parser = argparse.ArgumentParser()

parser.add_argument("-f", "--fasta", dest="fastafile", type=str, default=None, help="Fasta file")
parser.add_argument("-o", "--output", dest="outfile", type=str, default=None, help="Output file")
parser.add_argument("-n", "--nucleotide", dest="nucleotide", type=str, default=None, help="Nucleotides you want to know the lenght")

args=parser.parse_args()



spanlist = []
dicospan = {}

#DEBUG:
a = 0

with open(args.fastafile, 'rU') as handle:
	for record in SeqIO.parse(handle, "fasta") :
#DEBUG:
		while a < 1 :
#DEBUG:
			print(a)
#DEBUG:
			a += 1
#DEBUG:
			print(record.seq)
			spanlist = spanlist + [m.span() for m in re.finditer("["+args.nucleotide+"]+", str(record.seq))]
#DEBUG:
			print(spanlist)



for i in spanlist:
	diff = i[1]-i[0]
	if diff in dicospan.keys():
		dicospan[diff] = dicospan[diff] + 1
	else:
		dicospan[diff] = 1

print(dicospan)

with open(args.outfile, 'w') as df:
	df.write('Strands of {0}\tNumber of occurrences\n'.format(args.nucleotide))
	for i in sorted(dicospan.keys()):
		df.write('{0}\t{1}\n'.format(i, dicospan[i]))
	