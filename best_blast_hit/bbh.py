#! /usr/bin/python3.5

import pandas as pd
import argparse


dfTest = pd.DataFrame({'id' : [1,1,1,2,2,3,3,3,3,4,4,5,6,6,6,7,7],
    'value'  : ["first","second","second","first",
    "second","first","third","fourth",
    "fifth","second","fifth","first",
    "first","second","third","fourth","fifth"]})


#### ARGUMENTS HAVE TO BE RE-WORKED ON
# def __main__():
# 	parser = argparse.ArgumentParser(description='''
#         Get only best blast hit (BBH) output from blast results''')
#
# 	parser.add_argument("-f", "--file output", dest="blastHandle",
#         type=str, default=None,
#         help='''Blast output file (blast outfmt 6 only)\n''')
#
#
# 	args=parser.parse_args()
#     df = pd.read_csv(args.blastHandle, sep="\t")
#
#
#     print(df)
#
# if __name__ == "__main__": __main__()


## VARIABLES:
inputFile = "batch_1_uniq_blastx_eval1_outfmt6.out"
evalueMax = 1e-4

blastHeader = ['queryId', 'subjectId', 'identity', 'alignmentLength', 'mismatches', 'gapOpens', 'qStart', 'qEnd', 'sStart', 'sEnd', 'evalue', 'bitScore']

## LOAD BLAST OUTPUT FILE
with open(inputFile,'r') as blastHandle:
    df = pd.read_csv(blastHandle, sep="\t", names=blastHeader)

## TAKE ONLY THE FIRST LINE FOR EACH QUERY ID == TAKE ONLY BEST BLAST HIT
df2 = df.groupby('queryId').first()


with open(inputFile+'.bbh', 'w') as outFile:
    df2.to_csv(outFile, sep='\t')

print('Ta Daaaaa')

## COMMAND TO FILTER ON A COLUMN WITH SOME GIVEN PARAMETERS
#df3 = df2[df2['evalue'] < evalueMax ]

## ALWAYS LOL ON THE BRIGHT SIDE OF LIFE ^_^
#subjectIdUniq = list(set(sorted(df3['subjectId'])))
