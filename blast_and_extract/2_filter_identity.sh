#!/bin/bash

##	Declare a variable with the Path of all files

FILES=/homedir/ortegaabboud/burst/bioinfo_helpdesk/Yi/redox_genes_arabidopsis_20160614/output/*

##	Loop on listed files
for f in $FILES;

do

##	Rename the output file, chancge directory and replace ".fasta" with DBused
outfile=${f/.out/_filter_identity50.out};

echo "Processing: $outfile"
##	Filter blast results on identity greater or equal to 50%
awk '{if($3 >= 50) print $0}' $f > $outfile;

done

