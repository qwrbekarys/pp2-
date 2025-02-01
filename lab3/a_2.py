class Time:
    def __init__(self, hour = 0, min = 0, sec = 0):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __str__(self):
        s = ""
        if self.hour<10:
            s+="0" + str(self.hour)
        else:
            s+=str(self.hour)

        s+=":"

        if self.min<10:
            s+="0" + str(self.min)
        else:
            s+=str(self.min)

        s+=":"

        if self.sec<10:
            s+="0" + str(self.sec)
        else:
            s+=str(self.sec)

        return s

    def  inc_sec(self):
        add_time = self.sec + 60* self.min + 60*60*self.hour

        add_time += 1

        self.hour = add_time//3600
        self.min = add_time % 3600 // 60
        self.sec = add_time % 60
        