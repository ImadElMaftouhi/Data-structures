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


class Sll():
    
    list_size = 0 

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def sll_append(self, data):
        temp = Sll(data)
        ptr = self
        while ptr.next is not None: 
            ptr = ptr.next
        ptr.next = temp

        Sll.list_size+=1        

    def sll_prepend(self, data):
        temp = Sll(data)
        if self.next is None:
            temp.next = self
            Sll.list_size+=1        
            return temp
        temp.next = self
        Sll.list_size+=1        
        return temp


    def sll_print(self):
        ptr = self
        while ptr is not None:
            print("\n", ptr.data)
            ptr = ptr.next


    def sll_delete(self, rng):
        ptr = self
        if rng < 0 or rng >= Sll.list_size:
            return False
        for _ in range(rng - 1):
            ptr = ptr.next
        ptr.next = ptr.next.next
        #Deleting a node from our list has to do with python automatic garbage collector
        #See documentation for more.
       



head = Sll(0)
for i in range(1,10) :
    head.sll_append(i)


head.sll_delete(3)