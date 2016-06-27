#! /usr/local/bioinfo/python/3.4.3_build2/bin/python

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import pandas as pd
import argparse





def strand():
	'''
	Find out in which sense the sequence is going.
	Strand + or strand - and creates a fasta record.
	If the strand is - the reverse complementary sequence is given.
	
	In this precise script this info is given in the subject's 
	protein fasta. 
	'''
#	print("---------")
#	coordinatesVerified
#	print("---------")

	if coordinatesVerified[2] == '-':


		record = SeqRecord(Seq(str(recordGenome[scaff].seq[ coordinatesVerified[0] : coordinatesVerified[1]].reverse_complement()),
			IUPAC.ambiguous_dna),
			id = str(protId),
			name = recordPep[protId].name,
			description = str(recordPep[protId].description )#+ " extrasequence=({0},{1})".format(plusNuc, minusNuc))
			)


	else:


		record = SeqRecord(Seq(str(recordGenome[scaff].seq[ coordinatesVerified[0] : coordinatesVerified[1] ]),
			IUPAC.ambiguous_dna),
			id = str(protId),
			name = recordPep[protId].name,
			description = str(recordPep[protId].description )#+ " extrasequence=({0},{1})".format(plusNuc, minusNuc))
			)
	
	return  record




#####
##	Find which strand of the blast match on the subject (reference)
##	The input are s.start and s.end
##	If s.start < s.end, strand = +
##	if s.end < s.start, strand = -
def verifyCoordinatesFromBlastOutput():
	'''
	Check if the coordinates with the -upStream and +dwStream <int>
	are into the limits of the size of the scaffold.
	If they are not, the coordinates will be adjusted to 1 and to the last
	character of the scaffold.
	'''
	##	Work if strand is + or -
	if coordinates[2] == '-':
		if (coordinates[1] +args.upStream) > (len(recordGenome[scaff]) - 1) :
			## Impose max value of the scaffold
			leftCoord = (len(recordGenome[scaff]) - 1)
		else:
			leftCoord = coordinates[1] +args.upStream

		if (coordinates[0] -1 -args.dwStream) < 1 :
			##	Impose min value of the scaffold
			rightCoord = 1
		else:
			rightCoord = (coordinates[0] -1 -args.dwStream)


	if coordinates[2] == '+':


		if (coordinates[0] -1 -args.upStream) < 1 :
			##	Impose min value of the scaffold
			leftCoord = 1
		else:
			leftCoord = (coordinates[0] -1 -args.upStream)


		if (coordinates[1] +args.dwStream) > (len(recordGenome[scaff]) - 1) :
			##	 Impose max value of the scaffold
			rightCoord = (len(recordGenome[scaff]) - 1)
		else:
			rightCoord = (coordinates[1] +args.dwStream)

	return [leftCoord, rightCoord, coordinates[2]]



def verifyCoordinates():
	'''
	Verify that coordinates on the format [star, end, strand]
	don't have coordinates outside the scaffold where they belong
	when the user wants to have upstream and downstream sequences.

	This is format of writting coordinates is close to that of a GFF file
	'''

	if (coordinates[0] -1 -args.upStream) < 1 :
		##	Impose min value of the scaffold
		leftCoord = 1
	else:
		leftCoord = (coordinates[0] -1 -args.upStream)


	if (coordinates[1] +args.dwStream) > (len(recordGenome[scaff]) - 1) :
		##	 Impose max value of the scaffold
		rightCoord = (len(recordGenome[scaff]) - 1)
	else:
		rightCoord = (coordinates[1] +args.dwStream)

	return [leftCoord, rightCoord, coordinates[2]]



def __main__():


	#################################
	##	Declare global variables
	global args, recordPep, recordGenome, protId, prot, locus, scaff
	global coordinates, coordinatesVerified


	#################################
	##	Parse arguments
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
	
	parser.add_argument("-u", "--upstream", dest = "upStream",
				type = int, default = 0, 
				help = '''
				<int> Length of the upstream (promoter) sequence
				'''
				)
				
	parser.add_argument("-d", "--downstream", dest = "dwStream",
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
	## To call the markers use args.marker
	## To call the the outfile use args.outfile
	## The files to be treated are in the list args.genotype_files
	

	args=parser.parse_args()





# 	##########################################
# 	## START SCRIPT HERE
# 	## Check if mandatory options are well input


	##	Load Fastas:
	#recordPep = SeqIO.index("/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.pep.fas", "fasta")
	recordPep = SeqIO.index(args.subjectProtHandle, "fasta")
	#recordGenome = SeqIO.index("/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.fas", "fasta")
	recordGenome = SeqIO.index(args.subjectGenometHandle, "fasta")

	##	Load Blast result:
	blastResult = pd.read_csv(args.blastHandle, sep = '\t', header = None)

	

	##	Assign scaffold that we will work with and lengths for the tests
	##	This will be looped into the reading of the blast.out
	protId = "scaffold4727_3605"
	


	##	Slice the description of the
	prot = recordPep[protId]
	locus = prot.description[ prot.description.find("locus=") : prot.description.find("length=") - 2 ]
	scaff = locus[ locus.find("=") + 1 : locus.find("(") ]
	coordinates = locus[ locus.find("(") + 1 : locus.find(")") ].split(",")
	coordinates[0], coordinates[1] = int(coordinates[0]), int(coordinates[1])

	coordinatesVerified = verifyCoordinates()

	##	Find strand and create fasta record,
	fastaSeq = strand()



	print(fastaSeq)
	print("\n##")
	print("Sequence extracted from {0} to {1} in the strand {2}".format(coordinatesVerified[0], coordinatesVerified[1], coordinatesVerified[2]))
		


	with open(args.outputHandle, "w") as df:
		SeqIO.write(fastaSeq, df, "fasta")



if __name__ == "__main__": __main__()

