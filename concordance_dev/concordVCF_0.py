#!/usr/local/bioinfo/python/3.4.3_build2/bin/python
import argparse



def skim_comments(line, header, file_handle):
	'''
	Input = line from VCF,
	Passes and reads the next line if there are headers (/^##/)
	Return header when found (/^#C/)
	Return line splited in list
	'''
	

	## Pass if line starts with ##
	while line[0:2] == "##":
		line = file_handle.readline()
	
	## Get the header and modify the list that has been already created
	while line[0:2] == "#C":
		line = line.replace('\n','')
#		line = line.replace('#','')
		header = line.split('\t')
		line = file_handle.readline()
		
	
	## Split line
	else:
		line = line.replace('\n','')
		return_line = line.split('\t')
#		print("Zhu Li, do the thing with the line {0}".format(line))
	
	return return_line, header



def finish_it(line1, line2, file_handle_1, file_handle_2):
	'''
	Inputs the handles of both VCF files.
	Checks which file has already arrived to the end,
	and prints the rest of the lines of the other file.
	
	Target: attribute these lines as "file specific".
	'''

#DEBUG:
	print('##### inside finish_it')
#DEBUG:		print('line 1 : {0}'.format(line1))
	
	if line1 == '':
#DEBUG:		
		print('line 1 is empty')
		while line2 != '':
#DEBUG:			
			print('parsing file 2')
			line2 = line2.replace('\n', '')
			line2 = line2.split('\t')
			
			## Here there will be stuff to be done
		
#DEBUG:			
			print("Table 2 le reste: line = {0}".format(line2))
			line2 = file_handle_2.readline()
	
#DEBUG:		print('line 2 : {0}'.format(line2))
	if line2 == '':
#DEBUG:
		print('line 2 is empty, EOF file 2 has been achieved')
		print('parsing file 1')
		while line1 != '':
#DEBUG:
			

			line1 = line1.replace('\n', '')
			line1 = line1.split('\t')
			
			## Here there will be stuff to be done

#DEBUG:			
			print("Table 1 le reste: line = {0}".format(line1))
			line1 = file_handle_1.readline()
#DEBUG:
	print('\n##########\nexiting finish it')
	



def parse_per_position(line1, line2):
	'''
	Split both lines in lists and compare the first 2 elements
	'''
	line = line.replace('\n','')


#########################################################################################
#####   #####   ######   ######  ###   #####  ###########################################
#####  #  #  #  ####  ##  #####  ###  #  ###  ###########################################
#####  ##  ###  ###  ####  ####  ###  ##  ##  ###########################################
#####  #######  ###        ####  ###  ###  #  ###########################################
#####  #######  ###  ####  ####  ###  ####    ###########################################
#####  #######  ###  ####  ####  ###  #####   ###########################################
#########################################################################################


def __main__():

	#################################
	## Parse arguments 
	parser = argparse.ArgumentParser()
	parser.add_argument("-v1", "--vcf1", dest="vcf1", help="First VCF file", type=str)
	parser.add_argument("-v2", "--vcf2", dest="vcf2", help="Second VCF file", type=str)
#	parser.add_argument("-s1", "--sorted1", dest="sorted1", help="Is the first VCF sorted ? [Y|N]", type=str)
#	parser.add_argument("-s2", "--sorted2", dest="sorted2", help="Is the second VCF sorted ? [Y|N]", type=str)

## This line allows to get many parameters from one option, it might be useful later

	args=parser.parse_args()
	
#	print(args.vcf1)
#	print(args.sorted1)
#	print(args.vcf2)
#	print(args.sorted2)

	## Create variables
	vcf1_header = []
	vcf2_header = []
	vcf1_line = []
	vcf2_line = []

#DEBUG:
	counter_while_loop = 0

	## Open both vcf files at the same time, close the loop when one of the files is over.
	with open(args.vcf1, 'r') as vcf1, open(args.vcf2, 'r') as vcf2:
		
		
		## Read the first line on each VCF
		line1 = vcf1.readline()
		line2 = vcf2.readline()
		
		## Loop to read next line as long as the line is not empty
		while line1 != "" and line2 != "":
			
#DEBUG:
			print("\nLoop number = {0}".format(counter_while_loop))
			
		
			## Skim the comment lines and get the headers
			vcf1_line, vcf1_header = skim_comments(line1, vcf1_header, vcf1)
			vcf2_line, vcf2_header = skim_comments(line2, vcf2_header, vcf2)

			## Here's the place to do stuff with the lines

#DEBUG:
			print("Table 1 contents: line = {0} --- header = {1}".format(vcf1_line, vcf1_header))
#DEBUG:
			print("Table 2 contents: line = {0} --- header = {1}".format(vcf2_line, vcf2_header))


			## Read the next line
			line1 = vcf1.readline()
			line2 = vcf2.readline()
			
			## COUNTER:
			counter_while_loop += 1
			

			
#DEBUG:	print("number of loops made inside the while loop = {0}".format(counter_while_loop))


	## Find which file is out of files is in EOF and the parse the rest of the lines of the other file

		
		
		print("\nOut of while loop\n\n")
		
		finish_it(line1, line2, vcf1, vcf2)
		
		
		
		print("\nFinish Program")
		

			
	

if __name__ == "__main__": __main__()

