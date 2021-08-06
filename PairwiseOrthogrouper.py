#Authors: Imon Islam (iislam@ucsc.edu)
#EVEDataSorter.py
#August 5th, 2021
#San Francisco State University
'''A script for creating Gene Orthogroups across several species'''

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
	def BensMethod():
		#Human vs Mouse Pairwise Analysis
		FilteredHumanMouse = []
		#Exploring Ben's Method for creating 1:1:1:1:1:1 Orthogroups!
		
		#Replace the path with the destination of your 6 seperate files:
		
		#Human vs Mouse Pairwise Analysis
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/mart_export.txt', 'r') as read_obj:
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
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/mart_export-2.txt', 'r') as read_obj:
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
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/mart_export-3.txt', 'r') as read_obj:
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
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/mart_export-4.txt', 'r') as read_obj:
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
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/mart_export-5.txt', 'r') as read_obj:
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
		with open ('/Users/memelord/Desktop/Rohlfs Lab Files/BensMethod/mart_export-6.txt', 'r') as read_obj:
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
		for i in FinallyDone:
			print(i)

if __name__ == '__main__':
	DataAnal.BensMethod()
