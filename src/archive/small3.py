import numpy as np
import string

myMatrix = np.zeros([3,3], dtype=np.int)
#'''

myMatrix[0,1] = 1
myMatrix[1,2] = 1

# length 1 paths
#print myMatrix

# length two paths
myMatrix2 = np.dot(myMatrix,myMatrix)
print myMatrix + myMatrix2


iden = np.eye(3, dtype=int)

iden_x = iden - myMatrix

myInverseMatrix = np.linalg.inv(iden_x).astype(np.int)

print myInverseMatrix
'''
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
