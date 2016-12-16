import numpy as np
import string

myMatrix = np.zeros([11,11], dtype=np.int)
'''
myMatrix[0,0] = 1
myMatrix[1,1] = 1
myMatrix[2,2] = 1
myMatrix[3,3] = 1
myMatrix[4,4] = 1
myMatrix[5,5] = 1
myMatrix[6,6] = 1
myMatrix[7,7] = 1
myMatrix[8,8] = 1
myMatrix[9,9] = 1
myMatrix[10,10] = 1
'''
myMatrix[0,1] = 1
myMatrix[0,3] = 1
myMatrix[0,4] = 1

myMatrix[1,2] = 1
myMatrix[1,5] = 1

myMatrix[2,3] = 1
myMatrix[2,4] = 1

myMatrix[3,5] = 1
myMatrix[3,6] = 1

myMatrix[4,5] = 1
myMatrix[4,7] = 1

myMatrix[5,8] = 1
myMatrix[5,9] = 1

myMatrix[6,8] = 1

myMatrix[7,9] = 1

myMatrix[8,10] = 1

myMatrix[9,10] = 1
#'''
print myMatrix

myMatrix2 = np.dot(myMatrix,myMatrix)
myMatrix3 = np.dot(myMatrix, myMatrix2)
myMatrix4 = np.dot(myMatrix, myMatrix3)
myMatrix5 = np.dot(myMatrix, myMatrix4)
myMatrix6 = np.dot(myMatrix, myMatrix5)
myMatrix7 = np.dot(myMatrix, myMatrix6)

myExpandedMatrix = myMatrix + myMatrix2 + myMatrix3 + myMatrix4 + myMatrix5 + myMatrix6 + myMatrix7;

print myExpandedMatrix

myInverseExpMatrix = np.linalg.inv(myExpandedMatrix).astype(np.int)

print myInverseExpMatrix
'''
myInverseMatrix = np.linalg.inv(myMatrix).astype(np.int)
print "Current Matrix, 1 operation at a time:"
#print myMatrix
myString = "   "
for i in range(11):
	myString += string.lowercase[i] + " "
print myString
for i in range(len(myMatrix)):
	print string.lowercase[i], myMatrix[i]	

myString = "    "
for i in range(11):
	myString += string.lowercase[i] + "  "
print "Inverted Matrix, 1 operation at a time:"
#print myInverseMatrix
print myString
for i in range(len(myInverseMatrix)):
	print string.lowercase[i], myInverseMatrix[i], sum(abs(myInverseMatrix[i]))

'''	
