'''
Developer: Adam Terwilliger
Purpose: MTH 496
Details: Senior thesis in Mathematicas at
			Grand Valley State University
'''
import matplotlib.pyplot as plt
# operations (1,1) or (1,-1) or (2,0)

# length 0 paths S(0) = 1
path1len0 = [(0,0)]
sPath1len0 = ''

# length 1 paths S(1) = 2
path1len1 = [(0,0), (1,1), (2,0)]
path2len1 = [(0,0), (2,0)]

sPath1len1 = 'UD'
sPath2len1 = 'S'

# length 2 paths S(2) = 6
path1len2 = [(0,0), (1,1), (2,2), (3,1), (4,0)]
path2len2 = [(0,0), (1,1), (2,0), (3,1), (4,0)]
path3len2 = [(0,0), (2,0), (3,1), (4,0)]
path4len2 = [(0,0), (1,1), (2,0), (4,0)]
path5len2 = [(0,0), (1,1), (3,1), (4,0)]
path6len2 = [(0,0), (2,0), (4,0)]

sPath1len2 = 'UUDD'
sPath2len2 = 'UDUD'
sPath3len2 = 'SUD'
sPath4len2 = 'UDS'
sPath5len2 = 'USD'
sPath6len2 = 'SS'

# length 3 paths S(3) = 22
path1len3 = [(0,0), (1,1), (2,2), (3,3), (4,2), (5,1), (6,0)]

path22len3 = [(0,0), (2,0), (4,0), (6,0)]

sPath1len3 = 'UUUDDD'

sPath1len3 = ''

exampleDyckPath = [(0,0),(1,1),(2,2),(3,3),(4,2),(5,3),(6,2),
					(7,1),(8,2),(9,1),(10,0),(11,1),(12,0)]

xs = [x[0] for x in exampleDyckPath]
ys = [x[1] for x in exampleDyckPath]

exampleSchPath = [(0,0),(1,1),(2,2),(3,3),(5,3),(6,2),
					(7,1),(9,1),(10,0),(11,1),(12,0)]
xs1 = [x[0] for x in exampleSchPath]
ys1 = [x[1] for x in exampleSchPath]


examplesSchPath = [(0,0),(1,1),(2,2),(4,2),(6,2),
					(7,1),(9,1),(10,0)]
xs2 = [x[0] for x in examplesSchPath]
ys2 = [x[1] for x in examplesSchPath]

examplelSchPath = [(0,0),(2,0),(3,1),(4,2),(6,2),
					(7,1),(8,0),(10,0)]
xs3 = [x[0] for x in examplelSchPath]
ys3 = [x[1] for x in examplelSchPath]


exampleRule1Path = [(0,0),(1,1),(3,1),(4,0),(5,1),(6,0)]
xsR1 = [x[0] for x in exampleRule1Path]
ysR1 = [x[1] for x in exampleRule1Path]

plt.scatter(xsR1,ysR1)
plt.plot(xsR1,ysR1)
plt.axis([-1,8,-1,8])
plt.axis('off')
plt.savefig("nonSym_path2.png", bbox_inches='tight')


'''
plt.scatter(xs,ys)
plt.plot(xs,ys)
plt.axis([-1,13,-1,13])
plt.axis('off')
plt.savefig("exampleDyck.png", bbox_inches='tight')
'''
'''
plt.scatter(xs1,ys1)
plt.plot(xs1,ys1)
plt.axis([-1,13,-1,13])
plt.axis('off')
plt.savefig("exampleSchroder.png", bbox_inches='tight')
'''

'''
plt.scatter(xs2,ys2)
plt.plot(xs2,ys2)
plt.axis([-1,11,-1,11])
plt.axis('off')
plt.savefig("exampleSmallSchroder.png", bbox_inches='tight')
'''
'''
plt.scatter(xs3,ys3)
plt.plot(xs3,ys3)
plt.axis([-1,11,-1,11])
plt.axis('off')
plt.savefig("exampleLargeSchroder.png", bbox_inches='tight')
'''
