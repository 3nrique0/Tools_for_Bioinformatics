#! /usr/local/bioinfo/python/3.4.3/bin/python

# import libraries
from Bio import SeqIO

outfile = "patate"
fastafile = "/homedir/ortega-abboud/gemo/CRAC_v1.3.2/references/burkho/GY11_Burk_cdna.fasta"

with open(outfile, 'w') as df, open(fastafile, 'rU') as handle:
	for record in SeqIO.parse(handle, "fasta") :
		#print('{1}\t{0}'.format(record.id, len(record)))
		df.write('{0}\t{1}\n'.format(record.id, len(record)))
		

