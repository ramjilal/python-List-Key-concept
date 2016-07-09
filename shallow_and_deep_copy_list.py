#use python 2
#first simple copy of a list, List is mutable so it can be change by its copy.
x = [1,2,3]
y = x       # here list 'y' and list 'x' point to same content [1,2,3]. 
y[0]=5      # so whenever we will change list 'y' than list 'x' would be change.
print x    #print -> [5,2,3]
print y    #print -> [5,2,3]


#/**************************************************************\
#so to overcome this error we use SHALLOW copy.
#/**************************************************************\
#SHALLOW COPY of a LIST
from copy import *
x = [1,2,3]
y = copy(x)
y[0]=5
print x    #print -> [1,2,3]
print y    #print -> [5,2,3]


#/**************************************************************\
#but shallow copy also fail in deep copy of a list .let an example
#/**************************************************************\
from copy import *
x = [1,2,[3,4]]
y = copy(x)
y[0] = 12
y[2][0] = 5   # change value of first element of List [3,4]. 
print x       #print -> [1,2,[5,4]]
print y       #print -> [12,2,[5,4]]



#/**************************************************************\
#so to overcome this error we use DEEP copy.
#/**************************************************************\
from copy import *
x = [1,2,[3,4]]
y = deepcopy(x)
y[0] = 12
y[2][0] = 5   # change value of first element of List [3,4]. 
print x       #print -> [1,2,[3,4]]
print y       #print -> [12,2,[5,4]]
