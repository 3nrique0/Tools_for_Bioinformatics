#! /usr/local/bioinfo/python/3.4.3_build2/bin/python

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import argparse





	## To call the markers use args.marker
	## To call the the outfile use args.outfile
	## The files to be treated are in the list args.genotype_files

def strand():
	'''
	Find out in which sense the sequence is going.
	Strand + or strand - and creates a fasta record.
	If the strand is - the reverse complementary sequence is given.
	
	In this precise script this info is given in the subject's 
	protein fasta. 
	'''
	
	if coordinates[2] == '-':


		record = SeqRecord(Seq(str(recordGenome[scaff].seq[coordinates[0]:coordinates[1]].reverse_complement()),
			IUPAC.ambiguous_dna),
			id = str(protId),
			name = recordPep[protId].name,
			description = str(recordPep[protId].description )#+ " extrasequence=({0},{1})".format(plusNuc, minusNuc))
			)


	else:


		record = SeqRecord(Seq(str(recordGenome[scaff].seq[coordinates[0]:coordinates[1]]),
			IUPAC.ambiguous_dna),
			id = str(protId),
			name = recordPep[protId].name,
			description = str(recordPep[protId].description )#+ " extrasequence=({0},{1})".format(plusNuc, minusNuc))
			)
	
	return  record




def __main__():
	
	#################################
	## Parse arguments
	parser = argparse.ArgumentParser(description='''
				Slice a fasta sequence from the results of a blastp
				And using the "Scaffold + coordinates" name of the 
				protein to obtain the genomic fasta sequence + and 
				- some extra nucleotides determined by the user'
				''')
	
	parser.add_argument("-p", "--subjectProt", dest = "subjectProtHandle",
				type = str, default = None, 
				help = '''
				<str> File containing reference (subject) fasta sequence.
				File must be in fasta format. In this particular case it
				is a protein fasta file.
				'''
				)
				
	parser.add_argument("-g", "--subjectGenome", dest = "subjectGenometHandle",
				type = str, default = None, 
				help = '''
				<str> File containing reference (subject) genome fasta 
				sequence.
				'''
				)
				
	##	Soon to be used
	parser.add_argument("-b", "--blast", dest = "blastHandle",
				type = str, default = None, 
				help = '''
				<str> File containing result from blast.
				Format must be tsv, no headers.
				'''
				)

	##	Unused
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
	
	parser.add_argument("-u", "--upstream", dest = "upLen",
				type = int, default = 0, 
				help = '''
				<int> Length of the upstream (promoter) sequence
				'''
				)
				
	parser.add_argument("-d", "--downstream", dest = "dwLen",
				type = int, default = 0, 
				help = '''
				<int> Length of the downstream sequence
				'''
				)
								
# 	parser.add_argument("-f", "--files", metavar="files",
# 				type=str, default=None, 
# 				nargs='+', 
# 				help='''Put your genotype files in the order you want to treat them\n you can add as many files as'''
# 				)
	
	args=parser.parse_args()




# 	##########################################
# 	## START SCRIPT HERE
# 	## Check if mandatory options are well input


	##	Load Fastas:
	#recordPep = SeqIO.index("/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.pep.fas", "fasta")
	recordPep = SeqIO.index(args.subjectProtHandle, "fasta")
	#recordGenome = SeqIO.index("/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.fas", "fasta")
	recordGenome = SeqIO.index(args.subjectGenometHandle, "fasta")

	##	Assign scaffold that we will work with and lengths for the tests
	##	This will be looped into the reading of the blast.out
	protId = "scaffold4727_3605"
# 	plusNuc = 2000
# 	minusNuc = 2000


	##	Slice the description of the
	prot = recordPep[protId]
	locus = prot.description[ prot.description.find("locus=") : prot.description.find("length=") - 2 ]
	scaff = locus[ locus.find("=") + 1 : locus.find("(") ]
	coordinates = locus[ locus.find("(") + 1 : locus.find(")") ].split(",")
	coordinates[0], coordinates[1] = int(coordinates[0]), int(coordinates[1])

	##	Find strand and create fasta record,
	
# 	fastaSeq = strand()

	if coordinates[2] == '-':


		record = SeqRecord(Seq(str(recordGenome[scaff].seq[coordinates[0]-1:coordinates[1]].reverse_complement()),
			IUPAC.ambiguous_dna),
			id = str(protId),
			name = recordPep[protId].name,
			description = str(recordPep[protId].description )#+ " extrasequence=({0},{1})".format(plusNuc, minusNuc))
			)


	else:


		record = SeqRecord(Seq(str(recordGenome[scaff].seq[coordinates[0]-1:coordinates[1]]),
			IUPAC.ambiguous_dna),
			id = str(protId),
			name = recordPep[protId].name,
			description = str(recordPep[protId].description )#+ " extrasequence=({0},{1})".format(plusNuc, minusNuc))
			)


	with open(args.outputHandle, "w") as df:
		SeqIO.write(record, df, "fasta")


if __name__ == "__main__": __main__()

