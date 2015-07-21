from enum import Enum   #will not work in python 2

#allows for keyword-value pairs - kinda like a dictionary except now you can associate a
# single keyword with multiple values

#now Planet.MERCURY will return all the info for mercury
class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)   #each of these are a "member" of the enumeration
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27,   7.1492e7)
    SATURN  = (5.688e+26, 6.0268e7)
    URANUS  = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)
    
    #must have a constructor so python knows how to handle the two input values
    def __init__(self, mass, radius):
        self.mass = mass       # in kilograms
        self.radius = radius   # in meters
    
    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)
