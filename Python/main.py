# All data structure possible using Python 3.12

"""
Tuple : A tuple is a python's data structure in the form of an array, the elements are not not mutable (inchangeable). A tuple can hold various variable/constants of different type.
"""
var = (1,2,3,4,"string",56.34, True) # Same as writing var = () or var = tuple ()


"""
List : A list is a data strucutre that can hold different data types but are listed in order. The strucutre allows data manipulation
"""

var = [1,2,3,4,5,6,7,8,9,True, False, 45.3, 12.02] # Same as writing var = [] or var = list()


"""
Multidimensionnal list :
"""
var = [ [1,2], [3,4], [[5,6],[7,8]] ]


##linked list 

#Dont forget to import the necessary libraries to access the functions
import Dll as dll
import Sll as sll

dllist = dll.Dll()
sllist = sll.Sll()

for i in range(5) :
    dllist.dll_append(i)

for i in range(5):
    sllist.sll_append(i)

sllist.sll_print()
dllist.dll_print()

