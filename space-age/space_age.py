'''
Alternatively, it could be written like this one below, 
but the tests require each calculation to be a separate function, 
so the real solution has a bit of duplicity.

class SpaceAge:

    EARTH_YEARS = {
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'earth': 1.0,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132 
    }

    SECONDS_IN_A_YEAR = 31557600

    def __init__(self, seconds, planet):
        self.seconds = seconds
        self.planet = planet
        
    def calculate_age(self):    
        age = self.seconds / (SpaceAge.EARTH_YEARS[self.planet.lower()] * SpaceAge.SECONDS_IN_A_YEAR)   
        return round(age, 2)

'''

class SpaceAge:

    EARTH_YEARS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132 
    }

    SECONDS_IN_A_YEAR = 31557600

    def __init__(self, seconds):
        self.seconds = seconds        

    def on_mercury(self):
        return round(self.seconds / (SpaceAge.EARTH_YEARS['mercury'] * SpaceAge.SECONDS_IN_A_YEAR), 2)

    def on_venus(self):
        return round(self.seconds / (SpaceAge.EARTH_YEARS['venus'] * SpaceAge.SECONDS_IN_A_YEAR), 2)

    def on_earth(self):
        return round(self.seconds / (SpaceAge.EARTH_YEARS['earth'] * SpaceAge.SECONDS_IN_A_YEAR), 2)

    def on_mars(self):
        return round(self.seconds / (SpaceAge.EARTH_YEARS['mars'] * SpaceAge.SECONDS_IN_A_YEAR), 2)

    def on_jupiter(self):
        return round(self.seconds / (SpaceAge.EARTH_YEARS['jupiter'] * SpaceAge.SECONDS_IN_A_YEAR), 2)

    def on_saturn(self):
        return round(self.seconds / (SpaceAge.EARTH_YEARS['saturn'] * SpaceAge.SECONDS_IN_A_YEAR), 2)

    def on_uranus(self):
        return round(self.seconds / (SpaceAge.EARTH_YEARS['uranus'] * SpaceAge.SECONDS_IN_A_YEAR), 2)
    
    def on_neptune(self):
        return round(self.seconds / (SpaceAge.EARTH_YEARS['neptune'] * SpaceAge.SECONDS_IN_A_YEAR), 2)
