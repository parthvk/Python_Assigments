#Create the custom Python classes which have methods and attributes and implement single inheritance, multiple inheritance, and multilevel inheritance

# Single Inheritance
class Time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def displayMinute(self):
        print(f"{self.hours*60 + self.minutes} minutes")    

class Time2(Time):
    def __init__(self, hours, minutes):
        super().__init__( hours, minutes) 

    def displayHour(self):
        print(f"{self.hours} hours")

t1 = Time2(2, 50)
t1.displayHour()
t1.displayMinute()

# Multiple Inheritance
class Time3():
    def __init__(self, seconds):
        self.seconds = seconds 


class Time4(Time2, Time3):
    def __init__(self, hours, minutes, seconds):
        Time2.__init__(self, hours, minutes)
        Time3.__init__(self, seconds)

    def displaySeconds(self):
        print(f"{self.hours*3600 + self.minutes*60 + self.seconds} seconds")  

t1 = Time4(2, 50, 120)
t1.displayHour()
t1.displayMinute()
t1.displaySeconds()

# Multilevel Inheritance
class Time5(Time2):
    def __init__(self, hours, minutes, seconds):
        self.seconds = seconds
        super().__init__( hours, minutes)
    def displaySeconds(self):
        print(f"{self.hours*3600 + self.minutes*60 + self.seconds} seconds")

t1 = Time5(2, 50, 120)
t1.displayHour()
t1.displayMinute()
t1.displaySeconds()


