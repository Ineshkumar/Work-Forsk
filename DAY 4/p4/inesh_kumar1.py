# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:25:54 2018

@author: inesh
"""
    
def largest(x,y):
    if(x>y):
        return x
    else:
        return y    
        
def smallest(x,y):
    if(x<y):
        return x
    else:
        return y
    
x=list(input("enter the list :- "))    

print 'sum =',sum(x)
print 'multiply =',reduce(lambda x,y:x*y,x)
print 'largest =',reduce(largest,x)
print 'smallest =',reduce(smallest,x)
x.sort()
print 'sort =',x
print 'without Duplicates',set(x)



    
    

