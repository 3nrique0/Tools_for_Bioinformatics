# Tools_for_Bioinformatics
This are my custom made tools made mostly in python and bash to use them in my bioinformatics problems I encountered.
If there's a problem making them work or there any comments, please let me know.

## How i try to work:

  *Check that your shebang (#!) is correct, and change it accordingly
  *I try to remain as consistent as I can, although some changes may prevail, as I update to newer versions of python.
  *Sample datasets are still on going changes.

## Latest updates

**Work on zipped read files**


## Description of tools

### Treat reads

Use python to manipulate read files (fastq.gz) whithout unzipping them. The thing I wanted to do is to make it memory efficient, this tools are usually to be used only once, and what slows down the process is mostly the acces to disk data, therefore better to develop on a higher level object oriented language -- Yes, I know i'm not quite using the object oriented part... yet ! My scripts work on a line-by-line way, meaning the memory will not be saturated. :-)

#### Trim reads on 3 prime

So far I've not found a tool which allows to trim a read on 3' by telling it how many nucleotides you want to cut on the right side of the read. So, I made mine. This is particularly usefull when your reads are not of the same size. Tools so far only "keep a certain amount of reads on the left side, thus trimming the right end". This didn't fit my needs. So, there you go !

#### Random pick reads

Do you need to prepare a random dataset from existing data?  Do you need to create a sample file for your workshop? Lucky if you don't, but I do. So as I wanted to randomly pick reads from a file, and not just the head or the tail, I made my tool to do so:

It will randomly pick some reads without replacement. The requirements are the number of reads in your file and the number of reads you want to sample, as well as an input and output file. 







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

./4_extract_genomic_sequences.py -p /homedir/ortegaabboud/burst/test/gitstuff/Tools_for_Bioinformatics/Data/fasta_input/blast_extract_subject_peptide.fasta -g /homedir/ortegaabboud/burst/test/gitstuff/Tools_for_Bioinformatics/Data/fasta_input/blast_extract_subject_scaffold.fasta -b /homedir/ortegaabboud/burst/test/gitstuff/Tools_for_Bioinformatics/Data/blast_output/blast_extract_blast.out -o /homedir/ortegaabboud/burst/test/gitstuff/Tools_for_Bioinformatics/Data/fasta_output/output.fasta -u 20 -d 10


Run at home
python3.4 4_extract_genomic_sequences.py -p /media/enrique/Turing/Documents/testGit/Tools_for_Bioinformatics/Data/fasta_input/blast_extract_subject_peptide.fasta -g /media/enrique/Turing/Documents/testGit/Tools_for_Bioinformatics/Data/fasta_input/blast_extract_subject_scaffold.fasta -b /media/enrique/Turing/Documents/testGit/Tools_for_Bioinformatics/Data/blast_output/blast_extract_blast.out


First serious run:

There is a problem with the output, the size of the fasta is weird. I'll check out the detail after making run the full set of programs with -2000 and +2000 nucleotides
./4_extract_genomic_sequences.py -p /NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.pep.fas -g /NAS/NGS/Hevea/Genome/Reyan7-33-97/Hbgenome.fas -b /homedir/ortegaabboud/burst/bioinfo_helpdesk/Yi/redox_genes_arabidopsis_20160614/output/4-hydroxyphenylpyruvate_dioxygenase_blastp_on_Reyan_pep_identity50.filterout -o /homedir/ortegaabboud/burst/bioinfo_helpdesk/Yi/redox_genes_arabidopsis_20160614/output/4-hydroxyphenylpyruvate_dioxygenase_blastp_on_Reyan_pep_identity50.genomic.fasta
