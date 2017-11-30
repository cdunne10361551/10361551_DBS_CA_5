#Name: Connor Dunne
#Student Number: 10361551
#Calculator List Function
#This programme calls 10 object functions to calculate given list values

import math

class Calculator(object):
    
    #create a function to add values in a list
    def add(self, nums):
        number_types = (int, long, float, complex)
        checker = map(lambda x: isinstance(x,number_types),nums)
        if all(checker)==True:
            result = reduce(lambda x, y: x + y,nums)
            return result
        else:
            raise ValueError
    
    #create a function to subtract values within a list from each other
    def subtract(self, nums):
        number_types = (int, long, float, complex)
        checker = map(lambda x: isinstance(x,number_types),nums)
        if all(checker)==True:
            result = reduce(lambda x, y: x - y,nums)
            return result
        else:
            raise ValueError
     
    #create a function to multiply two given list values
    #how this works: multiply([a,b],[c,d])=[a*c, a*d, b*c, b*d]
    def multiply(self, ar, ab):
        number_types = (int, long, float, complex)
        checker1 = map(lambda x: isinstance(x,number_types),ar)
        checker2 = map(lambda x: isinstance(x,number_types),ab)
        if all(checker1) == True == all(checker2):
            result = []
            for i in range(len(ar)):
                df = map(lambda x:x*ar[i],ab)
                result = result + df
            return result
        else:
            raise ValueError
		
    #create a function to divide two given list values
    #how this works: divide([a,b],[c,d])=[a/c, a/d, b/c, b/d]
    def divide(self, ar, ab):
        number_types = (int, long, float, complex)
        checker1 = map(lambda x: isinstance(x,number_types),ar)
        checker2 = map(lambda x: isinstance(x,number_types),ab)
        if all(checker1) == True == all(checker2):
            try:
                result = []
                for i in range(len(ar)):
                    df = map(lambda x:ar[i]/x,ab)
                    result = result + df
                return result
            except ZeroDivisionError:
                print "Second input list cannot contain Zeros"
        else:
            raise ValueError
	
    #create a function to calculate the squre root of a given list value
    def squareroot(self, nums):
        number_types = (int, long, float, complex)
        checker = map(lambda x: isinstance(x,number_types),nums)
        if all(checker)==True:
            result = [math.sqrt(x) for x in nums]
            return result
        else:
            raise ValueError
			
   #create a function to calculate the sine of a given list value
    def sine(self, nums):
        number_types = (int, long, float, complex)
        checker = map(lambda x: isinstance(x,number_types),nums)
        if all(checker)==True:
            result = [math.sin(x) for x in nums]
            return result
        else:
            raise ValueError
		
    #create a function to calculate the cosine of a given list value
    def cosine(self, nums):
        number_types = (int, long, float, complex)
        checker = map(lambda x: isinstance(x,number_types),nums)
        if all(checker)==True:
            result = [math.cos(x) for x in nums]
            return result
        else:
            raise ValueError
		
    #create a function to calculate the tangent of a given list value
    def tangent(self, nums):
        number_types = (int, long, float, complex)
        checker = map(lambda x: isinstance(x,number_types),nums)
        if all(checker)==True:
            result = [math.tan(x) for x in nums]
            return result
        else:
            raise ValueError	
		
    #create a function to calculate the base-10 logarithm of a given list value
    def b10log(self, nums):
        number_types = (int, long, float, complex)
        checker = map(lambda x: isinstance(x,number_types),nums)
        if all(checker)==True:
            result = [math.log10(x) for x in nums]
            return result
        else:
            raise ValueError		
	
   #create a function to calculate the exponent of each value in list[x] given y
    def exponent(self, ar, ab):
        number_types = (int, long, float, complex)
        checker1 = map(lambda x: isinstance(x,number_types),ar)
        checker2 = isinstance(ab, number_types)
        if all(checker1) == True and checker2 == True:
            df = map(lambda x:x**ab,ar)
            return df
        else:
            raise ValueError