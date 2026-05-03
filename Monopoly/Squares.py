#from Monopoly import Player

class Square:
    address = ''
    
    def __init__(self, ind = 0, address = "", priceProperty = 0, rent = 0):
        self.ind = ind
        self.address = address
        self.rent = rent
        self.priceProperty = priceProperty
        self.mortgaged = False
        self.owner = None
        
    def __str__(self):
        return(self.address)

    def getPrice(self):
        return self.priceProperty
        
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
    def __init__(self, ind = 0, address = '', rent = 0, price = [], priceProperty = 0, mortgage = 0):
        super().__init__(ind, address,priceProperty, rent)
        
        self.price = price
        self.mortgage = mortgage
        self.nbHouses = 0
        self.hasHotel = False
        
    def getnbHouses(self):
        return self.nbHouses
    
    def setOwner(p):
        pass
    
    def getRent(self):
        return self.rent

    def landedOn(self, loc):
        pass
      
    def payRent(p):
        if self.mortgaged:
            print()('    ** Mortgaged. No rent.')
            return
            
        r = getRent()
        owner.addCash(r)
        p.reduceCash(r)

    def addHouse(self):
        self.nbHouses += 1
#        self.rent += 100
        
class LotSquare(Square):
      def getRent(r):
          return index

class RRSquare(Square):
    def __init__(self, ind = 0, address = '', rent = 50):
        super().__init__(ind, address, 100, rent)
        
    def getRent(self):
        return 50 * self.owner.getRRCount()
       

class RailRoadSquare(Square):
#      owner = Player()
      def getRent(r):
          pass
#          c = owner.getRRCount()

class UtilitySquare(Square):
      def __init__(self, ind = 0, address = '', rent = 10):
          super().__init__(ind, address, 150, rent)
        
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

