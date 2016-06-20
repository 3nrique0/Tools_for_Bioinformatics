#! /usr/local/bioinfo/python/3.4.3_build2/bin/python

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import argparse

##	Load Fastas:
recordPep = SeqIO.index("/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.pep.fas", "fasta")
recordGenome = SeqIO.index("/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.fas", "fasta")

##	Assign scaffold that we will work with
protId = "scaffold4727_3605"
plusNuc = 2000
minusNuc = 2000

##	Slice the description of the
prot = recordPep[protId]
locus = prot.description[ prot.description.find("locus=") : prot.description.find("length=") - 2 ]
scaff = locus[ locus.find("=") + 1 : locus.find("(") ]
coordinates = locus[ locus.find("(") + 1 : locus.find(")") ].split(",")
coordinates[0], coordinates[1] = int(coordinates[0]), int(coordinates[1])


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


with open("outfile.fasta", "w") as df:
	SeqIO.write(record, outHandle, "fasta")

