#!/usr/bin/python3.5

# Author: Enrique ORTEGA

## IMPORT LIBRARIES
import gzip
import argparse


## MAIN FUNCTION, ARGUMENT IS THE ARGS OBJECT FROM THE OTHER FUNCTION
def run(args):

    ## ADD 1 BECAUSE OF THE END LINE CHARACTER
    n = args.trim +1

    ## OPEN INPUT AND OUTPUT FILES
    fhin = gzip.open(args.infile, 'rb')
    fhout = gzip.open(args.outfile, 'wb')

    ## CREATE EXIT VALUE FOR THE LOOP
    name = 1

    while name != b'':

        ## IMPORT A FULL READ -- 4 LINES
        name = fhin.readline()
        sequence = fhin.readline()
        third = fhin.readline()
        quality = fhin.readline()

        ## TRIM THE SEQUENCE AND THE QUALITY
        sequence = sequence[0:len(sequence)-n] + sequence[len(sequence)-1:len(sequence)]
        quality = quality[0:len(quality)-n] + quality[len(quality)-1:len(quality)]

        ## CONCATENATE THE 4 LINES OF THE READ INTO A LIST
        outList = [name, sequence, third, quality]

        ## SAVE THE READ USING THE LIST
        fhout.writelines(outList)

    ## CLOSE FILES
    fhin.close()
    fhout.close()

    ## IF THE USER WANTS VERBOSE MODE, THIS WILL PRINT SOME INFO
    if args.verbose == True:
        print("File {0} trimmed {1} nucleotides.\nOutput in: {2}, ".format(args.infile, args.trim, args.outfile))



## FUNCTION TO TREAT ALL THE ARGUMENTS GIVEN, AND RETURN THEM IN THE OBJECT ARGS
def main():
    parser = argparse.ArgumentParser(description="Nice description here")

    parser.add_argument('-trim',
                    dest='trim',
                    type=int,
                    required=True,
                    help='Do potatoes, potate ?' )

    parser.add_argument('-in',
                    dest='infile',
                    type=str,
                    required=True,
                    help='Fastq file compressed with gzip')

    parser.add_argument('-out',
                    dest='outfile',
                    type=str,
                    required=True,
                    help='Output will be a fastq file compressed with gzip')

    parser.add_argument('-v',
                    dest='verbose',
                    type=bool,
                    default=False,
                    help='Prints information about the trimming once it has been finished')

    ## THIS IS SUPPOSED TO RUN THE OTHER FUNCTION.. BUT IT DOESN'T
    parser.set_defaults(func=run)

    ## CREATE AND RETURN THE OBJECT ARGS CONTAINING ALL THE ARGUMENTS
    args = parser.parse_args()
    return args


## RUN PROGRAM HERE
if __name__=="__main__":

    ## PROCESS ALL THE ARGUMENTS AND PUT THEM IN A VARIABLE
    truc = main()

    ## RUN THE MAIN PROGRAM USING THE ARGUMENTS FROM THE PREVIOUS DEFINITION
    run(truc)
