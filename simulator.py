'''is used by the optimizer to simulate the race
'''

import car
import enviornment

class Simulator:

    ''' Initializes a simulation with race properties
    '''
    def __init__(self, route, startTime):
        
        # create car and enviornemnt objects
        
        self.car = car.Car()
        self.enviornment = enviornment.Enviornment()


    ''' runs the simulation for one velocity over a period
    '''
    def stepSimulation(self, velocity, resolution, setpLength):

        # get enviornment
        # update car
        # update enviornemnt
        pass