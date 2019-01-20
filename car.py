'''Models the car
'''

class Car:
    def __init__(self,

        #constant paremeters
        mass,
        regen_efficiency,
        power_inefficiency,
        battery_max_charge,
        cd,
        Crr,
        frontal_area,
        panel_area,
        solarcell_base_efficiency,
        panel_tilt,
        azimuth_angle,
        
        #initial states
        battery_charge,
        pack_voltage = 28 * 3.5,
        battery_temperature = 25, 
		panel_temperature = 25):

        #initialize parameters
        self.mass = mass
        self.regen_efficiency = regen_efficiency
        self.power_inefficiency = power_inefficiency
        self.battery_max_charge = battery_max_charge
        self.cd = cd
        self.Crr = Crr
        self.frontal_area = frontal_area
        self.panel_area = panel_area
        self.solarcell_base_efficiency = solarcell_base_efficiency
        self.panel_tilt = panel_tilt
        self.azimuth_angle = azimuth_angle

        #initialize states
        self.battery_charge = battery_charge
        self.pack_voltage = pack_voltage
        self.battery_temperature = battery_temperature 
        self.panel_temperature = panel_temperature



    
    def updateCar(self):
        pass