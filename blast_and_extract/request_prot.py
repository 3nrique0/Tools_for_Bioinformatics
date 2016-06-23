
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import glob


recordPep = SeqIO.index("/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.pep.fas", "fasta")

path = "/homedir/ortegaabboud/burst/bioinfo_helpdesk/Yi/redox_genes_arabidopsis_20160614/output/"

for f in flieList:
	
	handle = open(path + f, "r")
	liste = handle.readlines()
	handle.close()
	
	handleOut = open(path + f.replace(".out",".fasta"), "w")
	for i in liste:
		SeqIO.write(recordPep[i.split("\t")[1]], handleOut, "fasta")
	handleOut.close()

