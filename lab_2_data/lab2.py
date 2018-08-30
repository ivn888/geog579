import math 

#track!D and percantage 

track1=0.10  
track2=0.15
track3=0.14
track4=0.09
track5=0.12
track6=0.06


#print track4

'''
n: number of objects in the sample
i j: pairing of object i and object j 
Zi: the attribute value for object i
Zj:	the attribute value for object j
cij:	the similarity between the attribute value of object i and that of object j

Wij: the spatial adjacency between object i and object j, Wii = 0 for all i
'''


#computation for Geary's C 

#sum of all attributes of these units
zi = track1+track2+track3+track4+track5+track6

#six comes from the total number of objects
zmean = (zi/6)

print zmean

def equation1(zi,zj):
	cij = (zi - zj)**2
	return cij 


obj1= equation1(track1,track1)
obj2= equation1(track1,track2)
obj3= equation1(track1,track3)
obj4= equation1(track1,track4)
obj5= equation1(track1,track5)
obj6= equation1(track1,track6)


print obj1,obj2,obj3,obj4,obj5,obj6


print (track2-track3)**2