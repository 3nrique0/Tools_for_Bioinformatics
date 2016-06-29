#! /usr/local/bioinfo/python/3.4.3_build2/bin/python


from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import glob
import argparse


parser= argparse.ArgumentParser(description="Gather fasta sequences from the matching results of a blast.")

parser.add_argument('--foo', help="foo help", )


recordPep = SeqIO.index("/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.pep.fas", "fasta")

path = "/homedir/ortegaabboud/burst/bioinfo_helpdesk/Yi/redox_genes_arabidopsis_20160614/output/"

fileList = glob.glob(path+"*.filterout")


for f in fileList:
	
	handle = open( f, "r")
	liste = handle.readlines()
	handle.close()
	
	handleOut = open( f.replace(".filterout",".pep.fasta"), "w")
	print("Gathering fasta sequence for:\t" + f)
	for i in liste:
		SeqIO.write(recordPep[i.split("\t")[1]], handleOut, "fasta")
	handleOut.close()

