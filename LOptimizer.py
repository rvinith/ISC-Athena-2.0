'''function finds best list of velocities for the race'''

import simulator as sim
import RaceParameters as rparam
import numpy as np
import itertools as iter

class LOptimizer:
    def __init__(self):
        self.bestVector = []
        self.bestTime = float("inf")
        self.maxSpeed = rparam.speedLimit

    def getBestVector(self, minVelocity, maxVelocity, resolution, increment):
        for sector in range(resolution):
            vector = self.makeVector(minVelocity, maxVelocity, sector, increment)
            time = self.getTime(vector)
            if time < self.bestTime:
                self.bestTime = time
                self.bestVector = vector
        
        return (self.bestVector, self.bestTime)
        
    '''gets rank of vector
    '''
    def getTime(self, vector):

        return 0

    'helper function makes vector with velocities for the race, and returned to getBestVector to be compared'
    'uses runSimulation'
    def makeVector(self, minVelocity, maxVelocity, numSectors, increment):
        badStarts = []
        choices = []
        result = []
        time = float("inf")
        speed = minVelocity
        while speed <= maxVelocity:
            choices.append(speed)
            speed += increment
        vectors = self.possibleCombos(choices, badStarts, numSectors)
        #find new way to compute all possibilities, s.t. list of bad vectors is taken 
        #into account while building vectors (save time and prevent building vectors we know won't work)
        for vector in vectors:
            if(sim.runSimulation(vector)):
                if self.getTime(vector) < time:
                    result = vector
        return result


    def possibleCombos(self, iterable, badStarts, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
        pool = tuple(iterable)
        n = len(pool)
        if not n and r:
            return
        indices = [0] * r
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != n - 1:
                    break
            else:
                return
            indices[i:] = [indices[i] + 1] * (r - i)
            yield tuple(pool[i] for i in indices)