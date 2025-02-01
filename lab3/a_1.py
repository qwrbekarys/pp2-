class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def increment_sec(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.increment_min()

    def increment_min(self):
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours = (self.hours + 1) % 24

    def decrement_sec(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.seconds = 59
            self.decrement_min()

    def decrement_min(self):
        self.minutes -= 1
        if self.minutes < 0:
            self.minutes = 59
            self.hours = (self.hours - 1) % 24


time = Time(11, 59, 59)
print(time) 

time.increment_sec()
print(time)

    