#! /usr/local/bioinfo/python/3.4.3_build2/bin/python

import sys
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import argparse



def __main__():

	#################################
	## Parse arguments
	parser = argparse.ArgumentParser(description='''
				Slice a fasta sequence from the results of a blast
				''')
	
	parser.add_argument("-s", "--subject", dest = "subjectHandle",
				type = str, default = None, 
				help = '''
				<str> File containing reference (subject) fasta sequence.
				File must be in fasta format
				'''
				)
	
	parser.add_argument("-b", "--blast", dest = "blastHandle",
				type = str, default = None, 
				help = '''
				<str> File containing result from blast.
				Format must be tsv, no headers.
				'''
				)

	parser.add_argument("-q", "--query", dest = "queryFastaHandle",
				type = str, default = None, 
				help = '''
				<str> File containing fasta sequences.
				It's the same containign the query sequences
				used in the blast
				'''
				)

	parser.add_argument("-o", "--output", dest = "outputHandle",
				type = str, default = "output.fasta", 
				help = '''
				<str> Name of output fasta file 
				defaut= "output.fasta"
				'''
				)
	
	parser.add_argument("-p", "--promoter", dest = "promLen",
				type = int, default = 2000, 
				help = '''
				<str> Name of output fasta file 
				defaut= "output.fasta"
				'''
				)
# 	parser.add_argument("-f", "--files", metavar="files",
# 				type=str, default=None, 
# 				nargs='+', 
# 				help='''Put your genotype files in the order you want to treat them\n you can add as many files as'''
# 				)
	
	args=parser.parse_args()

	## To call the markers use args.marker
	## To call the the outfile use args.outfile
	## The files to be treated are in the list args.genotype_files
	
# 	##########################################
# 	
# 	## START SCRIPT HERE
# 	## Check if mandatory options are well input

	# to be done


	## IMPORT BLAST DATA, CREATE STRAND COLUMN

	blastHeader = ['qId','sId','identity','alignmentLength','mismatches','gapOpens','qStart','qEnd','sStart','sEnd','evalue','bitScore']
	
	blastResult = pd.read_csv(args.blastHandle, sep="\t", header=0, names=blastHeader)

	blastResult['codingStrand'] = blastResult['sStart'] < blastResult['sEnd']	


	## IMPORT FASTA FROM SUBJECT
	subjectIndex = SeqIO.index(args.subjectHandle, "fasta")


	#####################################
	#####################################

	#### Scripting for single use @ RIM600
	outHandle = open(args.outputHandle, "w")
	outHandle.close()


	## HAND MADE DATA.FRAME TO PARSE DATA

	### BLAST RESULT WITH RIM600
# 	subjectListe = ['gi|461632731|gb|KB626928.1|','gi|461664072|gb|KB618043.1|','gi|461647759|gb|KB622456.1|','gi|461668479|gb|KB616792.1|']
# 	queryListe = ['CL432Contig1_HbPR-1', 'SSHE3-04_C10_T7_HbDefesin', 'SSHF3-02_D03_T7_Hb_beta_1,3Glucanase', 'gi|20135537|gb|AY057860.1|']
# 	startCoord = [19729, 214800, 9983, 87442]
# 	strand = ["-", "-", "+", "+"]


	subjectListe = ["gi|461632731|gb|KB626928.1|", "gi|461664072|gb|KB618043.1|", "gi|461647759|gb|KB622456.1|", "gi|461668479|gb|KB616792.1|"]
	queryListe = ["CL432Contig1_HbPR-1", "SSHE3-04_C10_T7_HbDefesin", "SSHF3-02_D03_T7_Hbβ1,3Glucanase", "gi|20135537|gb|AY057860.1|"]
	startCoord = [20358, 215368, 9983, 87442]
	strand = ["-", "-", "+", "+"]

	for i in range(0,len(subjectListe)):
		
		## PRINT FOR TEST
		print("\n###")
		print(i, subjectListe[i], queryListe[i],  startCoord[i], strand[i])
		print("\n")
		print(subjectIndex[subjectListe[i]])
		print("\n")
		print(subjectIndex[subjectListe[i]].seq[0:20])
		print(subjectIndex[subjectListe[i]].seq[0:20].reverse_complement())
		print(type(subjectIndex[subjectListe[i]].seq[0:20]))
		

		## IN CASE OF NEGATIVE SRAND
		if strand[i] == '-':


			record = SeqRecord(Seq(str(subjectIndex[subjectListe[i]].seq[startCoord[i]-args.promLen:startCoord[i]].reverse_complement()),
					IUPAC.ambiguous_dna),
					id = "prom-" + str(queryListe[i]),
					name="promoter_" + str(queryListe[i]),
					description="fragment from {0} ({1}:{2}) | Strand {3}".format(subjectListe[i], startCoord[i] - 2000, startCoord[i], strand[i]))

	
		## IN CASE OF POSITIVE STRAND
		else:
			record = SeqRecord(Seq(str(subjectIndex[subjectListe[i]].seq[startCoord[i]-args.promLen:startCoord[i]]),
					IUPAC.ambiguous_dna),
					id = "prom-" + str(queryListe[i]),
					name="promoter_" + str(queryListe[i]),
					description= "fragment from {0} ({1}:{2}) | Strand {3}".format(subjectListe[i], startCoord[i] - 2000, startCoord[i], strand[i])
					)


		print("\n")
		print(record)
		
		## SAVE SEQUENCE TO FILE
		outHandle = open(args.outputHandle, "a")
		SeqIO.write(record, outHandle, "fasta")
		outHandle.close()



if __name__ == "__main__": __main__()

