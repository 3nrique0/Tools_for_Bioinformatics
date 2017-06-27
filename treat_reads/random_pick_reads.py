#!/usr/bin/python3.5

# Author: Enrique ORTEGA

## IMPORT LIBRARIES
import gzip
import argparse
import random






## MAIN FUNCTION, ARGUMENT IS THE ARGS OBJECT FROM THE OTHER FUNCTION
def run(args):

    ## CHECK IF READS TO BE SAMPLE ARE EQUAL OR LESS THAN TOTAL READS
    try:
        args.readsToSample <= args.totalReads
    except ValueError:
        print("ERROR: the amount of reads to sample is larger than the reads in the fastq.gz file")
        # break



    ## GET AND SORT THE NUMBER OF THE INDEXES OF THE READS TO SAMPLE
    popRange = range(1, args.totalReads, 1)
    unsortedList = random.sample(popRange, args.readsToSample)
    sortedList = sorted(unsortedList)


    ## OPEN INPUT AND OUTPUT FILES
    fhin = gzip.open(args.infile, 'rb')
    fhout = gzip.open(args.outfile, 'wb')


    ## THIS LOOP ALLOWS TO READ THE READ FILE 4 LINES AT A TIME (A READ)
    ## IT WILL SAVE THE RANDOMLY SELECTED READS INTO A FILE
    ## IT WILL STOP WHEN THE LAST READ OF THE RANDOM LIST WILL BE SAVED

    for i in range(0, sortedList[-1] +1 ):

        name = fhin.readline()
        sequence = fhin.readline()
        third = fhin.readline()
        quality = fhin.readline()

        if i in sortedList:
            outList = [name, sequence, third, quality]
            fhout.writelines(outList)


    ### CREATE EXIT VALUE FOR THE LOOP
    #name = 1

    ### REPLACE WITH AN ITERATIVE LOOP
    #while name != b'':

        ### IMPORT A FULL READ -- 4 LINES
        #name = fhin.readline()
        #sequence = fhin.readline()
        #third = fhin.readline()
        #quality = fhin.readline()

        ### TRIM THE SEQUENCE AND THE QUALITY
        #sequence = sequence[0:len(sequence)-n] + sequence[len(sequence)-1:len(sequence)]
        #quality = quality[0:len(quality)-n] + quality[len(quality)-1:len(quality)]

        ### CONCATENATE THE 4 LINES OF THE READ INTO A LIST
        #outList = [name, sequence, third, quality]

        ### SAVE THE READ USING THE LIST
        #fhout.writelines(outList)

    ## CLOSE FILES
    fhin.close()
    fhout.close()

    ## IF THE USER WANTS VERBOSE MODE, THIS WILL PRINT SOME INFO
    if args.verbose == True:
        print("File {0} trimmed {1} nucleotides.\nOutput in: {2}, ".format(args.infile, args.trim, args.outfile))



## FUNCTION TO TREAT ALL THE ARGUMENTS GIVEN, AND RETURN THEM IN THE OBJECT ARGS
def main():
    '''
    This function treats all the arguments and puts them
    into a variable named args.
    This variable can later be used to run the other functions.
    '''
    parser = argparse.ArgumentParser(description='''This function will sample randomly reads from a fastq gziped file. The sampling is without replacement.

    It is made to work with indexes and only sample the reads from their index, therefor it requires little memory to sample reads from a big file without unzipping it.
    ''')


    parser.add_argument('-in',
                    dest='infile',
                    type=str,
                    required=True,
                    help='Fastq file compressed with gzip')


    parser.add_argument('-out',
                    dest='outfile',
                    type=str,
                    required=True,
                    help='''Output will be a fastq file compressed with gzip''')


    parser.add_argument('-numreads',
                    dest='totalReads',
                    type=int,
                    required=True,
                    help='''Number of reads in the fq.gz file.
                        To count the number of reads in a compressed file run:
                        $ zcat <FILE.fq.gz> | wc -l | awk '{print $1 / 4}' ''' )


    parser.add_argument('-sample',
                    dest='readsToSample',
                    type=int,
                    required=True,
                    help='''Number of reads to be sampled.
                    It must be less than the number of total reads in that file.''' )


    parser.add_argument('-v',
                    dest='verbose',
                    type=bool,
                    default=False,
                    help='''Prints information about the trimming once it has been finished''')


    ## THIS IS SUPPOSED TO RUN THE OTHER FUNCTION.. BUT IT DOESN'T
    parser.set_defaults(func=run)

    ## CREATE AND RETURN THE OBJECT ARGS CONTAINING ALL THE ARGUMENTS
    args = parser.parse_args()
    return args


## RUN PROGRAM HERE
if __name__=="__main__":

    ## PROCESS ALL THE ARGUMENTS AND PUT THEM IN A VARIABLE
    truc = main()

    ## RUN THE MAIN PROGRAM USING THE ARGUMENTS PROVIDED
    run(truc)
