#Authors: Imon Islam, Miguel Guardado
#EVEDataSorter.py
#October 30th, 2020
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
	def HowManyFiles():

		HumanAtP63 = ['young middle age', 'liver']
		ChickenAtP63 = ['postnatal day 70', 'liver']
		RabbitAtP63 = ['postnatal day 84', 'liver']
		MouseAtP63 = ['postnatal day 63', 'liver']
		MacaqueAtP63 = ['9 years', 'liver']
		OpossumAtP63 = ['postnatal day 120', 'liver']
		RatAtP63 = ['postnatal day 112', 'liver']	

		HumanAtP28 = ['young adult','liver']
		ChickenAtP28 = ['postnatal day 70', 'liver']
		RabbitAtP28 = ['postnatal day 84', 'liver']
		MouseAtP28 = ['postnatal day 28', 'liver']
		MacaqueAtP28 = ['6 months', 'liver']
		OpossumAtP28 = ['postnatal day 90', 'liver']
		RatAtP28 = ['postnatal day 42', 'liver']

		HumanAtP14 = ['toddler', 'liver']
		ChickenAtP14 = ['postnatal day 0', 'liver']
		RabbitAtP14 = ['postnatal day 14','liver']
		MouseAtP14 = ['postnatal day 14','liver']
		MacaqueAtP14 = ['postnatal day 23','liver']
		OpossumAtP14 = ['postnatal day 60', 'liver']
		RatAtP14 = ['postnatal day 14','liver']

		HumanAtP3 = ['20 week post conception', 'liver']
		ChickenAtP3 = ['embryonic day 14', 'liver']
		RabbitAtP3 = ['postnatal day 0', 'liver']
		MouseAtP3 = ['postnatal day 3', 'liver']
		MacaqueAtP3 = ['embryonic day 130', 'liver'] 
		OpossumAtP3 = ['postnatal day 21', 'liver']
		RatAtP3 = ['postnatal day 3', 'liver']

		HumanAtP0 = ['19 week post conception', 'liver']
		ChickenAtP0 = ['embryonic day 12', 'liver']
		RabbitAtP0 = ['embryonic day 27', 'liver']
		MouseAtP0 = ['postnatal day 0', 'liver']
		MacaqueAtP0 = ['embryonic day 108', 'liver']
		OpossumAtP0 = ['postnatal day 14', 'liver']
		RatAtP0 = ['postnatal day 0', 'liver']



		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/GeneDevelopmentPaperData/HUMANFILES.txt', 'r') as read_obj:
			csv_reader = reader(read_obj)
			listofrawdata = list(csv_reader)
			for i in listofrawdata:
				for j in i:
					if all(x in j for x in HumanAtP0):
						print('Human @ P0', len(j))
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/GeneDevelopmentPaperData/CHICKENFILES.txt', 'r') as read_obj:
			csv_reader = reader(read_obj)
			listofrawdata2 = list(csv_reader)
			for i in listofrawdata2:
				for j in i:
					if all(x in j for x in ChickenAtP0):
						print('Chicken @ P0',len(j))
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/GeneDevelopmentPaperData/RABBITFILES.txt', 'r') as read_obj:
			csv_reader = reader(read_obj)
			listofrawdata = list(csv_reader)
			for i in listofrawdata:
				for j in i:
					if all(x in j for x in RabbitAtP0):
						print('Rabbit @ P0',len(j))
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/GeneDevelopmentPaperData/MOUSEFILES.txt', 'r') as read_obj:
			csv_reader = reader(read_obj)
			listofrawdata4 = list(csv_reader)
			for i in listofrawdata4:
				for j in i:
					if all(x in j for x in MouseAtP0):
						print('Mouse @ P0',len(j))
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/GeneDevelopmentPaperData/MACAQUEFILES.txt', 'r') as read_obj:
			csv_reader = reader(read_obj)
			listofrawdata5 = list(csv_reader)
			for i in listofrawdata5:
				for j in i:
					if all(x in j for x in MacaqueAtP0):
						print('Macaque @ P0',len(j))
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/GeneDevelopmentPaperData/OPOSSUMFILES.txt', 'r') as read_obj:
			csv_reader = reader(read_obj)
			listofrawdata6 = list(csv_reader)
			for i in listofrawdata6:
				for j in i:
					if all(x in j for x in OpossumAtP0):
						print('Opossum @ P0', len(j))
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/GeneDevelopmentPaperData/RATFILES.txt', 'r') as read_obj:
			csv_reader = reader(read_obj)
			listofrawdata7 = list(csv_reader)
			for i in listofrawdata7:
				for j in i:
					if all(x in j for x in RatAtP0):
						print('Rat @ P0',len(j))

	def DataInput():
		'''This function is for processing a single VastTools Output File'''
		FirstParse = []
		SecondParse = []
		ThirdParse = []
		with open ('/Users/memelord/Downloads/INCLUSION_LEVELS_FULL-Mmu3-mm9.tab', 'r') as read_obj:
			data_reader = csv.reader(read_obj, delimiter='\t')
			for i in data_reader:
				print(i[0]+'-'+i[1],'\t',i[6],'\t',i[8],'\t',i[10])

	def ReadCountTableMaker():
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
	def OrthogroupswithGeneNames():
		numbercheck = []
		FirstEdit = []
		SecondEdit = []
		ThirdEdit = []
		FourthEdit = []
		FifthEdit = []
		FullOrthogroupGeneIDList = []

		FullHumanGeneList = []
		FullMouseGeneList = []
		FullChickenGeneList = []
		FullRatGeneList = []
		FullRabbitGeneList = []
		FullOpossumGeneList = []
		FullMacaqueGeneList = []

		FinalListDraft1 = []
		FinalListDraft2 = []
		FinalListDraft3 = []
		FinalListDraft4 = []
		FinalListDraft5 = []
		FinalListDraft6 = []

		templist1 = []
		templist2 = []
		templist3 = []
		templist4 = []
		templist5 = []
		templist6 = []
		templist7 = []
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/GenomeGeneNames/HumanGeneNames.txt') as read_obj1:
			for i in read_obj1:
				f = i.strip()
				HumanGeneList = f.split(',')
				FullHumanGeneList.append(HumanGeneList)
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/GenomeGeneNames/MouseGeneNames.txt') as read_obj2:
			for i in read_obj2:
				f = i.strip()
				MouseGeneList = f.split(',')
				FullMouseGeneList.append(MouseGeneList)
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/GenomeGeneNames/ChickenGeneNames.txt') as read_obj3:
			for i in read_obj3:
				f = i.strip()
				ChickenGeneList = f.split(',')
				FullChickenGeneList.append(ChickenGeneList)
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/GenomeGeneNames/RatGeneNames.txt') as read_obj4:
			for i in read_obj4:
				f = i.strip()
				RatGeneList = f.split(',')
				FullRatGeneList.append(RatGeneList)	
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/GenomeGeneNames/RabbitGeneNames.txt') as read_obj5:
			for i in read_obj5:
				f = i.strip()
				RabbitGeneList = f.split(',')
				FullRabbitGeneList.append(RabbitGeneList)
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/GenomeGeneNames/OpossumGeneNames.txt') as read_obj6: 
			for i in read_obj6:
				f = i.strip()
				OpossumGeneList = f.split(',')
				FullOpossumGeneList.append(OpossumGeneList)
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/GenomeGeneNames/MacaqueGeneNames.txt') as read_obj7:
			for i in read_obj7:
				f = i.strip()
				MacaqueGeneList = f.split(',')
				FullMacaqueGeneList.append(MacaqueGeneList)
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/SecondAttemptMethods/BensMethod2ndAttempt/BensMethod2ndAttempt.txt', 'r') as read_obj:
			for i in read_obj:
				FirstEdit.append(i)
			for i in FirstEdit:
				editedline = i.strip('\n')
				SecondEdit.append(editedline)
			for i in SecondEdit:
				ThirdEdit.append(i[1:-1])
			for i in ThirdEdit:
				Splitlines = i.split()
				FourthEdit.append(Splitlines)
			for i in FourthEdit:
				Variable = (i[0],i[1],i[2],i[3],i[4],i[5],i[6])
				FifthEdit.append(Variable)
			for i in FifthEdit:
				HumanGene = i[0][1:-2]
				MouseGene = i[1][1:-2]
				ChickenGene = i[2][1:-2]
				RatGene = i[3][1:-2]
				RabbitGene = i[4][1:-2]
				OpossumGene = i[5][1:-2]
				MacaqueGene = i[6][1:-1]
				FullOrthogroupGeneID = [HumanGene, MouseGene, ChickenGene, RatGene, RabbitGene, OpossumGene, MacaqueGene]
				FullOrthogroupGeneIDList.append(FullOrthogroupGeneID)
			for h in FullOrthogroupGeneIDList:
				for i in FullHumanGeneList:
					if i[0] == h[0]:
						tempvar = [i[1],h[1],h[2],h[3],h[4],h[5],h[6]]
						templist1.append(tempvar)
			for m in templist1:
				for i in FullMouseGeneList:
					if m[1] == i[0]:
						tempvar2 = [m[0],i[1],m[2],m[3],m[4],m[5],m[6]]
						templist2.append(tempvar2)
			for c in templist2:
				for i in FullChickenGeneList:
					if c[2] == i[0]:
						tempvar3 = [c[0],c[1],i[1],c[3],c[4],c[5],c[6]]
						templist3.append(tempvar3)
			for r in templist3:
				for i in FullRatGeneList:
					if r[3] == i[0]:
						tempvar4 = [r[0],r[1],r[2],i[1],r[4],r[5],r[6]]
						templist4.append(tempvar4)
			for rh in templist4:
				for i in FullRabbitGeneList:
					if rh[4] == i[0]:
						tempvar5 = [rh[0],rh[1],rh[2],rh[3],i[1],rh[5],rh[6]]
						templist5.append(tempvar5)
			for o in templist5:
				for i in FullOpossumGeneList:
					if o[5] == i[0]:
						tempvar6 = [o[0],o[1],o[2],o[3],o[4],i[1],o[6]]
						templist6.append(tempvar6)
			for ma in templist6:
				for i in FullMacaqueGeneList:
					if ma[6] == i[0]:
						tempvar7 = [ma[0],ma[1],ma[2],ma[3],ma[4],ma[5],i[1]]
						templist7.append(tempvar7)
			for i in templist7:
				if '' not in i:
					numbercheck.append(i)
			FullGeneGroups = numbercheck
		return FullGeneGroups

		'''for d in DraftList1:
				for m in MouseVastToolsData:
					if i[1] == m[0]:
						PSIofHumanMouse = [d[0],d[1],d[2],d[3],m[2],m[3],m[4]]
						print(PSIofHumanMouse)'''

	def EVEMatrixMaker(x):
		HumanVastToolsData = []
		MouseVastToolsData = []
		ChickenVastToolsData = []
		DraftList1 = []
		DraftList2 = []
		DraftList3 = []
		FinalDraft = []
		#Importing the various VastTools Output
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/Eve Data/INCLUSION_LEVELS_FULL-Hsa3-hg19.tab', 'r') as read_obj1:
			data_reader = csv.reader(read_obj1, delimiter='\t')
			for i in data_reader:
				HumanVar = [i[0],i[1],i[6],i[8],i[10]]
				HumanVastToolsData.append(HumanVar)
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/Eve Data/INCLUSION_LEVELS_FULL-Mmu4-mm9.tab', 'r') as read_obj2:
			data_reader = csv.reader(read_obj2, delimiter='\t')
			for i in data_reader:
				MouseVar = [i[0],i[1],i[6],i[8],i[10]]
				MouseVastToolsData.append(MouseVar)
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/Eve Data/INCLUSION_LEVELS_FULL-Gga4.tab', 'r') as read_obj3:
			data_reader = csv.reader(read_obj3, delimiter='\t')
			for i in data_reader:
				ChickenVar = [i[0],i[1],i[6],i[8],i[10]]
				ChickenVastToolsData.append(ChickenVar)
		#This is the part where I take every 1st[0] and 2nd[1] element of each list and compare them to x[0 if human, 1 if mouse, 2 if chicken]. If theyre there, reserve the gene name and exon name and attach psi samples.
		for i in x:
			for h in HumanVastToolsData:
				if i[0] == h[0]:
					PSIofHuman = [h[0],h[1],h[2],h[3],h[4]]
					DraftList1.append(PSIofHuman)
			for m in MouseVastToolsData:
				if i[1] == m[0]:
					PSIofMouse = [m[0],m[1],m[2],m[3],m[4]]
					DraftList2.append(PSIofMouse)
			for c in ChickenVastToolsData:
				if i[2] == c[0]:
					PSIofChicken = [c[0],c[1],c[2],c[3],c[4]]
					DraftList3.append(PSIofChicken)
		
		if DraftList1[0] == x[0]:
			if DraftList2[0] == x[1]:
				if DraftList3[0] == x[2]:
					FinalPSIList = [DraftList1[0], DraftList1[1], DraftList1[2], DraftList1[3], DraftList1[4], DraftList2[0], DraftList2[1], DraftList2[2], DraftList2[3], DraftList2[4], DraftList3[0], DraftList3[1], DraftList3[2], DraftList3[3], DraftList3[4]]
					print(FinalPSIList)
					FinalDraft.append(FinalPSIList)
		print(FinalDraft)
		'''for i in x:
			for hsa in DraftList1:
				for mmu in DraftList2:
					for gga in DraftList3:
						print('plz werk')
						if hsa[0] == x[0]:
							print('hi')
							if mmu[0] == x[1]:
								print('hii')
								if gga[0] == x[2]:
									print('hiii')
									FinalPSIList = [hsa[0], hsa[1], hsa[2], hsa[3], hsa[4], mmu [0], mmu[1], mmu[2], mmu[3], mmu[4], gga[0], gga[1], gga[2], gga[3], gga[4]]
									FinalDraft.append(FinalPSIList)
		print(FinalDraft)'''
	def ExorthistMatrixSetup():
		'''The purpose of this function is to take Exorthist Output: GeneID_sp1, Exon_coords_sp1, GeneID_sp2, Exon_coords_sp2, Sp1, Sp2
		and basically creates a matrix that is centered around the Human Gene. This function can be modified by a knowledgeable python coder
		to basically center the matrix around any other gene, doesnt have to be human.'''

		HumanList = []
		EditedRawData = []
		EditedRawData2 = []
		EditedRawData3 = []
		ChickenExonList = []
		RatExonList = []
		MouseExonList = []
		MacaqueExonList = []
		HumanExonList = []
		RabbitExonList = []
		OpossumExonList = []
		DraftExonList1 = []
		DraftExonList2 = []
		DraftExonList3 = []
		DraftExonList4 = []
		DraftExonList5 = []
		DraftExonList6 = []
		DraftFinalList1 = []
		DraftFinalList2 = []
		DraftFinalList3 = []
		DraftFinalList4 = []
		DraftFinalList5 = []
		DraftFinalList6 = []
		EmptyIterable = []
		FinalDraftList1 = []

		#Importing the Data from files
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/Exon Orthogroups/filtered_best_scored_EX_matches_by_targetgene.tab', 'r') as read_obj1:
			data_reader = csv.reader(read_obj1, delimiter='\t')
			for i in data_reader:
				j = i[0]+'*'+i[1]
				k = i[2]+'*'+i[3]
				l = [k,j]
				EditedRawData.append(l)
			#Cleaning the data
			for i in EditedRawData:
				if i[0].startswith('ENSG'):
					f = i[0].split('*')
					k = i[1].split('*')
					a = [f[0],f[1],k[0],k[1]]
					HumanExonList.append(a)
				if i[0].startswith('ENSMUSG'):
					f = i[0].split('*')
					k = i[1].split('*')
					a = [f[0],f[1],k[0],k[1]]
					MouseExonList.append(a)
				if i[0].startswith('ENSGALG'):
					f = i[0].split('*')
					k = i[1].split('*')
					a = [f[0],f[1],k[0],k[1]]
					ChickenExonList.append(a)
				if i[0].startswith('ENSRNOG'):
					f = i[0].split('*')
					k = i[1].split('*')
					a = [f[0],f[1],k[0],k[1]]
					RatExonList.append(a)
				if i[0].startswith('ENSOCUG'):
					f = i[0].split('*')
					k = i[1].split('*')
					a = [f[0],f[1],k[0],k[1]]
					RabbitExonList.append(a)
				if i[0].startswith('ENSMODG'):
					f = i[0].split('*')
					k = i[1].split('*')
					a = [f[0],f[1],k[0],k[1]]
					OpossumExonList.append(a)
				if i[0].startswith('ENSMMUG'):
					f = i[0].split('*')
					k = i[1].split('*')
					a = [f[0],f[1],k[0],k[1]]
					MacaqueExonList.append(a)

			#Sorting the data into manageable lists for iteration
			for i in HumanExonList:
				if i[0].startswith('ENSG'):
					if i[2].startswith('ENSMUSG'):
						DraftExonList1.append(i) #now has Human, Mouse
			for i in MouseExonList:
				if i[0].startswith('ENSMUSG'):
					if i[2].startswith('ENSGAL'):
						DraftExonList2.append(i) #now has Mouse, Chicken 
			for i in ChickenExonList:
				if i[0].startswith('ENSGAL'):
					if i[2].startswith('ENSRNOG'):
						DraftExonList3.append(i) #now has Chicken, Rat
			for i in RatExonList:
				if i[0].startswith('ENSRNOG'):
					if i[2].startswith('ENSOCUG'):
						DraftExonList4.append(i) #now has Rat, Rabbit
			for i in RabbitExonList:
				if i[0].startswith('ENSOCUG'):
					if i[2].startswith('ENSMODG'):
						DraftExonList5.append(i) #now has Rabbit, Opossum
			for i in OpossumExonList:
				if i[0].startswith('ENSMODG'):
					if i[2].startswith('ENSMMUG'):
						DraftExonList6.append(i) #now has Opossum, Macaque
			
			#Attempting to create orthogroups
			for i in DraftExonList1:
				for k in DraftExonList2:
					if i[2] == k[0]:
						j = i[0],i[1],i[2],i[3],k[2],k[3]
						DraftFinalList1.append(j)
			for i in DraftFinalList1:
				print(i)

			'''This is where I decided to write the DraftFinalList1 to memory, because it ate up so much of my processing power!
			So I decided to basically run the code:
			python EVEDataSorter.py > FirstDraftofFinalOG.txt 

			The above command wrote it into a text file, which I can then work with further through the next set of loops.'''
			'''ArrayOfLists = [DraftExonList1,DraftExonList2,DraftExonList3,DraftExonList4,DraftExonList5,DraftExonList6]
			return ArrayOfLists'''


	def ExorthistMatrixMaker():
		FirstDraftofFinalOG = []
		DraftExonList1 = x[0]
		DraftExonList2 = x[1]
		DraftExonList3 = x[2] 
		DraftExonList4 = x[3]
		DraftExonList5 = x[4]
		DraftExonList6 = x[5]
		DraftFinalList2 = []
		CleaningUpLines = []
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/FirstDraftofFinalOG.txt') as read_obj1:
			for i in read_obj1:
				k = i.strip()
				j = k.replace('(','')
				f = j.replace(')','')
				m = f.split(',')
				CleaningUpLines.append(m)
			for i in CleaningUpLines:
				j = [i[0][1:-1],i[1][2:-1],i[2][2:-1],i[3][2:-1],i[4][2:-1],i[5][2:-1]]
				FirstDraftofFinalOG.append(j)
			for i in FirstDraftofFinalOG:
				print(i)
				for k in DraftExonList3:
					if i[4] == k[0]:
						f = i[0],i[1],i[2],i[3],i[4],i[5],k[2],k[3]
						#print(f)
		'''for i in DraftFinalList1:
			for k in DraftExonList3:
				if i[4] == k[0]:
					j = i[0],i[1],i[2],i[3],i[4],i[5],k[2],k[3]
					DraftFinalList2.append(j)
					print(DraftFinalList2)'''
	def ToyDataTest():
		'''I made this function so I could test on a smaller subset of my data, so I could work out any kinks in my analysis!'''
		import csv

		CleaningUpLines = []
		RawExorthistOutput = []
		TestDataForExonOG = []
		ToyDataFromExorthistFile = []
		templist = []

		#For Human Exorthist Subgroups
		HumanMouse = []
		HumanRat = []
		HumanOpossum = []
		HumanMacaque = []
		HumanChicken = []
		HumanRabbit = []

		#For Mouse Exorthist Subgroups
		MouseHuman = []
		MouseRat = []
		MouseOpossum = []
		MouseMacaque = []
		MouseChicken = []
		MouseRabbit = []

		#For Rat Exorthist Subgroups
		RatHuman = []
		RatMouse = []
		RatOpossum = []
		RatMacaque = []
		RatChicken = []
		RatRabbit = []

		#For Opossum Exorthist Subgroups
		OpossumHuman = []
		OpossumMouse = []
		OpossumRat = []
		OpossumMacaque = []
		OpossumChicken = []
		OpossumRabbit = []

		#For Chicken Exorthist Subgroups
		ChickenHuman = []
		ChickenMouse = []
		ChickenRat = []
		ChickenMacaque = []
		ChickenRabbit = []
		ChickenOpossum = []

		#For Macaque Exorthist Subgroups
		MacaqueHuman = []
		MacaqueMouse = []
		MacaqueRat = []
		MacaqueRabbit = []
		MacaqueOpossum = []
		MacaqueChicken = []

		#For Rabbit Exorthist Subgroups
		RabbitHuman = []
		RabbitMouse = []
		RabbitRat = []
		RabbitOpossum = []
		RabbitChicken = []
		RabbitMacaque = []

		#Draft Exogroups
		DraftHumanExoGroups1 = []
		DraftHumanExoGroups2 = []
		DraftHumanExoGroups3 = []
		DraftHumanExoGroups4 = []
		DraftHumanExoGroups5 = []
		FinalHumanExoGroups = []

		#Importing Exorthist Output and creating subset
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/TestDataForExonOrthogroups/TestGroup2.txt') as read_obj1:
			for i in read_obj1:
				x = i.replace('[','')
				v = x.replace(']','')
				m = v.replace('\n','')
				l = m.split(',')
				j = [l[0][1:-1],l[1][2:-1],l[2][2:-1],l[3][2:-1],l[4][2:-1],l[5][2:-1],l[6][2:-1]]
				CleaningUpLines.append(j)

		#Using Bens Method to pull all pairwise observations out of exorthist raw data
		'''with open('/Users/memelord/Desktop/Rohlfs Lab Files/Exon Orthogroups/filtered_best_scored_EX_matches_by_targetgene.tab') as read_obj0:
			data_reader0 = csv.reader(read_obj0, delimiter='\t')
			for i in data_reader0:
				RawExorthistOutput.append(i)
		for i in CleaningUpLines:
			for v in i:
				for j in RawExorthistOutput:
					if v in j:
						print(j)'''

		#Importing Exorthist Subset of Output
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/TestDataForExonOrthogroups/TestPairwiseExorthistOutput2.tab') as read_obj1:
			data_reader = csv.reader(read_obj1, delimiter='\t')
			#Saving Exorthist Output to List
			for i in data_reader:
				#Modified for Subset of Exorthist Data:
				for v in i:
					j = v.split(',')
					e = j[0]+','+j[1],j[2]+','+j[3],j[4],j[5]
					RawExorthistOutput.append(e)
			for i in CleaningUpLines:
				for k in i:
					TestDataForExonOG.append(k)
			for i in TestDataForExonOG:
				for k in RawExorthistOutput:
					if i in k[0]:
						ToyDataFromExorthistFile.append(k)
					if i in k[1]:
						ToyDataFromExorthistFile.append(k)

			#Sorting all pairwise combinations into their various species pairs:
			for i in ToyDataFromExorthistFile:
				#Human & Every Other Species:
				if i[2] == 'Human':
					if i[3] == 'Mouse':
						HumanMouse.append(i)
				if i[2] == 'Human':
					if i[3] == 'Rat':
						HumanRat.append(i)
				if i[2] == 'Human':
					if i[3] == 'Opossum':
						HumanOpossum.append(i)
				if i[2] == 'Human':
					if i[3] == 'Macaque':
						HumanMacaque.append(i)
				if i[2] == 'Human':
					if i[3] == 'Chicken':
						HumanChicken.append(i)
				if i[2] == 'Human':
					if i[3] == 'Rabbit':
						HumanRabbit.append(i)

				#Mouse and Every Other Species:
				if i[2] == 'Mouse':
					if i[3] == 'Human':
						MouseHuman.append(i)
				if i[2] == 'Mouse':
					if i[3] == 'Rat':
						MouseRat.append(i)
				if i[2] == 'Mouse':
					if i[3] == 'Opossum':
						MouseOpossum.append(i)
				if i[2] == 'Mouse':
					if i[3] == 'Macaque':
						MouseMacaque.append(i)
				if i[2] == 'Mouse':
					if i[3] == 'Chicken':
						MouseChicken.append(i)
				if i[2] == 'Mouse':
					if i[3] == 'Rabbit':
						MouseRabbit.append(i)

				#Rat and Every Other Species:
				if i[2] == 'Rat':
					if i[3] == 'Mouse':
						RatMouse.append(i)
				if i[2] == 'Rat':
					if i[3] == 'Human':
						RatHuman.append(i)
				if i[2] == 'Rat':
					if i[3] == 'Opossum':
						RatOpossum.append(i)
				if i[2] == 'Rat':
					if i[3] == 'Macaque':
						RatMacaque.append(i)
				if i[2] == 'Rat':
					if i[3] == 'Chicken':
						RatChicken.append(i)
				if i[2] == 'Rat':
					if i[3] == 'Rabbit':
						RatRabbit.append(i)

				#Opossum and Every Other Species:
				if i[2] == 'Opossum':
					if i[3] == 'Mouse':
						OpossumMouse.append(i)
				if i[2] == 'Opossum':
					if i[3] == 'Human':
						OpossumHuman.append(i)
				if i[2] == 'Opossum':
					if i[3] == 'Rat':
						OpossumRat.append(i)
				if i[2] == 'Opossum':
					if i[3] == 'Macaque':
						OpossumMacaque.append(i)
				if i[2] == 'Opossum':
					if i[3] == 'Chicken':
						OpossumChicken.append(i)
				if i[2] == 'Opossum':
					if i[3] == 'Rabbit':
						OpossumRabbit.append(i)

				#Chicken and Every Other Species:
				if i[2] == 'Chicken':
					if i[3] == 'Mouse':
						ChickenMouse.append(i)
				if i[2] == 'Chicken':
					if i[3] == 'Human':
						ChickenHuman.append(i)
				if i[2] == 'Chicken':
					if i[3] == 'Opossum':
						ChickenOpossum.append(i)
				if i[2] == 'Chicken':
					if i[3] == 'Macaque':
						ChickenMacaque.append(i)
				if i[2] == 'Chicken':
					if i[3] == 'Rat':
						ChickenRat.append(i)
				if i[2] == 'Chicken':
					if i[3] == 'Rabbit':
						ChickenRabbit.append(i)

				#Macaque and Every Other Species:
				if i[2] == 'Macaque':
					if i[3] == 'Mouse':
						MacaqueMouse.append(i)
				if i[2] == 'Macaque':
					if i[3] == 'Human':
						MacaqueHuman.append(i)
				if i[2] == 'Macaque':
					if i[3] == 'Opossum':
						MacaqueOpossum.append(i)
				if i[2] == 'Macaque':
					if i[3] == 'Chicken':
						MacaqueChicken.append(i)
				if i[2] == 'Macaque':
					if i[3] == 'Rat':
						MacaqueRat.append(i)
				if i[2] == 'Macaque':
					if i[3] == 'Rabbit':
						MacaqueRabbit.append(i)

				#Rabbit and Every Other Species:
				if i[2] == 'Rabbit':
					if i[3] == 'Mouse':
						RabbitMouse.append(i)
				if i[2] == 'Rabbit':
					if i[3] == 'Human':
						RabbitHuman.append(i)
				if i[2] == 'Rabbit':
					if i[3] == 'Opossum':
						RabbitOpossum.append(i)
				if i[2] == 'Rabbit':
					if i[3] == 'Chicken':
						RabbitChicken.append(i)
				if i[2] == 'Rabbit':
					if i[3] == 'Rat':
						RabbitRat.append(i)
				if i[2] == 'Rabbit':
					if i[3] == 'Macaque':
						RabbitMacaque.append(i)

			#Final Human Lists without redundancy
			FiHumanMouse = list(map(list,(set(map(tuple,HumanMouse)))))
			FiHumanRat = list(map(list,(set(map(tuple,HumanRat)))))
			FiHumanOpossum = list(map(list,(set(map(tuple,HumanOpossum)))))
			FiHumanMacaque = list(map(list,(set(map(tuple,HumanMacaque)))))
			FiHumanChicken = list(map(list,(set(map(tuple,HumanChicken)))))
			FiHumanRabbit = list(map(list,(set(map(tuple,HumanRabbit)))))

			#Final Mouse Lists without redundancy
			FiMouseHuman = list(map(list,(set(map(tuple,MouseHuman)))))
			FiMouseRat = list(map(list,(set(map(tuple,MouseRat)))))
			FiMouseOpossum = list(map(list,(set(map(tuple,MouseOpossum)))))
			FiMouseMacaque = list(map(list,(set(map(tuple,MouseMacaque)))))
			FiMouseChicken = list(map(list,(set(map(tuple,MouseChicken)))))
			FiMouseRabbit = list(map(list,(set(map(tuple,MouseRabbit)))))

			#Final Rat Lists without redundancy
			FiRatHuman = list(map(list,(set(map(tuple,RatHuman)))))
			FiRatMouse = list(map(list,(set(map(tuple,RatMouse)))))
			FiRatOpossum = list(map(list,(set(map(tuple,RatOpossum)))))
			FiRatMacaque = list(map(list,(set(map(tuple,RatMacaque)))))
			FiRatChicken = list(map(list,(set(map(tuple,RatChicken)))))
			FiRatRabbit = list(map(list,(set(map(tuple,RatRabbit)))))

			#Final Opossum Lists without redundancy
			FiOpossumHuman = list(map(list,(set(map(tuple,OpossumHuman)))))
			FiOpossumMouse = list(map(list,(set(map(tuple,OpossumMouse)))))
			FiOpossumRat = list(map(list,(set(map(tuple,OpossumRat)))))
			FiOpossumMacaque = list(map(list,(set(map(tuple,OpossumMacaque)))))
			FiOpossumChicken = list(map(list,(set(map(tuple,OpossumChicken)))))
			FiOpossumRabbit = list(map(list,(set(map(tuple,OpossumRabbit)))))

			#Final Chicken Lists without redundancy
			FiChickenHuman = list(map(list,(set(map(tuple,ChickenHuman)))))
			FiChickenMouse = list(map(list,(set(map(tuple,ChickenMouse)))))
			FiChickenRat = list(map(list,(set(map(tuple,ChickenRat)))))
			FiChickenMacaque = list(map(list,(set(map(tuple,ChickenMacaque)))))
			FiChickenRabbit = list(map(list,(set(map(tuple,ChickenRabbit)))))
			FiChickenOpossum = list(map(list,(set(map(tuple,ChickenOpossum)))))

			#Final Macaque Lists without redundancy
			FiMacaqueHuman = list(map(list,(set(map(tuple,MacaqueHuman)))))
			FiMacaqueMouse = list(map(list,(set(map(tuple,MacaqueMouse)))))
			FiMacaqueRat = list(map(list,(set(map(tuple,MacaqueRat)))))
			FiMacaqueRabbit = list(map(list,(set(map(tuple,MacaqueRabbit)))))
			FiMacaqueOpossum = list(map(list,(set(map(tuple,MacaqueOpossum)))))
			FiMacaqueChicken = list(map(list,(set(map(tuple,MacaqueChicken)))))

			#Final Rabbit Lists without redundancy
			FiRabbitHuman = list(map(list,(set(map(tuple,RabbitHuman)))))
			FiRabbitMouse = list(map(list,(set(map(tuple,RabbitMouse)))))
			FiRabbitRat = list(map(list,(set(map(tuple,RabbitRat)))))
			FiRabbitOpossum = list(map(list,(set(map(tuple,RabbitOpossum)))))
			FiRabbitChicken = list(map(list,(set(map(tuple,RabbitChicken)))))
			FiRabbitMacaque = list(map(list,(set(map(tuple,RabbitMacaque)))))

			#Empty Lists
			Box1 = []
			Box2 = []
			Box3 = []
			Box4 = []
			Box5 = []
			Box6 = []
			Box7 = []
			Box8 = []
			
			#Symmetric Pairwise Structures
			HumanMouseSymmetry = []
			HumanChickenSymmetry = []
			HumanRatSymmetry = []
			HumanRabbitSymmetry = []
			HumanOpossumSymmetry = []
			HumanMacaqueSymmetry = []

			MouseChickenSymmetry = []
			MouseRatSymmetry = []
			MouseRabbitSymmetry = []
			MouseOpossumSymmetry = []
			MouseMacaqueSymmetry = []

			ChickenRatSymmetry = []
			ChickenRabbitSymmetry = []
			ChickenOpossumSymmetry = []
			ChickenMacaqueSymmetry = []

			RatRabbitSymmetry = []
			RatOpossumSymmetry = []
			RatMacaqueSymmetry = []

			RabbitOpossumSymmetry = []
			RabbitMacaqueSymmetry = []

			OpossumMacaqueSymmetry = []

			#Checking Pairwise Symmetry for Human and X:
			for i in FiHumanMouse:
				for j in FiMouseHuman:
					if i[0] == j[1]:
						if j[0] == i[1]:
							HMSymmetry = [i[0],i[1]]
							HumanMouseSymmetry.append(HMSymmetry)
			for i in FiHumanChicken:
				for j in FiChickenHuman:
					if i[0] == j[1]:
						if j[0] == i[1]:
							HCSymmetry = [i[0],i[1]]
							HumanChickenSymmetry.append(HCSymmetry)
			for i in FiHumanRat:
				for j in FiRatHuman:
					if i[0] == j[1]:
						if j[0] == i[1]:
							HRSymmetry = [i[0],i[1]]
							HumanRatSymmetry.append(HRSymmetry)
			for i in FiHumanRabbit:
				for j in FiRabbitHuman:
					if i[0] == j[1]:
						if j[0] == i[1]:
							HRSymmetry = [i[0],i[1]]
							HumanRabbitSymmetry.append(HRSymmetry)
			for i in FiHumanOpossum:
				for j in FiOpossumHuman:
					if i[0] == j[1]:
						if j[0] == i[1]:
							HOSymmetry = [i[0],i[1]]
							HumanOpossumSymmetry.append(HOSymmetry)
			for i in FiHumanMacaque:
				for j in FiMacaqueHuman:
					if i[0] == j[1]:
						if j[0] == i[1]:
							HMSymmetry = [i[0],i[1]]
							HumanMacaqueSymmetry.append(HMSymmetry)

			#Checking Pairwise Symmetry for Mouse and X
			for i in FiMouseChicken:
				for j in FiChickenMouse:
					if i[0] == j[1]:
						if j[0] == i[1]:
							MCSymmetry = [i[0],i[1]]
							MouseChickenSymmetry.append(MCSymmetry)
			for i in FiMouseRat:
				for j in FiRatMouse:
					if i[0] == j[1]:
						if j[0] == i[1]:
							MRSymmetry = [i[0],i[1]]
							MouseRatSymmetry.append(MRSymmetry)
			for i in FiMouseRabbit:
				for j in FiRabbitMouse:
					if i[0] == j[1]:
						if j[0] == i[1]:
							MRSymmetry = [i[0],i[1]]
							MouseRabbitSymmetry.append(MRSymmetry)
			for i in FiMouseOpossum:
				for j in FiOpossumMouse:
					if i[0] == j[1]:
						if j[0] == i[1]:
							MOSymmetry = [i[0],i[1]]
							MouseOpossumSymmetry.append(MOSymmetry)
			for i in FiMouseMacaque:
				for j in FiMacaqueMouse:
					if i[0] == j[1]:
						if j[0] == i[1]:
							MMSymmetry = [i[0],i[1]]
							MouseMacaqueSymmetry.append(MMSymmetry)

			#Checking Pairwise Symmetry for Chicken and X
			for i in FiChickenRat:
				for j in FiRatChicken:
					if i[0] == j[1]:
						if j[0] == i[1]:
							CRSymmetry = [i[0],i[1]]
							ChickenRatSymmetry.append(CRSymmetry)
			for i in FiChickenRabbit:
				for j in FiRabbitChicken:
					if i[0] == j[1]:
						if j[0] == i[1]:
							CRSymmetry = [i[0],i[1]]
							ChickenRabbitSymmetry.append(CRSymmetry)
			for i in FiChickenOpossum:
				for j in FiOpossumChicken:
					if i[0] == j[1]:
						if j[0] == i[1]:
							COSymmetry = [i[0],i[1]]
							ChickenOpossumSymmetry.append(COSymmetry)
			for i in FiChickenMacaque:
				for j in FiMacaqueChicken:
					if i[0] == j[1]:
						if j[0] == i[1]:
							CMSymmetry = [i[0],i[1]]
							ChickenMacaqueSymmetry.append(CMSymmetry)
			
			#Checking Pairwise Symmetry for Rat and X
			for i in FiRatRabbit:
				for j in FiRabbitRat:
					if i[0] == j[1]:
						if j[0] == i[1]:
							RRSymmetry = [i[0],i[1]]
							RatRabbitSymmetry.append(RRSymmetry)
			for i in FiRatOpossum:
				for j in FiOpossumRat:
					if i[0] == j[1]:
						if j[0] == i[1]:
							ROSymmetry = [i[0],i[1]]
							RatOpossumSymmetry.append(ROSymmetry)
			for i in FiRatMacaque:
				for j in FiMacaqueRat:
					if i[0] == j[1]:
						if j[0] == i[1]:
							RMSymmetry = [i[0],i[1]]
							RatMacaqueSymmetry.append(RMSymmetry)
			
			#Checking Pairwise Symmetry for Rabbit and X
			for i in FiRabbitOpossum:
				for j in FiOpossumRabbit:
					if i[0] == j[1]:
						if j[0] == i[1]:
							ROSymmetry = [i[0],i[1]]
							RabbitOpossumSymmetry.append(ROSymmetry)
			for i in FiRabbitMacaque:
				for j in FiMacaqueRabbit:
					if i[0] == j[1]:
						if j[0] == i[1]:
							RMSymmetry = [i[0],i[1]]
							RabbitMacaqueSymmetry.append(RMSymmetry)

			#Checking Pairwise Symmetry for Opossum and X
			for i in FiOpossumMacaque:
				for j in FiMacaqueOpossum:
					if i[0] == j[1]:
						if j[0] == i[1]:
							OMSymmetry = [i[0],i[1]]
							OpossumMacaqueSymmetry.append(OMSymmetry)

			#Creating Exon Orthogroups from Species Pairwise Information:

			#Adding Human + Mouse + Chicken to Box Element using Human as marker (human is checked)
			for i in HumanMouseSymmetry:
				for j in HumanChickenSymmetry:
					if i[0] == j[0]:
						BoxElement1 = [i[0],i[1],j[1]]
						Box1.append(BoxElement1)
			#Checking if Chicken and Mouse Match
			for i in Box1:
				for j in MouseChickenSymmetry:
					if i[1] == j[0]:
						if i[2] == j[1]:
							BoxElement2 = [i[0],i[1],i[2]]
							Box2.append(BoxElement2)
			#Adding Rat
			for i in Box2:
				for j in HumanRatSymmetry:
					if i[0] == j[0]:
						BoxElement3 = [i[0],i[1],i[2],j[1]]
						Box3.append(BoxElement3)
			#Checking if Rat matches Mouse and Chicken
			for i in Box3:
				for j in MouseRatSymmetry:
					for k in ChickenRatSymmetry:
						if i[3] == j[1]:
							if i[2] == k[0]:
								BoxElement4 = [i[0],i[1],i[2],i[3]]
								Box4.append(BoxElement4)
			#Adding Rabbit
			for i in Box4:
				for j in HumanRabbitSymmetry:
					if i[0] == j[0]:
						BoxElement5 = [i[0],i[1],i[2],i[3],j[1]]
						Box5.append(BoxElement5)
			#Checking if Rabbit matches Mouse, Chicken, and Rat
			for i in Box5:
				for j in MouseRabbitSymmetry:
					for k in ChickenRabbitSymmetry:
						for l in RatRabbitSymmetry:
							if i[1] == j[0]:
								if i[2] == k[0]:
									if i[3] == l[0]:







if __name__ == '__main__':
	'''x = DataAnal.BensMethod()
	z = DataAnal.AnalyzingBothMethods()
	DataAnal.MethodMatrixes(x, z)'''
	#x = DataAnal.OrthogroupswithGeneNames()
	#DataAnal.EVEMatrixMaker(x)
	DataAnal.ToyDataTest()
	#DataAnal.ExorthistMatrixMaker()


