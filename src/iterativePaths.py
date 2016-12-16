#!/usr/bin/python

'''
Developer: Adam Terwilliger
Purpose: MTH 496
Details: Senior thesis in Mathematics at
            Grand Valley State University
'''

import itertools as it
import numpy as np
import sys


np.set_printoptions(linewidth=1000)
np.set_printoptions(threshold='nan')


def main():

	if ( len(sys.argv) != 2 ):
		print 'program parameters incorrect'
		print 'usage: ./prog.py size '
		sys.exit(2)    
	else:
		exampleKey = int(sys.argv[1])


	operations = ['U','D','S']

	#maxPathLen = 15
	#maxPathLen = 10

	maxPathLen = 2 * exampleKey + 1

	possiblePaths = []

	pathDict = {}
	lexPathDict = {}

	for m in range(maxPathLen):
		possiblePaths = possiblePaths + [''.join(i) for i in it.product(operations, repeat = m)]

	for path in possiblePaths:
	
		if isValidPath(path):
			size = getPathSize(path)

			if size not in pathDict:
				pathDict[size] = [path]
			else:
				pathDict[size].append(path)

	#for key in pathDict:
		#print key, pathDict[key], len(pathDict[key])
		#print key, len(pathDict[key])

	#exampleKey = 4
	lexList = []
	edgeList = []
	for path in pathDict[exampleKey]:
		#print exampleKey, path, lexMapPath(path) 
		pathEdgeList = ruleStoDU(path) + ruleUDtoS(path)
		for vertex in pathEdgeList:
			edgeList.append((lexMapPath(path),vertex))	
		lexList.append(lexMapPath(path))

	sLexList = sorted(lexList)

	lexMatrix = np.zeros([len(lexList),len(lexList)], dtype=np.int)

	#for path in sLexList:
	#	print path, sLexList.index(path)

	for i in range(len(edgeList)):
		vertex0index = sLexList.index(edgeList[i][0])
		vertex1index = sLexList.index(edgeList[i][1])
		#print edgeList[i], vertex0index, vertex1index
		lexMatrix[vertex0index,vertex1index] = 1


	diffIandX = np.identity(len(lexList)) - lexMatrix

	lexInvMatrix = np.linalg.inv(diffIandX).astype(np.int)

	colSums = np.sum(lexInvMatrix, axis=0).tolist()
	rowSums = np.sum(lexInvMatrix, axis=1).tolist()

	dupColSums = set([x for x in colSums if colSums.count(x) > 1])
	dupRowSums = set([x for x in rowSums if rowSums.count(x) > 1])

	freqColSums = [[x,colSums.count(x)] for x in set(colSums)]
	freqRowSums = [[x,rowSums.count(x)] for x in set(rowSums)]

	fcs = 0
	for i in range(len(freqColSums)):
		if freqColSums[i][1] == 2:
			fcs+=1
	frs = 0
	for i in range(len(freqRowSums)):
		if freqRowSums[i][1] == 2:
			frs+=1

	print "Size:", exampleKey

	print "Num colSums:", len(colSums)
	print "Num rowSums:", len(rowSums)

	print "Num dupColSums:", len(dupColSums)
	print "Num dupRowSums:", len(dupRowSums)
	
	print "Amount of col pairs:", fcs
	print "Amount of row pairs:", frs

	print "freqColSums:", freqColSums
	print "freqRowSums:", freqRowSums

	print "colSums:", colSums
	print "rowSums:", rowSums
	print "dupColSums:", dupColSums
	print "dupRowSums:", dupRowSums

	#print 'Dimensions of Matrix:', lexMatrix.shape

	#print 'Column Sums of Original:', np.sum(lexMatrix, axis=0)
	#print 'Row Sums of Original:', np.sum(lexMatrix, axis=1)

	#print 'Column Sums of (I-X)^-1:',np.sum(lexInvMatrix, axis=0)
	#print 'Row Sums of (I-X)^-1:',np.sum(lexInvMatrix, axis=1)

	#print lexMatrix
	#print lexInvMatrix

	#examplePath = 'SUUUSSSDDDS'

	#print ruleStoDU(examplePath)
	#print ruleUDtoS(examplePath)

	'''
	for i in range(len(examplePath)):
		newPath = examplePath
		if examplePath[i] == 'S':
			newPath = examplePath[:i] + 'DU' + examplePath[i+1:]
			print i
			print 'Original:', examplePath, isValidPath(examplePath), getPathSize(examplePath)
			print 'New:     ', newPath, isValidPath(newPath), getPathSize(newPath)
			print '\n'
	
	Ulist = []
	for i in range(len(examplePath)):
		newPath = examplePath
		if examplePath[i] == 'U':
			Ulist.append(i)
		if examplePath[i] == 'D':
			currU = Ulist.pop()
			currD = i
			stringBeforeU = examplePath[:currU]
			stringBetweenUandD = examplePath[currU+1:currD]
			stringAfterD = examplePath[currD+1:]

			newPathBefore = stringBeforeU + 'S' + stringBetweenUandD + stringAfterD
			newPathAfter = stringBeforeU + stringBetweenUandD + 'S' + stringAfterD

			print currU, currD
			print 'Original:  ', examplePath, isValidPath(examplePath), getPathSize(examplePath)
			#if newPathBefore == newPathAfter:
			#	print newPathBefore, isValidPath(newPathBefore), getPathSize(examplePath)
			#else:
			print 'New Before:', newPathBefore, isValidPath(newPathBefore), getPathSize(examplePath)
			print 'New After: ', newPathAfter, isValidPath(newPathAfter), getPathSize(examplePath)
			print '\n'

		print examplePath, lexMapPath(examplePath)
	'''
	
def isValidPath(myPath):
	unbalanced = 0
	belowAxis = 0
	for char in myPath:
		if char == 'U':
			unbalanced +=1
		if char == 'D':
			unbalanced -=1
		if unbalanced < belowAxis:
			belowAxis = unbalanced

	if (unbalanced == 0) and (belowAxis == 0):
		#print path, belowAxis, unbalanced, size
		valid = 1
	else:
		valid = 0

	return valid


def getPathSize(myPath):
	size = 0
	for char in myPath:
		if char == 'U' or char == 'S':
			size += 1
	return size

def lexMapPath(myPath):
	newPath = ''
	myMap = {'U':'a', 'S':'b', 'D':'c'}
	for i in range(len(myPath)):
		newPath = newPath + myMap[myPath[i]]
	return newPath

def ruleStoDU(myPath):
	StoDUlist = []
	for i in range(len(myPath)):
		if myPath[i] == 'S':
			newPath = myPath[:i] + 'DU' + myPath[i+1:]
			if isValidPath(newPath):
				StoDUlist.append(lexMapPath(newPath))

	return StoDUlist
	
def ruleUDtoS(myPath):
	UDtoSlist = []
	Ulist = []
	for i in range(len(myPath)):
		newPath = myPath
		if myPath[i] == 'U':
			Ulist.append(i)
		if myPath[i] == 'D':
			currU = Ulist.pop()
			currD = i
			stringBeforeU = myPath[:currU]
			stringBetweenUandD = myPath[currU+1:currD]
			stringAfterD = myPath[currD+1:]

			newPathBefore = stringBeforeU + 'S' + stringBetweenUandD + stringAfterD
			newPathAfter = stringBeforeU + stringBetweenUandD + 'S' + stringAfterD

			if isValidPath(newPathBefore) and newPathBefore == newPathAfter:
				UDtoSlist.append(lexMapPath(newPathBefore))
			else:
				if isValidPath(newPathBefore):
					UDtoSlist.append(lexMapPath(newPathBefore))
				if isValidPath(newPathAfter):
					UDtoSlist.append(lexMapPath(newPathAfter))

	return UDtoSlist


if __name__ == "__main__":
    main()
