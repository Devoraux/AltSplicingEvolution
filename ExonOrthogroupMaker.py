#Authors: Imon Islam (iislam@ucsc.edu)
#ExonOrthogroupMaker
#August 5th, 2021
#San Francisco State University
'''A script for creating Exon Orthogroups across several species'''

import sys
import csv
from csv import reader
from collections import Counter
import os

class DataAnal(object):
	def ExonOrthogroupMaker():
		'''Final Code to create Exon Orthogroups using Exorthist Output'''

		import csv

		CleaningUpLines = []
		RawExorthistOutput = []
		FullDataForExonOG = []
		FullDataFromExorthistFile = []
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

		#Empty Lists
		Box1 = []
		Box2 = []
		Box3 = []
		Box4 = []
		Box5 = []
		Box6 = []
		Box7 = []
		Box8 = []
		Box9 = []
		Box10 = []
		Box11 = []
		Box12 = []
		Box13 = []
		BoxZ = []
		BoxF = []
		BoxL = []
		BoxM = []
		BoxV = []
		BoxG = []
		BoxN = []
		BoxE = []
			
		#Symmetric Pairwise Lists
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


		#Importing Exorthist Output and creating subset
		'''with open ('/Users/memelord/Desktop/Rohlfs Lab Files/TestDataForExonOrthogroups/TestGroups/TestGroup8.txt') as read_obj1:
			for i in read_obj1:
				x = i.replace('[','')
				v = x.replace(']','')
				m = v.replace('\n','')
				l = m.split(',')
				j = [l[0][1:-1],l[1][2:-1],l[2][2:-1],l[3][2:-1],l[4][2:-1],l[5][2:-1],l[6][2:-1]]
				CleaningUpLines.append(j)'''

		#Using Bens Method to pull all pairwise observations out of exorthist raw data
		with open('/Users/memelord/Desktop/Rohlfs Lab Files/Exon Orthogroups/filtered_best_scored_EX_matches_by_targetgene.tab') as read_obj0:
			data_reader0 = csv.reader(read_obj0, delimiter='\t')
			for i in data_reader0:
				RawExorthistOutput.append(i)
		for i in CleaningUpLines:
			for v in i:
				for j in RawExorthistOutput:
					if v in j:
						print(j)

		#Path for using test group to check if this program works:
		#/Users/memelord/Desktop/Rohlfs Lab Files/TestDataForExonOrthogroups/TestPairwiseExorthistOutput2.tab

		#Path for Glycine Server
		#/home/rohlfslab/Imons_Files/TestPairwiseExorthistOutput.tab

		#Path for MixedGroupPairwise.tab

		#Path for Raw File (tab seperate)
		#/Users/memelord/Desktop/Rohlfs Lab Files/Exon Orthogroups/filtered_best_scored_EX_matches_by_targetgene.tab

		#Path for 1000 genes test group
		#/Users/memelord/Desktop/Rohlfs Lab Files/TestDataForExonOrthogroups/TestGroup3.txt

		#Importing Exorthist Output
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/TestDataForExonOrthogroups/Exon Orthogroup Subsets/ExonOrthogroupSubset7.txt') as read_obj1:
			data_reader = csv.reader(read_obj1, delimiter=',')
			for i in data_reader:
				RawExorthistOutput.append(i)
			for i in RawExorthistOutput:
				k = [i[0]+','+i[1],i[2]+','+i[3],i[4],i[5]]
				FullDataFromExorthistFile.append(k)
			#Sorting all pairwise combinations into their various species pairs:
			for i in FullDataFromExorthistFile:
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
			#Checking if Rat matches Mouse 
			for i in Box3:
				for j in MouseRatSymmetry:
					if i[3] == j[1]:
						BoxElementZ = [i[0],i[1],i[2],i[3]]
						BoxZ.append(BoxElementZ)
			#Checking if Rat matches Chicken
			for i in BoxZ:
				for k in ChickenRatSymmetry:
					if i[3] == k[1]:
						if i[2] == k[0]:
							BoxElement4 = [i[0],i[1],i[2],i[3]]
							Box4.append(BoxElement4)
			#Adding Rabbit by comparing Human
			for i in Box4:
				for j in HumanRabbitSymmetry:
					if i[0] == j[0]:
						BoxElement5 = [i[0],i[1],i[2],i[3],j[1]]
						Box5.append(BoxElement5)
			#Checking if Rabbit matches Mouse
			for i in Box5:
				for j in MouseRabbitSymmetry:
					if i[1] == j[0]:
						if i[4] == j[1]:
							BoxElementF = [i[0],i[1],i[2],i[3],i[4]]
							BoxF.append(BoxElementF)
			#Checking if Rabbit matches Chicken
			for i in BoxF:
				for k in ChickenRabbitSymmetry:
					if i[2] == k[0]:
						if i[4] == k[1]:
							BoxElementL = [i[0],i[1],i[2],i[3],i[4]]
							BoxL.append(BoxElementL)
			for i in BoxL:
				for l in RatRabbitSymmetry:
					if i[3] == l[0]:
						if i[4] == l[1]:
							BoxElement6 = [i[0],i[1],i[2],i[3],i[4]]
							Box6.append(BoxElement6)

			#Adding Opossum
			for i in Box6:
				for j in HumanOpossumSymmetry:
					if i[0] == j[0]:
						BoxElement7 = [i[0],i[1],i[2],i[3],i[4],j[1]]
						Box7.append(BoxElement7)

			#Checking if Opossum matches Mouse, and Chicken
			for i in Box7:
				for j in MouseOpossumSymmetry:
					if i[1] == j[0]:
						if i[5] == j[1]:
							BoxElementM = [i[0],i[1],i[2],i[3],i[4],i[5]]
							BoxM.append(BoxElementM)
			for i in BoxM:
				for k in ChickenOpossumSymmetry:
					if i[2] == k[0]:
						if i[5] == k[1]:
							BoxElement8 = [i[0],i[1],i[2],i[3],i[4],i[5]]
							Box8.append(BoxElement8)
			#Checking if Opossum matches Rat, and Rabbit
			for i in Box8:
				for j in RatOpossumSymmetry:
					if i[3] == j[0]:
						if i[5] == j[1]:
							BoxElementV = [i[0],i[1],i[2],i[3],i[4],i[5]]
							BoxV.append(BoxElementV)
			for i in BoxV:
				for k in RabbitOpossumSymmetry:
					if i[4] == k[0]:
						if i[5] == k[1]:
							BoxElement9 = [i[0],i[1],i[2],i[3],i[4],i[5]]
							Box9.append(BoxElement9)
			#Adding Macaque
			for i in Box9:
				for j in HumanMacaqueSymmetry:
					if i[0] == j[0]:
						BoxElement10 = [i[0],i[1],i[2],i[3],i[4],i[5],j[1]]
						Box10.append(BoxElement10)
			#Checking Macaque vs Mouse, Chicken
			for i in Box10:
				for j in MouseMacaqueSymmetry:
					if i[1] == j[0]:
						if i[6] == j[1]:
							BoxElement11 = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
							Box11.append(BoxElement11)

			for i in Box11:
				for k in ChickenMacaqueSymmetry:
					if i[6] == k[1]:
						if i[2] == k[0]:
							BoxElement12 = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
							Box12.append(BoxElement12)

			#Checking Macaque vs Rat, Rabbit, and Opossum
			for i in Box12:
				for j in RatMacaqueSymmetry:
					if i[3] == j[0]:
						if i[6] == j[1]:
							BoxElement13 = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
							Box13.append(BoxElement13)

			for i in Box13:
				for k in RabbitMacaqueSymmetry:
					if i[4] == k[0]:
						if i[6] == k[1]:
							BoxElementG = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
							BoxG.append(BoxElementG)
			for i in BoxG:
				for l in OpossumMacaqueSymmetry:
					if i[5] == l[0]:
						if i[6] == l[1]:
							BoxElementN = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
							BoxN.append(BoxElementN)
			for i in BoxN:
				print(i)
		return