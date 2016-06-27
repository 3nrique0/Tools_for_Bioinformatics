# Tools_for_Bioinformatics
This are my custom made tools made mostly in python and bash to use them in my bioinformatics problems I encountered.
If there's a problem making them work or there any comments, please let me know.

########
DATA
The sample data is kept in the Data directory. It is organised in Input and Output, the inputs will thusly available for all tools. These sample data files will be as small as possible to help run the tests as fast as possible.

DATA INPUT

Data/Input/blast_corrected.out
	Blast result of an A. thaliana gene (mRNA) blastn on the reference rim600.
	The result has been manualy curated to "fuse" both segmented results of the blast.
	Indicating that probably this gene may composed of more than 1 exon.
	

########

BLAST_AND_EXTRACT

Example usage of commands, :

4_extract_genomic_sequences.py Allows to slice a genomic fasta sequence depending on the coordinates which have been given to it. 

Set your cwd to Tools_for_Bioinformatics/blast_and_extract/

Run at cluster
python 4_extract_genomic_sequences.py -p ../Data/fasta_input/blast_extract_subject_peptide.fasta -g ../Data/fasta_input/blast_extract_subject_scaffold.fasta -o ../Data/fasta_output/output.fasta -u 20 -d 10

Run at home
python3.4 4_extract_genomic_sequences.py -p /media/enrique/Turing/Documents/testGit/Tools_for_Bioinformatics/Data/fasta_input/blast_extract_subject_peptide.fasta -g /media/enrique/Turing/Documents/testGit/Tools_for_Bioinformatics/Data/fasta_input/blast_extract_subject_scaffold.fasta -b /media/enrique/Turing/Documents/testGit/Tools_for_Bioinformatics/Data/blast_output/blast_extract_blast.out

