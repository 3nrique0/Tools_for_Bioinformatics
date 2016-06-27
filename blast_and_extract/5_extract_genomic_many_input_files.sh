#!/bin/bash

##	Declare a variable with the Path of all files

FILES=/homedir/ortegaabboud/burst/bioinfo_helpdesk/Yi/redox_genes_arabidopsis_20160614/output/*.filterout
genome=/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.fas
peptides=/NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.pep.fas
upstream=20

##	Loop on listed files
for f in $FILES;

do

##	Rename the output file, chancge directory and replace ".fasta" with DBused
outfile=${f/.blastout/_identity50.filterout};

##	Execute python script
python 4_extract_genomic_sequences.py -p $peptides -g $genome -o $outfile -b $f  -u 20 -d 10;

##	Echo file, remove when working on the cluster
echo "Finding genomic fasta for...  $f";

done
