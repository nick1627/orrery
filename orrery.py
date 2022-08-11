"""
Code to obtain the position of solar system objects at a given time
"""

import numpy as np
import matplotlib as plt
import astropy as astr

class System:
    def __init__(allPlanets=True):
        self.allPlanets = False
        if allPlanets:
            self.allPlanets = True
        return
    
    def getBodyPosition(body, time):
        #return position of the body at the given time

    def getSystemPositions(time):

class Planet:
    def __init__(name, position):
        self.name = name
        self.position = position

    def 