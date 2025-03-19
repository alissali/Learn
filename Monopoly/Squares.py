#from Monopoly import Player

class Square:
    address = ''
    
    def __init__(self, address = "", rent = 0):
        self.address = address
        self.rent = rent
        self.owner = None
        
    def __str__(self):
        return(self.address)

    def getPrice(self):
        return 200
        
    def landedOn(self, loc):
        pass
    
    def setRent(self, r):
        self.rent = r
    
    def getRent(self):
        return self.rent

    def canPurchase(self):
        return self.owner == None
        
class RegularSquare(Square):
    def landedOn():
        pass
      
class GoSquare():
    def __init__(self, title):
        self.title = title
        
    def __str__(self):
        return(self.title)

        
    def landedOn():
        pass
      
class InComeTaxSquare(Square):
    def landedOn():
        pass
    
class PropertySquare(Square):
    def __init__(self, address = '', rent = 0, price = 0, priceProperty = 0, mortgage = 0):
        super().__init__(address, rent)
        
        self.price = price
        self.priceProperty = priceProperty
        self.mortgage = mortgage
        self.nbHouses = 0
        
    def getnbHouses(self):
        return self.nbHouses
    
    def setOwner(p):
        pass
    
    def landedOn(self, loc):
        pass
      
    def payRent(p):
        r = getRent()
        owner.addCash(r)
        p.reduceCash(r)

    def addHouse(self):
        self.nbHouses += 1
        self.rent += 100
        
class LotSquare(Square):
      def getRent(r):
          return index

class RRSquare(Square):
    def __init__(self, address = '', rent = 50):
        super().__init__(address, rent)


class RailRoadSquare(Square):
#      owner = Player()
      def getRent(r):
          pass
#          c = owner.getRRCount()

class UtilitySquare(Square):
      def __init__(self, address = '', rent = 10):
          super().__init__(address, rent)
        
      def getRent(self, r):
          return self.rent * r
          
class CardSquare():

    def __str__(self):
        return('Card')



class ChanceSquare(CardSquare):
    
    def __str__(self):
        return('Chance')

class CCSquare(CardSquare):
    def __str__(self):
        return('Community Chest')

