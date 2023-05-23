class person:

    def __init__(self, budget):
        self.budget = budget

    def makan(self, iterasi):
        if self.budget >= 0:
            self.budget += iterasi*15000
    
    def getMakan(self):
        return "Hari ini kamu telah mengeluarkan uang sebesar " + str(self.budget)
    
Nasi_Lauk = person(0)

Nasi_Lauk.makan(6)
print(Nasi_Lauk.getMakan())
