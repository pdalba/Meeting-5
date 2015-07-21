import abc   #forces users to implement things like you want them to be

class Animal(metaclass = abc.ABCMeta):   #standard syntax for abstract classes
#you cannot just make an animal class - there is no implementation - it can only be made in
# classes below (not from command line)
    @abc.abstractmethod
    def makeNoise(self):
        print('This animal says ', end = '')
        #pass

    @abc.abstractproperty
    def color(self):
        pass

class Cow(Animal):

#you can make a cow by c = Cow() but you cannot make a = Animals() this is abstract
#cow has to implement ALL abstract methods 

    def makeNoise(self):
        print('MOO')

    @property
    def color(self):
        return 'Black and White'

class Duck(Animal):

    def quack(self):    #this will break since I do not have def makeNoise...
    #def makeNoise(self):
        #super().makeNoise()   #if you put in super, then it will actually call the "this animal
        # says from the superclass above. otherwise it will just return QUACK
        
        print('QUACK')

    @property
    def color(self):
        return 'Brown'
