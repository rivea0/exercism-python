import math

class Clock:
    def __init__(self, hour, minute):
        self.hour = (math.floor(minute / 60) + hour) % 24 
        self.minute = minute % 60 

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        # Fill the zeroes if needed, so that it is in a readable format like '03:02'
        if len(str(self.hour)) == 1 and len(str(self.minute)) == 1:
            return f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}'         
        if len(str(self.hour)) == 1:
            return f'{str(self.hour).zfill(2)}:{self.minute}'
        if len(str(self.minute)) == 1:
            return f'{self.hour}:{str(self.minute).zfill(2)}'
        return f'{self.hour}:{self.minute}'

    def __eq__(self, other):
        return self.__str__() == other.__str__() 

    def __add__(self, minutes):
        self.hour = (math.floor(minutes / 60) + self.hour) % 24 
        self.minute += minutes % 60

        if self.minute >= 60:
            self.hour = (math.floor(self.minute / 60) + self.hour) % 24 
            self.minute %= 60

        return self.__str__()

    def __sub__(self, minutes):
        self.minute -= minutes
        
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
        while self.hour < 0:
            self.hour += 24

        return self.__str__()