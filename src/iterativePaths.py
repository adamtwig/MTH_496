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

# print options allow for long lines to print
np.set_printoptions(linewidth=1000)
np.set_printoptions(threshold='nan')

def main():

	# user inputs length of path (#U + #S)
	if ( len(sys.argv) != 2 ):
		print 'program parameters incorrect'
		print 'usage: ./prog.py size '
		sys.exit(2)    
	else:
		exampleKey = int(sys.argv[1])


	# only operations are up, down, straight
	operations = ['U','D','S']

	# max string length is twice the path size (all UD steps)
	maxPathLen = 2 * exampleKey + 1

	# initialize data structures
	possiblePaths = []
	pathDict = {}
	lexPathDict = {}

	# generate all possible strings
	for m in range(maxPathLen):
		possiblePaths = possiblePaths + [''.join(i) for i in it.product(operations, repeat = m)]

	# filter out only paths we are interested in
	for path in possiblePaths:
	
		if isValidPath(path):
			size = getPathSize(path)

			# key to dict is size (collect all paths for specific size)
			if size not in pathDict:
				pathDict[size] = [path]
			else:
				pathDict[size].append(path)

	# if desire to print all paths
	#for key in pathDict:
		#print key, pathDict[key], len(pathDict[key])
		#print key, len(pathDict[key])

	lexList = []
	edgeList = []
	# map paths to lexiographic notation 
	for path in pathDict[exampleKey]:
		pathEdgeList = ruleStoDU(path) + ruleUDtoS(path)
		for vertex in pathEdgeList:
			edgeList.append((lexMapPath(path),vertex))	
		lexList.append(lexMapPath(path))

	# sort paths based on lexiographic ordering
	sLexList = sorted(lexList)

	# initialize adj matrix to all 0s
	lexMatrix = np.zeros([len(lexList),len(lexList)], dtype=np.int)

	# get vertex indices and set path between them
	for i in range(len(edgeList)):
		vertex0index = sLexList.index(edgeList[i][0])
		vertex1index = sLexList.index(edgeList[i][1])
		lexMatrix[vertex0index,vertex1index] = 1

	# get diff between identity and adj matrix
	diffIandX = np.identity(len(lexList)) - lexMatrix

	# take inverse of matrix (we know it's invertibile
	#	because diagonal is all 1s and lower triangle is all 0s
	lexInvMatrix = np.linalg.inv(diffIandX).astype(np.int)

	# get column and row sums for (I-X)^-1
	colSums = np.sum(lexInvMatrix, axis=0).tolist()
	rowSums = np.sum(lexInvMatrix, axis=1).tolist()
	
	print 'Dimensions of Matrix:', lexMatrix.shape

	print 'Column Sums of (I-X)^-1:',np.sum(lexInvMatrix, axis=0)
	print 'Row Sums of (I-X)^-1:',np.sum(lexInvMatrix, axis=1)
	
	# print adj matrix and (I-X)^-1 matrix
	print lexMatrix
	print lexInvMatrix

	'''
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

	# collect stats about row/col sums
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
	'''
	
def isValidPath(myPath):
	"""
	@summary: returns 0/1 (True/False) if path is valid
		-- makes sure path is balanced with U and D steps
		-- makes sure path does not go below x axis
	"""

	unbalanced = 0
	belowAxis = 0
	valid = 0
	for char in myPath:
		if char == 'U':
			unbalanced +=1
		if char == 'D':
			unbalanced -=1
		if unbalanced < belowAxis:
			belowAxis = unbalanced

	if (unbalanced == 0) and (belowAxis == 0):
		valid = 1

	return valid


def getPathSize(myPath):
	"""
	@summary: returns size of path
		-- number of up steps + straight steps
	"""
	size = 0
	for char in myPath:
		if char == 'U' or char == 'S':
			size += 1
	return size


def lexMapPath(myPath):
	"""
	@summary: map path to lexiographically 
				ordered version
	"""
	newPath = ''
	myMap = {'U':'a', 'S':'b', 'D':'c'}
	for i in range(len(myPath)):
		newPath = newPath + myMap[myPath[i]]
	return newPath

def ruleStoDU(myPath):
	"""
	@summary: turns straight steps into down-up
	"""
	StoDUlist = []
	for i in range(len(myPath)):
		if myPath[i] == 'S':
			newPath = myPath[:i] + 'DU' + myPath[i+1:]
			if isValidPath(newPath):
				StoDUlist.append(lexMapPath(newPath))

	return StoDUlist
	
def ruleUDtoS(myPath):
	"""
	@summary: turns up-down pairs into straight steps
	"""
	UDtoSlist = []
	Ulist = []
	for i in range(len(myPath)):
		newPath = myPath
		# create a list of where up steps are
		if myPath[i] == 'U':
			Ulist.append(i)
		# as you find down steps, pop off corresponding up steps
		if myPath[i] == 'D':
			currU = Ulist.pop()
			currD = i
			stringBeforeU = myPath[:currU]
			stringBetweenUandD = myPath[currU+1:currD]
			stringAfterD = myPath[currD+1:]

			# create new path by adding straight step to left of remaining path 
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
