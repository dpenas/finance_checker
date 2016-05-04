#!/usr/bin/python
import csv

class CSVParser:

	def parseCsv(self, file, delimiter='\t', quotechar='|'):
		transaction = []
		with open(file, 'r') as csvFile:
			rowReader = csv.reader(csvFile, delimiter=delimiter, quotechar=quotechar)
			for row in rowReader:
				transaction.append(row)
		return transaction

	def parse(self):
		return self.parseCsv('test.csv')


