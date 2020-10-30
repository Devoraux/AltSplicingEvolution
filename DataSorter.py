#Authors: Imon Islam, Miguel Guardado
#DataSorter.py
#July 1st, 2020
import sys
import csv
from csv import reader
from collections import Counter
import os

#Random Lists:
ListofShit = ['']
ListofStuff = []
ListofNewerStuff = []
ListofNewestStuff = []
ListofNewerestStuff = []
ListofUghNamesSoLong =[]
ListofUghIWannaDie = []
ListofOkDeadAF = []
ListofOMGJesus = []
ListofBernieBros = []
ListofCheckingLengthOfFullOrthologs = []

class DataAnal(object):

	def genecount(self):
		SetOfRandoShit = set()
		ListOfRandoShit2 = []
		for line in self:
			y = line.strip()
			SetOfRandoShit.add(y)
		for i in SetOfRandoShit:
			print(i)
	def RandomHelpfulFunctions(self):
		Dict4Orthologs =  {}
		Res = []
		ListOfRandoShit = []
		ListOfRandoShit2 = []
		ListOfRandoShit3 = []
		ListOfRandoShit4 = []
		ListOfRandoShit5 = []
		ListOfRandoShit6 = []
		ListOfUniqueGenes = []


		#Process and Filter Raw List
		for line in self:
			x = line.split(',')
			ListOfRandoShit.append(x)
		for i in ListOfRandoShit:
			for x in i:
				if x.startswith("E"):
					ListOfRandoShit2.append(x)
		for i in ListOfRandoShit2: #Handles cases of when string ends with \n
			if i.endswith("\n"):
				g = i.replace('\n', '')
				ListOfRandoShit3.append(g)
		for i in ListOfRandoShit2:
			if not i.endswith("\n"):
				ListOfRandoShit4.append(i)


		#List of All Orthologs
		JoinedListOfRandoShit = ListOfRandoShit3 + ListOfRandoShit4
		#print(JoinedListOfRandoShit)
		#Got this list iteration from https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
		#[Res.append(x) for x in JoinedListOfRandoShit if x not in Res]
		'''for i in JoinedListOfRandoShit: 
			if i not in Res:
				Res.append(i)
		print(Res)'''

		#List of Unique Orthologs (only appear once instead of a billion times)
		ListOfUniqueGenes = list(set(JoinedListOfRandoShit)) #Turn the list into a set, a set is able to get only the unique elements
		#print(len(ListOfUniqueGenes))
		#Dictionary with frequencies of all genes
		for key in ListOfUniqueGenes:
			Dict4Orthologs[key] = 0
		for item in JoinedListOfRandoShit: #dictionary that assigns orthologs to key
			if (item in Dict4Orthologs): #checks if item is in key pair and counts them and assigns number
				Dict4Orthologs[item] += 1
		#print(Dict4Orthologs)
		
		#To check how many genes only show up once
		"""devchar = 0
		for i in Dict4Orthologs.values():
			if i != 1:
				devchar += 1
			print(devchar)"""

		#Using https://www.geeksforgeeks.org/python-program-to-find-the-highest-3-values-in-a-dictionary/
		#I was able to impliment 'counter' module
		k = Counter(Dict4Orthologs)
		high = k.most_common()
		print("Dictionary with 30 highest values:")
		for i in high:
			print(i[0], ":", i[1],"")
		
		ListOfOrthologFrequencies = (Dict4Orthologs.values())

		#print(ListOfOrthologFrequencies)
				#Print number of gene repititions(gene, number of repeats):		
		#Using https://www.geeksforgeeks.org/python-program-to-find-the-highest-3-values-in-a-dictionary/
		#I was able to impliment 'counter' module
		#k = Counter(Dict4Orthologs)
		#high = k.most_common()
		#print("Dictionary with 30 highest values:")
		#for i in high:
		#	print(i[0], ":", i[1],"")

		#Using a Dictionary to classify this large data file and its many-to-many relationships
		#For Anything greater than 3 matches:
		#for key, value in Dict4Orthologs.items():
		#	if value >= 3:
		#		ListOfOrtho3.append(value)
		
		#If you want to Filter Columns individually, uncomment these lines and change the numbers:
		'''for line in ListOfOrtho:
			a = line[5],line[6]
			ListOfRat.append(a)
		for x in ListOfRat: 
			a = x[0],x[1]
			Emptyset1.add(a)
			StupidVariable = list(set(Emptyset1))
		for i in StupidVariable:
			print(i[0],i[1])'''

		#Go through dictionary and get all genes of specific species
		#for key, value in Dict4Orthologs.items():
			#if key.startswith('ENSMUS'):
			#	print(value)
			#if key.startswith('ENSGAL'):
			#	print(value)
			#if key.startswith('ENSRNO'):
			#	print(value)
			#if key.startswith('ENSOCU'):
			#	print(value)
			#if key.startswith('ENSMOD'):
			#	print(value)
			#if key.startswith('ENSMMU'):
			#	print(value)
			#if not key.startswith('ENSMUS') and not key.startswith('ENSGAL') and not key.startswith('ENSRNO') and not key.startswith('ENSOCU') and not key.startswith('ENSMOD') and not key.startswith('ENSMMU'):
			#	print(value)

	def ImonsMethod():
		#In Order for BioMart List, Useless so far!
		import sys 

		Dict4Orthologs = {}
		Dict4AdjacentOrthologs = {}
		Dic4HomoSapian = [] #ENS, Homo Sapian, Human
		Dic4Mouse = [] #ENSMUS, Mus Musculus, Mouse
		Dic4Chicken = [] #ENSGAL, Gallus Gallus, Chicken
		Dic4Rat = [] #ENSRNO, Rattus Norvegicus, Rat
		Dic4Rabbit = [] #ENSOCU, Oryctolagus Cuniculus, Rabbit
		Dic4Possum = [] #ENSMOD, Monodelphis Domestica, Opossum
		Dic4Macaque = [] #ENSMMU, Macaca Mulatta, Macaque

		#Just placeholder lists in case I need them!
		Res = []
		ListOfOrtho = []
		ListOfOrtho2 = []
		ListOfOrtho3 = []
		ListOfOrtho4 = []
		ListOfOrtho5 = []
		ListOfMouse = []
		ListOfChicken = []
		ListOfRat = []
		ListOfRabbit = []
		ListOfPossum = []
		ListOfMacaque = []
		ListOfRepeats = []
		ListOfRepeats2 = []

		#EmptySets: Used to get rid of duplicate genes
		Emptyset1 = set()

		for line in sys.stdin:
			y = line.strip()
			x = y.split(',')
			ListOfOrtho.append(x) #all raw lines in ListOfOrtho
		for i in ListOfOrtho:
			for j in i:
				ListOfOrtho2.append(j) #Every gene in each line appended to a list called ListOfOrtho2
		
		#print(ListOfOrtho2) #Contains raw genes, lots of duplicates, unprocessed.
		
		for i in ListOfOrtho2: #For cases where sometimes its empty
			if i != '':
				ListOfOrtho3.append(i)
		#print(ListOfOrtho3)
		ListOfUniqueGenes = list(set(ListOfOrtho3))
		#print(len(ListOfUniqueGenes))

		#Initialize Dictionary
		for key in ListOfUniqueGenes:
			Dict4Orthologs[key] = 0
		for item in ListOfOrtho2: 
			if (item in Dict4Orthologs):
				Dict4Orthologs[item] += 1
		#print(Dict4Orthologs)

		#Get List from Dictionary of All Unique (meaning appears one time throughout the entire data structure) Genes
		for key, value in Dict4Orthologs.items():
			if value == 1:
				Res.append(key)

		#Go through unique list of genes and if slice is in it then save line!
		for i in ListOfOrtho:
				for j in Res:
					if j in i[0] and i[1] and i[2] and i[3] and i[4] and i[5] and i[6]:
						print(i)

	def BensMethod():
		#Human vs Mouse Pairwise Analysis
		FilteredHumanMouse = []
		#Exploring Ben's Method for creating 1:1:1:1:1:1 Orthogroups!
		#Replace the path with the destination of your 6 seperate files
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/SecondAttemptMethods/BensMethod2ndAttempt/mart_export.txt', 'r') as read_obj:
			#Pass the file object to reader()
			csv_reader = reader(read_obj)
			#Pass reader to list()
			list_of_rows_HumanMouse = list(csv_reader)
		#Filter out only ortholog_one2one
		for i in list_of_rows_HumanMouse:
			if 'ortholog_one2one' in i:
				FilteredHumanMouse.append([i[0],i[1]])
		#print(FilteredHumanMouse)

		#Human vs Chicken Pairwise Analysis
		FilteredHumanChicken = []
		#Exploring Ben's Method for creating 1:1:1:1:1:1 Orthogroups!
		#Replace the path with the destination of your 6 seperate files
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/SecondAttemptMethods/BensMethod2ndAttempt/mart_export-2.txt', 'r') as read_obj:
			#Pass the file object to reader()
			csv_reader = reader(read_obj)
			#Pass reader to list()
			list_of_rows_HumanChicken = list(csv_reader)
		#Filter out only ortholog_one2one
		for i in list_of_rows_HumanChicken:
			if 'ortholog_one2one' in i:
				FilteredHumanChicken.append([i[0],i[1]])
		#print(FilteredHumanChicken)

		#Human vs Rat Pairwise Analysis
		FilteredHumanRat = []
		#Exploring Ben's Method for creating 1:1:1:1:1:1 Orthogroups!
		#Replace the path with the destination of your 6 seperate files
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/SecondAttemptMethods/BensMethod2ndAttempt/mart_export-3.txt', 'r') as read_obj:
			#Pass the file object to reader()
			csv_reader = reader(read_obj)
			#Pass reader to list()
			list_of_rows_HumanRat = list(csv_reader)
		#Filter out only ortholog_one2one
		for i in list_of_rows_HumanRat:
			if 'ortholog_one2one' in i:
				FilteredHumanRat.append([i[0],i[1]])
		#print(FilteredHumanRat)

		#Human vs Rabbit Pairwise Analysis
		FilteredHumanRabbit = []
		#Exploring Ben's Method for creating 1:1:1:1:1:1 Orthogroups!
		#Replace the path with the destination of your 6 seperate files
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/SecondAttemptMethods/BensMethod2ndAttempt/mart_export-4.txt', 'r') as read_obj:
			#Pass the file object to reader()
			csv_reader = reader(read_obj)
			#Pass reader to list()
			list_of_rows_HumanRabbit = list(csv_reader)
		#Filter out only ortholog_one2one
		for i in list_of_rows_HumanRabbit:
			if 'ortholog_one2one' in i:
				FilteredHumanRabbit.append([i[0],i[1]])
		#print(FilteredHumanRabbit)

		#Human vs Opossum Pairwise Analysis
		FilteredHumanOpossum = []
		#Exploring Ben's Method for creating 1:1:1:1:1:1 Orthogroups!
		#Replace the path with the destination of your 6 seperate files
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/SecondAttemptMethods/BensMethod2ndAttempt/mart_export-5.txt', 'r') as read_obj:
			#Pass the file object to reader()
			csv_reader = reader(read_obj)
			#Pass reader to list()
			list_of_rows_HumanOpossum = list(csv_reader)
		#Filter out only ortholog_one2one
		for i in list_of_rows_HumanOpossum:
			if 'ortholog_one2one' in i:
				FilteredHumanOpossum.append([i[0],i[1]])
		#print(FilteredHumanOpossum)

		#Human vs Macaque Pairwise Analysis
		FilteredHumanMacaque = []
		#Exploring Ben's Method for creating 1:1:1:1:1:1 Orthogroups!
		#Replace the path with the destination of your 6 seperate files
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/SecondAttemptMethods/BensMethod2ndAttempt/mart_export-6.txt', 'r') as read_obj:
			#Pass the file object to reader()
			csv_reader = reader(read_obj)
			#Pass reader to list()
			list_of_rows_HumanMacaque = list(csv_reader)
		#Filter out only ortholog_one2one
		for i in list_of_rows_HumanMacaque:
			if 'ortholog_one2one' in i:
				FilteredHumanMacaque.append([i[0],i[1]])
		#print(FilteredHumanMacaque)
		#Now time to construct the final orthogroups using human as identifier.
		AlmostDone = []
		AlmostDoneHeh = []
		AlmostDoneHehHeh = []
		AlmostDoneHehHehHeh = []
		FinallyDone = []
		for i in FilteredHumanMouse:
			for j in FilteredHumanChicken:
				if i[0] in j[0]:
					AlmostDone.append([i[0],i[1],j[1]])
		for i in AlmostDone:
			for j in FilteredHumanRat:
				if i[0] in j[0]:
					AlmostDoneHeh.append([i[0],i[1],i[2],j[1]])
		for i in AlmostDoneHeh:
			for j in FilteredHumanRabbit:
				if i[0] in j[0]:
					AlmostDoneHehHeh.append([i[0],i[1],i[2],i[3],j[1]])
		for i in AlmostDoneHehHeh:
			for j in FilteredHumanOpossum:
				if i[0] in j[0]:
					AlmostDoneHehHehHeh.append([i[0],i[1],i[2],i[3],i[4],j[1]])
		for i in AlmostDoneHehHehHeh:
			for j in FilteredHumanMacaque:
				if i[0] in j[0]:
					FinallyDone.append([i[0],i[1],i[2],i[3],i[4],i[5],j[1]])
		PairwiseData = [list_of_rows_HumanMouse, list_of_rows_HumanChicken, list_of_rows_HumanRat, list_of_rows_HumanRabbit, list_of_rows_HumanOpossum, list_of_rows_HumanMacaque, FinallyDone]
		return PairwiseData

	def AnalyzingBothMethods():
		BensMethodList = []
		CheckingBensList = []
		CheckingImonsList = []
		#Exploring Ben's Method for creating 1:1:1:1:1:1 Orthogroups!
		#Replace the path with the destination of your 6 seperate files
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/SecondAttemptMethods/BensMethod2ndAttempt/BensMethod2ndAttempt.txt', 'r') as read_obj:
			BensMethod = []
			list_of_rows_BensMethod = read_obj
			for i in list_of_rows_BensMethod:
				j = i.strip('[')
				k = j.replace(']', '')
				l = k.strip('\n')
				BensMethod.append(l)
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/SecondAttemptMethods/ImonsMethod2ndAttempt/ImonsMethod2ndAttempt.txt', 'r') as read_obj2:
			ImonsMethod = []
			list_of_rows_ImonsMethod = read_obj2
			for i in list_of_rows_ImonsMethod:
				j = i.strip('[')
				k = j.replace(']', '')
				l = k.strip('\n')
				ImonsMethod.append(l)

		#Looking at both methods for differences using for loops to iterate through each line
		res = filter(lambda i: i not in BensMethod, ImonsMethod)
		mes = filter(lambda i: i not in ImonsMethod, BensMethod)

		Differences = list(res)
		Differences2 = list(mes)
		print(len(Differences)) #Also known as 'z'
		print(len(Differences2))
		return Differences

	def AnalyzingImonsOrthology(self):
		ImonsMethod = []
		ImonsMethod2 = []
		ImonsMethod3 = []
		ImonsMethod4 = []
		ImonsMethod5 = []
		ImonsMethod6 = []
		ImonsMethod7 = []
		ImonsMethod8 = []
		ImonsMethod9 = []
		HumanOrthologs = [] #ENSG
		MouseOrthologs = [] #ENSMUS
		ChickenOrthologs = [] #ENSGAL
		RatOrthologs = [] #ENSRNOG
		RabbitOrthologs = [] #ENSOCU
		OpossumOrthologs = [] #ENSMODG
		MacaqueOrthologs = [] #ENSMMUG

		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/ImonsMethodOrthogroups.txt', 'r') as read_obj2:
			list_of_rows_ImonsMethod = read_obj2
			for i in list_of_rows_ImonsMethod:
				j = i.strip('[')
				k = j.replace(']', '')
				l = k.strip('\n')
				ImonsMethod.append(l)
		#General List Processing
		for i in ImonsMethod:
			g = i.split(',')
			ImonsMethod2.append(g)
		#For Human Orthologs:
		for i in ImonsMethod2:
			ImonsMethod3.append(i[0])
		for i in ImonsMethod3:
			HumanOrthologs.append(i[1:-1])
		#For Mouse Orthologs:
		for i in ImonsMethod2:
			ImonsMethod4.append(i[1])
		for i in ImonsMethod4:
			g = i.strip()
			MouseOrthologs.append(g[1:-1])
		#For Chicken Orthologs:
		for i in ImonsMethod2:
			ImonsMethod5.append(i[2])
		for i in ImonsMethod5:
			g = i.strip()
			ChickenOrthologs.append(g[1:-1])
		#For Rat Orthologs:
		for i in ImonsMethod2:
			ImonsMethod6.append(i[3])
		for i in ImonsMethod6:
			g = i.strip()
			RatOrthologs.append(g[1:-1])
		#For Rabbit Orthologs:
		for i in ImonsMethod2:
			ImonsMethod7.append(i[4])
		for i in ImonsMethod7:
			g = i.strip()
			RabbitOrthologs.append(g[1:-1])
		#For Opossum Orthologs:
		for i in ImonsMethod2:
			ImonsMethod8.append(i[5])
		for i in ImonsMethod8:
			g = i.strip()
			OpossumOrthologs.append(g[1:-1])
		#For Macaque Orthologs:
		for i in ImonsMethod2:
			ImonsMethod9.append(i[6])
		for i in ImonsMethod9:
			g = i.strip()
			MacaqueOrthologs.append(g[1:-1])
		#Human to Mouse for Analysis
		HumanOrthoRelations = []
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/mart_export.txt', 'r') as read_obj:
			#Pass the file object to reader()
			csv_reader = reader(read_obj)
			#Pass reader to list()
			list_of_rows_HumanMouse = list(csv_reader)
		for i in HumanOrthologs:
			for k in list_of_rows_HumanMouse:
				if i in k:
					HumanOrthoRelations.append(k[2])
		x = HumanOrthoRelations.count('ortholog_one2one')
		y = HumanOrthoRelations.count('ortholog_one2many')
		z = HumanOrthoRelations.count('ortholog_many2many')
		print('The total number of Human genes in Imons Method is: '+ str(len(HumanOrthologs)))
		print('The total number of Human genes identified from Imons Method using Bens Orthology Descriptors '+ str(len(HumanOrthoRelations)))
		print('In human the number of ortholog_one2one '+ str(x), 'the percentage is '+ str(x/len(HumanOrthoRelations)))
		print('In human the number of ortholog_one2many '+ str(y), 'the percentage is ' + str(y/len(HumanOrthoRelations)))
		print('In human the number of ortholog_many2many '+ str(z), 'the percentage is ' + str(z/len(HumanOrthoRelations)))

	def MethodMatrixes(x, z):
		'''The x variable is the pairwise analysis between two species, containing 3 columns (each of the 6 lists I imported), which I use to replace constructed list genes with the third row
		which is orthology for the purposes of making matrixes that describe the lines in relation to human genes. At the end of the x variable is Ben's complete orthogroups which ive appended to use in this function.
		The z variable is the x amount of lines that Bens method lacks, that Imons method was able to pick up from the biomart data miner.'''
		ImonsTrimmedList = []
		ImonsFinalTrimmedLines = []
		DraftMatrix1 = []
		DraftMatrix2 = []
		DraftMatrix3 = []
		DraftMatrix4 = []
		DraftMatrix5 = []
		DraftMatrix6 = []
		FinalMatrix = []

		BensDraftMatrix1 =[]
		BensDraftMatrix2 = []
		BensDraftMatrix3 = []
		BensDraftMatrix4 = []
		BensDraftMatrix5 = []
		BensDraftMatrix6 = []
		BensFinalMatrix = []

		HumanMouseOrthoList = x[0]
		HumanChickenOrthoList = x[1]
		HumanRatOrthoList = x[2]
		HumanRabbitOrthoList = x[3]
		HumanOpossumOrthoList = x[4]
		HumanMacaqueOrthoList = x[5]
		BensMethodCompleteOrthoGroups = x[6]
		#Just text editing/cleaning the lines that Imon's method has, but Ben's method does not, into a list.
		for i in z:
			j = i.split(',')
			ImonsTrimmedList.append(j)
		for i in ImonsTrimmedList:
			ImonsFinalTrimmedLines.append([i[0][1:-1],i[1][2:-1],i[2][2:-1],i[3][2:-1],i[4][2:-1],i[5][2:-1],i[6][2:-1]])
		#Just text editing/cleaning the lines that Bens's method has, but Imon's method does not, into a list.
		'''for i in z:
			j = i.split(',')
			BensTrimmedList.append(j)'''
		'''for i in BensTrimmedList:
			BensFinalTrimmedLines.append([i[0][1:-1],i[1][2:-1],i[2][2:-1],i[3][2:-1],i[4][2:-1],i[5][2:-1],i[6][2:-1]])'''
		#for i in ImonsFinalTrimmedLines:
		#	print(i)
		#print(len(ImonsFinalTrimmedLines))


		#Constructing a Matrix Structure for Imon's OrthoGroups that Ben does not have. 
		#Looking through my x lines that my method has that ben's does not, I am able to create orthology matrixes using Ben's pairwise files.
		for i in ImonsFinalTrimmedLines:
			for j in HumanMouseOrthoList:
				if i[0] == j[0]:
					DraftMatrix1.append(i[0]+','+j[2])
		for i in DraftMatrix1:
			for q in HumanChickenOrthoList:
				if i[0:15] == q[0]:
					DraftMatrix2.append(i[0:]+','+q[2])
		for i in DraftMatrix2:
			for v in HumanRatOrthoList:
				if i[0:15] == v[0]:
					DraftMatrix3.append(i[0:]+','+v[2])
		for i in DraftMatrix3:
			for g in HumanRabbitOrthoList:
				if i[0:15] == g[0]:
					DraftMatrix4.append(i[0:]+','+g[2])
		for i in DraftMatrix4:
			for h in HumanOpossumOrthoList:
				if i[0:15] == h[0]:
					DraftMatrix5.append(i[0:]+','+h[2])
		for i in DraftMatrix5:
			for k in HumanMacaqueOrthoList:
				if i[0:15] == k[0]:
					DraftMatrix6.append(i[0:]+','+k[2])
		for i in DraftMatrix6:
			if i not in FinalMatrix:
				FinalMatrix.append(i)
		#Just do 'python DataSorter.py > YourResults.txt' on the terminal
		for i in FinalMatrix:
			print(i) 


		#Checking all of Ben's Orthology
		#As a sanity check, I am checking every single gene in Bens Method Orthogroups to make sure they are all one-to-one.
		for i in BensMethodCompleteOrthoGroups:
			for j in HumanMouseOrthoList:
				if i[0] == j[0]:
					BensDraftMatrix1.append(i[0]+','+j[2])
		for i in BensDraftMatrix1:
			for q in HumanChickenOrthoList:
				if i[0:15] == q[0]:
					BensDraftMatrix2.append(i[0:]+','+q[2])
		for i in BensDraftMatrix2:
			for v in HumanRatOrthoList:
				if i[0:15] == v[0]:
					BensDraftMatrix3.append(i[0:]+','+v[2])
		for i in BensDraftMatrix3:
			for g in HumanRabbitOrthoList:
				if i[0:15] == g[0]:
					BensDraftMatrix4.append(i[0:]+','+g[2])
		for i in BensDraftMatrix4:
			for h in HumanOpossumOrthoList:
				if i[0:15] == h[0]:
					BensDraftMatrix5.append(i[0:]+','+h[2])
		for i in BensDraftMatrix5:
			for k in HumanMacaqueOrthoList:
				if i[0:15] == k[0]:
					BensDraftMatrix6.append(i[0:]+','+k[2])
		for i in BensDraftMatrix6:
			if i not in BensFinalMatrix:
				BensFinalMatrix.append(i)
		#for i in BensFinalMatrix:
			#print(i)


if __name__ == '__main__':
	'''x = DataAnal.BensMethod()
	z = DataAnal.AnalyzingBothMethods()
	DataAnal.MethodMatrixes(x, z)'''
	DataAnal.ImonsMethod()


