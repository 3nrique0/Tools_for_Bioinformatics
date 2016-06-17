#!/bin/bash

module load compiler/gcc/4.9.2 bioinfo/ncbi-blast/2.2.30
sleep 5s

##	 Declare a variable with the Path of all files
FILES=/homedir/ortegaabboud/burst/bioinfo_helpdesk/Yi/redox_genes_arabidopsis_20160614/input/*

##	Loop on listed files
for f in $FILES; 

do 
##	Rename the output file, chancge directory and replace ".fasta" with DBused
outfile=${f/input/output};
outfile=${outfile/.fasta/_blastp_on_Reyan.pep.out}
##	Rename process name for qsub output/error files
procname=${f%.fasta};
procname=${procname##*/};

##	Print on screen which file is being launched to keep trace of what has been done
echo "processing $procname ..."; 

##	Launch blastp on the cluster, result in tab format no headers
qsub -b y -V -q normal.q -N blastp blastp -db /homedir/ortegaabboud/burst/blastdb/Reyan7-33-97_pep -query $f -out $outfile -outfmt 6 -evalue 1e-20 -threshold 150;

done

