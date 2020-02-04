#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This is Kerry Rainford's Week 1 Assignment Part 1"

def listDivide(numbers, divide=2):
    """Returns the number of elements in the numbers list that are divisible by divide.

Args:
    numbers (list): The first parameter
    divide (int): The second parameter. Defaults to 2.
    
    
Returns:
    Int: Returns an integer if successful; Returns an custom error from the ListDivideException class if False.
    >>> listDivide([1, 2, 3, 4, 5])
    '2'
    
    >>> listDivide([2, 4, 6, 8, 10])
    '5'
    
    >>> listDivide([30, 54, 63, 98, 100], divide=10)
    '2'
    
    >>> listDivide([])
    '0'
    
    >>> listDivide([1,2,3,4,5], 1)
    '5'
    """
    counter = 0
    for x in range(0, len(numbers)):
        if numbers[x] % divide == 0:
            counter += 1  
    return(counter)


class ListDivideException(Exception):
    pass


def testListDivide(): 
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException('There is a problem with listDivide Test 1')
    if listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException('There is a problem with listDivide Test 2')
    if listDivide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException('There is a problem with listDivide Test 3')
    if listDivide([]) != 0:
        raise ListDivideException('There is a problem with listDivide Test 4')
    if listDivide([1,2,3,4,5], 1) != 5:
        raise ListDivideException('There is a problem with listDivide Test 5')
        
testListDivide()

