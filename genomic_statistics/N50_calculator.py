#! /usr/local/bioinfo/python/3.4.3_build2/bin/python

## Script to calculate N50 or N90 (or any other) from a fasta file.
## N50 calculated as defined here :
## https://en.wikipedia.org/wiki/N50,_L50,_and_related_statistics#N50

## Made in python 3.4.3

## Script realised in august 2016, by Enrique Ortega Abboud at Cirad, AGAP, BURST team

## Dev to do:

## A)
## Later I'd love to output a small histogram of the distribution of scaffold lenghts
## Which would include a vertical line on the desired N*

## B)
## Add optional: verbose (stdout) and output file

############################
## IMPORT LIBRARIES
############################

from Bio import SeqIO
import numpy as np
#import matplotlib.mlab as mlab
#import matplotlib.pyplot as plt
import argparse



############################
## TREAT ARGUMENTS
############################

parser = argparse.ArgumentParser(
	prog = '''N50 Calculator''',
	description = '''Calculate N50, N90 or any N* from a fasta file'''
	)

parser.add_argument("-f", "--fasta", type = str, dest = "fastaHandle"
	, default = None
	, help = '''Name of input fasta file'''
	)

parser.add_argument("-N", type = int, dest = "n"
	, default = 50
	, help = '''Integer (def=50), The integer of the percentil you want as N*'''
	)

args = parser.parse_args()


############################
## IMPORT FASTA FILE
############################

fastaIndex = SeqIO.index(args.fastaHandle, 'fasta')

print("File opened: {0}".format(args.fastaHandle))
print("N requested: {0}".format(args.n))



###########################
## FIND N50
###########################

## CALCULATE TOTAL SIZE OF GENOME
genomeSize = 0
for i in sorted(fastaIndex.keys()):
	genomeSize = genomeSize + len(fastaIndex[i])

var =  0
percentil = args.n/100.

for i in reversed(sorted(fastaIndex.keys())):
	var = var + len(fastaIndex[i])
	if var >= genomeSize * percentil:
		scaff = i
		scaffLen = len(fastaIndex[i])
		print("Genome Size: {0}".format(genomeSize))
		print("var={0}; 50%g={1}".format(var, genomeSize * percentil))
		print("Scaffold containing the requested percentil: {0}".format(i))
		print("N{0}: {1}".format(args.n, len(fastaIndex[i])))
		break




