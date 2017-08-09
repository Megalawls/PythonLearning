import math

class Paint ():
    def __init__ (self, name, litresCan, priceCan, coveragePerLitre):
        self.name = name
        self.litresCan = litresCan
        self.priceCan = priceCan
        self.coveragePerLitre = coveragePerLitre

    def getCoveragePerCan (self):
        return self.coveragePerLitre * self.litresCan

    def pricePerRoom(self, input):

        def cansPerRoom (self, surfaceArea):
            return math.ceil(surfaceArea/self.getCoveragePerCan())

        print("A room of "+str(input)+"m2 will require "+
        str(cansPerRoom(self, input))+" cans, and cost "+
        str(cansPerRoom(self, input)*self.priceCan))
        print(str((math.ceil(input/self.getCoveragePerCan()))-
        (input/self.getCoveragePerCan()))+
        " cans of Paint will be wasted")
        return cansPerRoom(self, input)*self.priceCan



cheapoMax = Paint("cheapoMax", 20, 19.99, 10)
averageJoes = Paint("averageJoes", 15, 17.99, 11)
duluxuriousPaints = Paint("duluxuriousPaints", 10, 25.00, 20)

print(cheapoMax.pricePerRoom(300))
print(averageJoes.pricePerRoom(300))
print(duluxuriousPaints.pricePerRoom(300))
