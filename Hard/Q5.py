#5. Create a class 'Time' and initialize it with hours and minutes. Create a method addTime() which should take two Time objects and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min) Create another method displayTime() which should print the time. Also, create a method displayMinute() which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minutes.

class Time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, time1, time2):
        self.hours = time1.hours + time2.hours
        self.minutes = time1.minutes + time2.minutes
        if self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60
    
    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        print(f"{self.hours*60 + self.minutes} minutes")

t1 = Time(2, 50)
t2 = Time(1, 20)
t3 = Time(0, 0)
t3.addTime(t1, t2)
t3.displayTime()
t3.displayMinute()
