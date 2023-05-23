class Handpone:
    
    def __init__(self, power):
        self.power = power

    def play_game(self, duration):
        if self.power > 0:
            self.power -= (duration * 5)
            if self.power <= 0:
                self.power = 0

    def call(self, duration):
        if self.power > 0:
            self.power -= duration
            if self.power <= 0:
                self.power = 0

    def sms(self, length):
        if self.power > 0:
            self.power -= (length//100)
            if self.power <= 0: 
                self.power = 0

    def charge(self, duration):
        if self.power < 100:
            self.power += (duration*2)
            if self.power >= 100:
                self.power = 100
    
    def getPower(self):
        if self.power > 0:
            return 'baterai anda tersisa: ' + str(self.power) + '%'
        else:
            return 'baterai anda habis, segera charge atau beli lagi!'

# Instantiate dengan kondisi baterai 0%    
xiaomi = Handpone(0)

#Charge 2 jam
xiaomi.charge(120)
print(xiaomi.getPower())

# call 30 minute
xiaomi.call(30)
print(xiaomi.getPower())

# sms 1000 chars
xiaomi.sms(1000)
print(xiaomi.getPower())

# charge 30 minute
xiaomi.charge(30)
print(xiaomi.getPower())

# play game 30 minute
xiaomi.play_game(30)
print(xiaomi.getPower())