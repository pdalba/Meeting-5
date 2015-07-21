import numpy as np
from time import time

class Vector(object):

    __vectorID = 1     #class variable - will be unique for each vector object created

    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
            self._id = None
            self.__setID(Vector.__vectorID)
        elif len(args) == 2:
            if isinstance(args[0],(int,float)) and isinstance(args[1],(int,float)):
                self.x = args[0]
                self.y = args[1]
                self._id = None
                self.__setID(Vector.__vectorID);
            else:
                errorStr = 'Input values were not valid numbers'
                raise TypeError(errorStr)                   
	#these are just a subset of magic methods (can look up others) all magic methods have
	# __ on either side
	#now you can define what it means to add two of these ojects
	
	#this magic method (str) prints out strings of all info (as you chose to return)
	#otherwise print(vec) would return nothing helpful - now pring(vec) prints out useful
	#infor
    def __str__(self):
        return 'ID: '+str(self.id)+'\tCoordinate Values: '+'('+str(self.x)+', '+str(self.y)+')'

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector):
        return Vector(self.x * vector.x, self.y * vector.y)

    def dot(self, vector):
        return self.x*vector.x + self.y*vector.y

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        pass
    
    def __setID(self, value):    #will assign the object the current id and then increment up the id number
        self._id = value
        Vector.__vectorID += 1

    @staticmethod  #static to the class - not going to change with each instance. each 
    # instance will know about this even if this is changed after the instance is created
    def getNextValidID():
        return Vector.__vectorID
