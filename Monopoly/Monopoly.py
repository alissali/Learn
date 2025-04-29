'''          
  My Monopoly
  TODO: test (Continuous)
  TODO: Player knows game (players out of game?)
  TODO: exchangeProprty UnitOfWork (technical feature)
  TODO: payPlayer(), listOtherProperties, Property exchange (Done),
        CC card, buyHotel (menu and attemptPurchase option), Parking,
        attemptPurchase option:use sellHouses and mortgage if not enough cash
        mortgage (Done)
          TODO: mortgage value from DB
        Adresses in Cards (+mySql -- Done)
        Property price
        rent in DB and initialisation : (Done after infinite parties.)
        Player.attemptPurchase : replace insert + sort with insertInSorted
        Use Square.ind instead of board.index()
        List Collection
        Register Playersc
        Defensive Programming:
        Collection methods
            colorname = game.board.color[game.board.collections.index(game.players[game.currentPlayer].getCollection(s, game.board))]
        payRent --- feature: payOwner(allIveGot) when defect (Done)
        tax square
        check mortgage amounts (Done ; double addition)
        buyHouses(): 2 by default
        addHouse() and rent
        priceHotel instead of price[4] (mini-feature)
        
        quit() after:
        (Card)
        ...
          ** Not enough cash [TODO]
    reduceCash 50
    
Cash = -75

        U.I. After attemptPurchase propose menu() (micro-feature)
        also after : (Extension)
          *** I have no more money!!!
          and:
            quitting jail
          and:
            passing departure
  * I have no houses to sell, trying mortgage
    Paying rent: 615
    reduceCash 615
    and:
 ** Three turns in jail
    Forced out of Jail, Out-of-jail card used!
    also after:
      ** Got whole collection
      Buy houses ? y
    reduceCash 50
  *** Bought a house on C/ Moralzarzal!
  Buy another? n

    
    U.I.    Using out-of-jail card : not auto

        sell and/or exchange out-of-jail card (mini-feature)
        Operation -mini-feature)
        None  Square 36 : Spinnaker Dr. New Haven (F_White)
        
   U.I. feature (Urgent): adapt principal menu(player | player.properties)
   
  Can purchase
    Purchase 300
  ** Not enough cash for purchase!
Cash = 10

          Chance card: Make general repairs on all your property. For each house pay $For each hotel pay $100.
    reduceCash 600
Cash = -55
    also ib buyHouses()
        BUG:
line 727, in menu
    p.buyHouse(game.board, game.board.squares[i])
    refactored: buyHouses()
IndexError: list index out of range

micro-feauture: buyHouse : check

        Parking -- Go, see: /home/allocation/Dev/Monopoly-game-master/images/go.png
        (Done) Nothing to do according to standard rules

mini-feature: (Done: no more occurences)
       *** Sold for 99. (Priority : U)
       
       BUG: double addition mortgage amount (Done)
       
       BUG:
602, in playCard
    square = m.board.squares[self.piece.loc]
IndexError: pop from empty list
       BUG: (Solved Tue Mar 25 17:13:46 CET 2025 @717 /Internet Time/)
341, in printProperties
    print(f'    Property[{board.squares.index(p)}]: {p}')
246, in cmpHouses
    elif ind1 < ind2:
AttributeError: 'UtilitySquare' object has no attribute 'getnbHouses'

TODO: code smell:
unmortgageProperty(self):
        self.mortgagedList = ...
        
      BUG: (Solved)
  Chance card: Go Back 3 Spaces.
Cash = 1075
  Not executed.
  also:
Chance card: Advance to Athinon Str. Rhodes. If you pass Go, collect $200.

      BUG (Scenario):
    Roll : 3
    Roll : 3
    Forced out of Jail, fine paid!
      lines 306-321 : test dice first then nbTurnsInJail
    Roll : 4
    Roll : 4
    Forced out of Jail, fine paid!
      with freeCard
   
      BUG exchangeProperty:
    ** Cash = -30 (cf. payPlayer)
    
    BUG: RR (200 for others)
  rent = 150
  
  mini-feature (auto -- buyHotel -- It. 2)
    *** Bought a house on Mazzeh Villat!
  Buy another? n


macro-feature:  
** Cash = -45

  BUG: not ownCollection
  rent = 25
    ** Doubling rent
    Paying rent: 50
    
  BUG: (nothing is done)
  You chose:  C
Cash = 355
   
    BUG: playSquare after:
   Chance card: Go Back 3 Spaces.
Cash = 34

    BUG: can't unmorgage, property in list ind 0 and item at ind 0 is another property
    Houses: 0. Rent: 70 (F_Blue)
    *** Mortgaged

    ind: 1
 *** Strong St. San Rafael is not mortgaged
 
    BUG:
None    Property[32]: Furth Circle Burlingame
      Houses: 3. Rent: 1845 (F_Cyan)

None    Property[33]: Linden Road Sandown Singapore
      Houses: 3. Rent: 1450 (F_Cyan)

    BUG:
    ** Unmortgaged Erling Skakkes gate Stavern

  ** Cash = -90

    also pay fine (check amount)
    BUG: Should invoke canPurchase()
None  Square 8 : Water Company
{Color.F_Green}    ** Mortgaged, no rent.{Color.F_White}

    BUG:
  * Property to exchange : 32
  * Against : 18
Traceback (most recent call last):
...
ValueError: list.remove(x): x not in list

    BUG: playSquare should be called

  Chance card: Go Back 3 Spaces.
 Landed on rue du Commerce
 
    U.I. mortgage()
    BUG: readjust rent when houses sold (Urgent)
        Checked: code seems OK
      Houses: 0. Rent: 2350

None    Property[14]: Lyonerstr. Frankfurt
      Houses: 4. Rent: 1445 (F_Green)

None    Property[21]: Berguvsvägen  Luleå
      Houses: 4. Rent: 2265 (F_Blue)
        
        BUG:
  *** Sold for 175.
      Doing mortgage
    Paying rent: 1080
    reduceCash 1080
Cash = 860
      
      BUG:
  rent = 100
  *** I have no more money!!!
  ** Selling houses
        Sold Furth Circle Burlingame (100/285)
        Sold Linden Road Sandown Singapore (200/285)
        Sold Brehmen St. Bergen (300/285)
  *** Sold for 300.
    Paying rent: 100
      BUG: after bad exchange (Solved: pythonic exchange code)
None    Property[6]: St Kilda Road Melbourne
      Houses: 0. Rent: 20 (F_Red)
    Property[8]: Water Company
    Property[8]: Water Company
    and:
None    Property[21]: Berguvsvägen  Luleå
      Houses: 0. Rent: 165 (F_Blue)

None    Property[21]: Berguvsvägen  Luleå
      Houses: 0. Rent: 165 (F_Blue)

    BUG: after attemptPurchase.ownCollection -- buyHouses then exit
Done:
  Fri Apr 25 00:24:01 CEST 2025 @975 /Internet Time/:
    Hotels: simple solution, requires refactoring of original code
'''

from Squares import *
from Cards import *
from mmysql import get_squares, get_chanceCards, wait_for_mysql_to_come_up
from Color import Color

import random
from functools import cmp_to_key
import os

from flask import Flask, render_template, request, session, url_for, redirect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import text

import colorama
from colorama import Fore, Style

import functools


class Die:
    faceValue = 6
    
    def roll(self):
        self.r = round((random.random()*5) + 1)
        print (f'    Roll : {self.r}')
        return(self.r)

class Cup:
    '''
        Singleton
    '''
    dice = [Die for d in range(2)]
         
    def roll(self):
        self.r1 = self.dice[0].roll(self.dice[0])
        self.r2 = self.dice[1].roll(self.dice[1])

        return self.r1 + self.r2
    
    def double(self):
        return (self.r1 == self.r2)
        
    def getTotal():
        return tot * 4
        
def get_mysql_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 3306 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "Allocation_123")
    user, db_name ="allocation", "monopoly" 
    return f"mysql://{user}:{password}@{host}:{port}/{db_name}"
  
        
def _get_squares(squares):
     get_session = sessionmaker(bind=create_engine(get_mysql_uri()))
     session = get_session()
     squares = get_squares(session, squares)
#     for s in squares:
#         print(f's.address  = {s.address}')
     return squares
 
def _get_chanceCards(chanceCards):
     get_session = sessionmaker(bind=create_engine(get_mysql_uri()))
     session = get_session()
     chanceCards = get_chanceCards(session, chanceCards)
#     for s in squares:
#         print(f's.address  = {s.address}')
     return chanceCards
 
class Collection:

    def __init__(self):
        self.color = ''
        self.properties = [PropertySquare]
    
class Board:
    '''
        Singleton
    '''    
    def build(self):
        print('build')
        
        self.squares[5]  = RRSquare(5, 'Mahattet Elhijaz', 50)
        self.squares[15] = RRSquare(15, 'NY RRS', 50)
        self.squares[25] = RRSquare(25, 'Gare du Nord', 50)
        self.squares[35] = RRSquare(35, 'Trafelgar RRS', 50)
        
        self.squares[8]  = UtilitySquare(8, 'Water Company')        
        self.squares[31] = UtilitySquare(3, 'Electricity Company')
        
        self.squares[2]  = ChanceSquare()        
        self.squares[16] = ChanceSquare()        
        self.squares[27] = ChanceSquare()        

        self.squares[13] = CCSquare()        
        self.squares[22] = CCSquare()        
        self.squares[37] = CCSquare()        

        self.squares[0]  = GoSquare('Departure')  
        self.squares[10] = GoSquare('Go to jail')  
        self.squares[20] = GoSquare('Parking')  
        self.squares[30] = GoSquare('Jail')


        self.squares = _get_squares(self.squares)

        self.color = ['F_LightRed', 'F_Red', 'F_Green', 'F_Yellow', 'F_Blue', 'F_Magenta', 'F_Cyan', 'F_White']
        
        k = 0
        for i in range(0, 8):
            self.collections[i].color = self.color[i]
            l = 0
            for j in range(0, 3):
                while not isinstance(self.squares[k], PropertySquare):
                    k += 1
                print(f'k = {k}')
                self.collections[i].properties.insert(l, self.squares[k])
                k += 1
                l += 1

        for i in range(0, 8):
            print(f'color = {self.collections[i].color}')
            for j in range(0, 3):
                print(f'p = {self.collections[i].properties[j].address}')
        
    def void():
        pass
        
    def __init__(self):
        self.squares = [Square() for s in range(40) ]
#        self._init_from_file(self.squares)
        
        self.collections = [Collection() for i in range(8)]
        self.usedChanceCards = []
        
        self.build()
        
        self.chanceCards = [ChanceCard('', self.void) for c in range(15) ]
        self.chanceCards = _get_chanceCards(self.chanceCards)
        
        random.shuffle(self.chanceCards)
        
        for c in self.chanceCards:
            print(c.content)
        
   
    def _read_next(self):
        yield 0
    
    def _init_from_file(self, squares):
        return [s for s in self._read_next()]
        
    def getSquare(self, loc, fvTot):
        return self.squares[loc]
        
    def listProperties(self, player):
        print(' *** Properties')
        i = 0
        for s in self.squares:
            if isinstance(s, PropertySquare):
                colorname = self.color[self.collections.index(player.getCollection(s, self))]
                color = Color.getColor(colorname)
            else:
                color = Color.getColor('F_LightBlue')
            print(f'{color}Square[{i}]: {s}')
            if isinstance(s, Square):
                if s.owner:
                    print(f'{Color.F_LightYellow} --- ({s.owner.name}){Color.F_White}')
                     
            i += 1
        
class Piece:
    def __init__(self):
        self.loc = 0
   
    def isOn(s: Square):
        pass
        
class MonopolyGame:
    def __init__(self):

        print('Creating MonopolyGame')
        self.board = Board()
        self.cup = Cup()
        self.players = []
        self.players.append(Player('Hassan', 1500))
        self.players.append(Player('Mamoun', 1500, True))
        self.players.append(Player('Rima', 1500))
        self.players.append(Player('Saleem', 1500))
        self.playerCount = 4
        self.currentPlayer = 0
       
        self.positions = [0 for p in self.players]

    def nextPlayer(self):
        self.currentPlayer = (self.currentPlayer + 1) % self.playerCount
        return self.players[self.currentPlayer]
        
    def PlayedWith(d: Die):
        pass
    
    def getPosition(self, i):
        return self.positions[i]
    
    
    def advance(self, p, loc, distance):
        if p.piece.loc + distance >= 40:
            print('  Passing departure')
            p.addCash(200)
        p.piece.loc = (p.piece.loc + distance) % 40

        return p.piece.loc
             
    def quit(self, p):
        p.sellAll()
        for prop in p.properties:
            if prop.mortgaged: prop.mortgaged = False
        self.players.remove(p)
        self.playerCount -= 1

def cmpProperties(p1, p2):
    ind1 = p1.ind
    ind2 = p2.ind
    
    if ind1 > ind2:
      return 1
    elif ind1 < ind2:
      return -1
    return 0
    
def cmpHouses(p1, p2):
# BUG Solution:
#    if not (isinstance(p1, PropertySquare) and isinstance(p2, PropertySquare)):
    try:
        nh1 = p1.getnbHouses()
        nh2 = p2.getnbHouses()
        if nh1 > nh2:
          return 1
        elif nh1 < nh2:
          return -1
        return 0
    except AttributeError:  
        if isinstance(p1, PropertySquare): return 1
        else: return -1
      
class Player:
    def __init__(self, name = '', cash = 0, isHuman = False):
        self.name = name
        self.cash = cash
        self.human = isHuman

        self.RRCount = 0
        
        self.nbDoubles = 0
        self.freeCard = False
        self.inJail = False
        self.nbTurnsInJail = 0
        self.piece = Piece()
        self.properties = []

        
    def plays(m: MonopolyGame):
        pass               
    
    def takeTurn(self, m, dv):
        '''
        loc par bricolage obligé, le suivant ne pasee pas.
#        nonlocal cup
#        nonlocal loc
      '''
        self.answer = 'y'
        if self.inJail:
            if m.cup.double():
                self.inJail = False
                self.nbTurnsInJail = 0
                print('    Double! Got out of Jail')
                return dv
            elif self.freeCard and self.nbTurnsInJail != 3:
                if self.human:
                    self.answer = input('Use out-of-jail card ? ')
                    if self.answer.lower() == 'n':
                        self.nbTurnsInJail += 1
                        return 0
                print('    Using out-of-jail card')
                self.freeCard = False
                self.inJail = False
                self.nbTurnsInJail = 0
                return dv
            elif self.nbTurnsInJail == 3:
               print(' ** Three turns in jail')
               self.nbTurnsInJail = 0
               if self.freeCard:
                   self.freeCard = False
                   print('    Forced out of Jail, Out-of-jail card used!')
               else:
                   print('    Forced out of Jail, fine paid!')
                   self.reduceCash(50)
               self.inJail = False
               return dv
            else:
                self.answer = input('Pay fine ? ')
                if self.answer.lower() == 'y':
                    self.reduceCash(50)
                    self.nbTurnsInJail = 0
                    self.inJail = False
                    return dv                        
                else:
                    self.nbTurnsInJail += 1
                    print('Still in jail!')
                    return 0
        else:
            if m.cup.double():
                if self.nbDoubles == 3:
                    print('  Third consecutive double, goto Jail!')
                    self.inJail = True
                    self.piece.loc = 30
                    self.nbDoubles = 0
                    return 0
            else:
                self.nbDoubles = 0
          
                return dv
    #        location.landedOn(loc)
#        self.nbTurnsInJail += 1
        
        return dv

    @staticmethod
    def wrapper(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            if self.cash < args[0]:
                # getCash()
                print("  ** Not enough cash [TODO]")
            return func(self, *args, **kwargs)
        return wrap

    @wrapper
    def reduceCash(self, pr):
        print(f'    reduceCash {pr}')
        self.cash -= pr
        
#    wrapper = staticmethod(wrapper)

    def printProperties(self, board):
        for p in self.properties:
            if not isinstance(p, PropertySquare):                
                print(f'{Color.F_LightBlue}    Property[{board.squares.index(p)}]: {p}')
            else:
                colorname = board.color[board.collections.index(self.getCollection(p, board))]
                color = Color.getColor(colorname)
                print(f'{color}    Property[{board.squares.index(p)}]: {p}')

                print(f'     {Color.B_LightGray}{Color.F_Black} Houses: {p.nbHouses}.{Color.B_Default}{Color.F_Default} Rent: {p.rent} ({getColor(p, board.collections)})')
            if p.mortgaged:
                print(f'{Color.F_Red}    *** Mortgaged')
                
        try:        
            print(f'  *** max: {max(self.properties, key=cmp_to_key(cmpHouses))}\n')
        except ValueError:
            print(f'    {Color.B_Yellow}**** You have no property!{Color.B_Default}')

    def haveHouses(self):
        for p in self.properties:
            if isinstance(p, PropertySquare) and p.nbHouses != 0:
                return True
        return False
        
    def haveHotels(self):
        for p in self.properties:
            if isinstance(p, PropertySquare) and p.hasHotel:
                return True
        return False
        
    def sellHotels(self, missedAmount):
        print('  ** Selling hotels')
        props = [p for p in self.properties if isinstance(p, PropertySquare) and p.hasHotel]
        saleAmount = 0
        if props:
            i = 0
            for p in props:
                p.setRent(p.getRent() - 100)
                p.hasHotel = False
                p.nbHouses = 4
                saleAmount = int(p.price[4]/2)
                if saleAmount > missedAmount:
                    return saleAmount
                    
        return saleAmount
    
       
    def sellHouses(self, missedAmount):
        print('  ** Selling houses')
        props = [p for p in self.properties if isinstance(p, PropertySquare)]
        if props:
            props.sort(key=cmp_to_key(cmpHouses), reverse=True)
            i = 0
            saleAmount = 0
            while self.haveHouses() and saleAmount < missedAmount and i < len(props):
                if props[i].nbHouses > 0:
                    p = props[i]
                    saleAmount += int(p.price[p.nbHouses - 1] / 2)
                    p.nbHouses -= 1
                    p.setRent(p.getRent() - 50)
                    print(f'        Sold {p} ({saleAmount}/{missedAmount})')
                i += 1
                if i == len(props):
                    i = 0
            print(f'  *** Sold for {saleAmount}.')
        
            return saleAmount
        else:
            return 0
    
    def doMortgage(self, missedAmount):
        collected = 0
        for p in self.properties:
            if collected < missedAmount and not p.mortgaged:
                collected += int(p.priceProperty / 2)
                p.mortgaged = True
                    
        return collected

    def unmortgageProperty(self):
        self.mortgagedList = [p for p in self.properties if p.mortgaged]
        i = 0
        for p in self.mortgagedList:
            print(f'  Mortgaged {i}: {p}')
            i += 1
        
        ind = int(input('    ind: '))
            
        if self.mortgagedList[ind].owner != self:
            print("  You dont't own this property!")
            return
        else:
            p = self.mortgagedList[ind]
            
        if not p.mortgaged:
            print(f' *** {p} is not mortgaged')
        else:
            self.reduceCash(int(p.priceProperty / 2))
            p.mortgaged = False
            print(f'    ** Unmortgaged {p}')

    def sellAll(self):
        for p in self.properties:
            p.owner = None
    
    def attemptPurchase(self, game, s: Square):
        print(f'    Purchase {s.getPrice()}')
        pr = s.getPrice()
        if self.cash >= pr:
            self.reduceCash(pr)
            s.owner = self
            self.properties.append(s)
            self.properties.sort(key=cmp_to_key(cmpProperties))
            if isinstance(s, PropertySquare):
                c = self.getCollection(s, game.board)
                color = c.color
                if self.ownCollection(color, game.board.collections):
                    print('  ** Got whole collection')
                    answer = input('      Buy houses ? ')
                    answer = answer.upper()
                    if answer == 'Y':
                      self.buyHouses(game.board, s)        
        else:
            print('  ** Not enough cash for purchase!')
            
    def ownProperty(self, s):
        return s.owner == self
    
    def ownCollection(self, color, collections):
        for c in collections:
            if c.color == color:
                break
                
        for i in range(3):
            p = c.properties[i]
            if not p.owner:
                return False
                
            if not self.ownProperty(c.properties[i]):
                return False
                
        return True
        
    def getCollection(self, p, board):
        if isinstance (p, PropertySquare):
            for c in board.collections:
                 for q in c.properties:
                     if p == q:
                         return c
        
        else:
            return None
            
    def buyHotel(self, s):
        s.hasHotel = True
        s.nbHouses = 0
        s.setRent(s.getRent() + 100)
        self.reduceCash(s.price[4])
    
    def buyHouses(self, board, s, repeat = True):
         
#        print(' ownCollection : {ownCollection(color, board.collections)}')
        if not isinstance(s, PropertySquare):
            print(f"  ** Can't buy houses on non property square {s}")
            return False
            
        c = self.getCollection(s, board)
        color = c.color
        if not self.ownCollection(color, board.collections):
            print('  ** You do not own collection')
            return False
            
        if s.nbHouses == 4:
            print('  ** You have 4 houses, you should buy a hotel!')
            return False
            
        if self.cash >= s.price[s.nbHouses]:
            self.reduceCash(s.price[s.nbHouses])
            s.addHouse()
            s.setRent(s.getRent() + 50)
            print(f'  *** Bought a house on {s}!')
            if repeat:
                r = input('  Buy another? ')
                if r.upper() == 'Y':
                    self.buyHouses(board, s)
            return True
        else:
            print('  *** Attempted to buy a house but not enough cash!')
            return False

    def exchangeProperties(self, squares):
        i = int(input('  * Property to exchange : '))
        j = int(input('  * Against : '))
        
        p = squares[i]
        q = squares[j]

        p.owner, q.owner = q.owner, p.owner

        try:
            p.owner.properties.append(q)
            q.owner.properties.append(p)
        except AttributeError:
            print(f'  {Color.B_Red}*** Property not owned!{Color.B_Default}')
            return
            
        
        try:
            p.owner.properties.remove(p)
            q.owner.properties.remove(q)
        except ValueError:  # TODO: rewap properties (undo)
            print(f'  {Color.B_Red}*** Not the right owner!{Color.B_Default}')
            p.owner, q.owner = q.owner, p.owner
            
            return
            
        self.properties.sort(key=cmp_to_key(cmpProperties))
        o.properties.sort(key=cmp_to_key(cmpProperties))
      
        
        pd = int(input('  * Price difference : '))
        self.reduceCash(pd)
        o.addCash(pd)
           
    def payRent(self, s, board, p, r):
        if isinstance(s, PropertySquare) and s.nbHouses == 0 and not s.hasHotel:
            if p.ownCollection(p.getCollection(s, board).color, board.collections):
                print('    ** Doubling rent')
                r *= 2
        if ( r > self.cash):
            ''' getCash() TODO
            '''
            print('  *** I have no more money!!!')
            if self.haveHotels():
                self.cash += self.sellHotels(r - self.cash)
            if self.cash > r:
                self.reduceCash(r)
                p.addCash(r)
              
                return True
                
            if self.haveHouses():
                self.cash += self.sellHouses(r - self.cash)
                if ( r > self.cash):
                    print('      Doing mortgage')
                    self.cash += self.doMortgage(r - self.cash)
            else:
                print('  * I have no houses to sell, trying mortgage')
                self.cash += self.doMortgage(r - self.cash)
        if ( r <= self.cash):
            print(f'    Paying rent: {r}')
            self.reduceCash(r)
            p.addCash(r)
        else:
            p.addCash(self.cash)
            print(f'{Color.B_LightYellow}**** I lost, quitting game{Color.B_Default}')
            return False
            
        return True
            
    def addCash(self, pr):
        self.cash += pr
        return self.cash
        
    def playSquare(self, game, loc, square, adv):
        rent = 0
        
        if isinstance(square, Square):
            if isinstance(square, PropertySquare):
                colorname = game.board.color[game.board.collections.index(self.getCollection(square, game.board))]
                color = Color.getColor(colorname)
            else:
                color = Color.getColor('F_LightBlue')
            if hasattr(self.getCollection(square, game.board), 'color'):                
                print(f'{color}  Square {loc} : {square.address}{Color.F_White}')
            else:
                print(f'{color}  Square {loc} : {square.address}{Color.F_White}')
            if square.owner != None:
                print(f'{Color.F_LightYellow}  owner : {square.owner.name}{Color.F_White}')
            if square.mortgaged:
                print(f'{Color.F_Green}    ** Mortgaged, no rent.{Color.F_White}')
                return True
        
        if isinstance(square, UtilitySquare):
            if square.owner != None:
                rent = square.getRent(adv)
                print(f'  Utility Square: rent = {rent}')
            elif square.canPurchase():
                print('  Can purchase')
                self.attemptPurchase(game, square)
                return True
            else:
                if self != square.owner:
                    rent = square.getRent(adv)
                    if not self.payRent(square, game.board, square.owner, rent):
                        game.quit(self)
                        return False
                return True
        elif isinstance(square,CardSquare):
            card = game.board.chanceCards.pop()
            game.board.usedChanceCards.append(card)
            self.playCard(game, card, adv)
            return True
        elif isinstance(square,GoSquare):
            self.playGoSquare(square.title, loc)
            return True
        else:
            if square.canPurchase():
                print('  Can purchase')
                self.attemptPurchase(game, square)
                if isinstance(square, RRSquare):
                    self.setRRCount(self.getRRCount() + 1)
#                    square.rent = 50 * self.getRRCount()
                    print(f'  getRRCount = {self.getRRCount()}')
                return True
            else:
                if isinstance(square, Square) and not square.owner == self:
                    rent = square.getRent()
                
        if rent != 0:
            if self != square.owner:
                print(f'{Color.F_Red}  rent = {rent}{Color.F_White}')
                if not self.payRent(square, game.board, square.owner, rent):
                    game.quit(self)
                    return False
        return True

    def playCard(self, m, card, adv):
        print(f'  Chance card: {card.content}')
        
        if len(m.board.chanceCards) == 0:
            m.board.chanceCards = m.board.usedChanceCards.copy()
            print('       ** Shuffling chance cards **')
            random.shuffle(m.board.chanceCards)
            m.board.usedChanceCards.clear()
        
        match card.ind:
            case 0:
                self.piece.loc = 23
                square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 1:
                self.piece.loc = 0
                self.addCash(200)
                self.addCash(200)  # TODO: should be in advance() (to Go)
            case 2:
                if self.piece.loc > 7:
                    self.addCash(200)
                self.piece.loc = 7
                square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 3:
                self.piece.loc = (self.piece.loc + 1) % 40
                square = m.board.squares[self.piece.loc]
                while(not isinstance(square, RRSquare)):
                    self.piece.loc = (self.piece.loc + 1) % 40
                    square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 4:
                self.piece.loc = (self.piece.loc + 1) % 40
                square = m.board.squares[self.piece.loc]

                while(not isinstance(square, UtilitySquare)):
                    self.piece.loc = (self.piece.loc + 1) % 40
                    square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 5:
                self.addCash(50)
            case 6:
                self.freeCard = True
            case 7:
                m.advance(self, self.piece.loc, -3)
                square = m.board.squares[self.piece.loc]
                if isinstance(square, PropertySquare) or isinstance(square, RRSquare)\
                or isinstance(square, UtilitySquare) or isinstance(square, GoSquare):
                    print(f' Landed on {square}')
                    self.playSquare(m, self.piece.loc, square, adv)
                elif isinstance(square, ChanceSquare):
                    print(f' Landed on chance square')
                    card = m.board.chanceCards.pop()
                    m.board.usedChanceCards.append(card)
                    self.playCard(m, card, adv)
                elif isinstance(square, CCSquare):
                    print(f' Landed on CC square')
                    card = m.board.chanceCards.pop()
                    m.board.usedChanceCards.append(card)
                    self.playCard(m, card, adv)
                else:
                    print(f' Landed on impossible {square}')
                    
            case 8:
                self.piece.loc = 30
                self.inJail = True
            case 9:
                nbHouses = 0
                nbHotels = 0
                for p in self.properties:
                    if isinstance(p, PropertySquare):
                        nbHouses += p.nbHouses
                self.reduceCash(50 * nbHouses + 100 * nbHotels)
            case 10:
                self.reduceCash(15)
            case 11:
                if self.piece.loc > 35:
                    self.addCash(200)
                self.piece.loc = 35
                square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 12:
                for p in m.players:
                    if p != self:
                        p.addCash(50)
                        self.reduceCash(50)
            case 13:
                self.addCash(150)
            case 14:
                if self.piece.loc > 17:
                    self.addCash(200)
                self.piece.loc = 17
                square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)

         
              
    def playGoSquare(self, title, loc):
        print(f'  Square: {loc}. Landed on a go: {title}')
        if loc == 10:
            self.piece.loc = 30
            self.inJail = True
        
    def getRRCount(self): 
        return self.RRCount
        
    def setRRCount(self, rrc): 
        self.RRCount = rrc
           
          
def DBconnect():
   print('trying connection')
   app.run(host='127.0.0.1', port=5001, debug=True)

global ms_url

''' 
def _get_squares():
    address = []
    filename='classicmodels_customers.sql'
    with open(filename, 'r') as f:
        value = f.readline()
        value = value.split(",")
        while(value):
#            print(value)
            address.append(value[0] + ' ' + value[1])
            value = f.readline()
            if (value): value = value.split(",")
#        print(f'address = {address}')

    squares = [address[i] for i in range(24)]
    squares = [s.replace('"', '') for s in squares]

    squares[0] =  '__86__'
    for s in squares:
        print(f's = {s}, {s[0]}, {s[1]}')

    ms_url = get_mysql_uri()
    engine = create_engine(ms_url)
    print("Created engine : ", ms_url)
    wait_for_mysql_to_come_up(engine)
    DBconnect()
 

    get_session = sessionmaker(bind=create_engine(ms_url))
    session = get_session()
     
    with open('squares.sql', 'w') as f:
        for s in squares:
            print(f's = {s}')
            instr =f'INSERT INTO squares Values ("Property", "{s}");'
            instr.strip('\n')
            f.write(instr)
            print(f'instr = {instr}')
            session.execute(text(instr))

    squares = [(PropertySquare(), s) for s in squares]

    r = 0
    for s in squares:
        s[0].setRent(r)
        r += 5
        
    squares.insert(4, (RailRoadSquare(), 'Mahattet Elhijaz'))
     
    print(f'squares = {squares}')
     
    return squares
'''
def getColor(p, collections):
    for c in collections:
        if p in c.properties:
            return c.color
            
    return None

def listFree(game):
    squares = game.board.squares
    freeList = []
    for s in squares:
        if isinstance(s, Square) and not s.owner:
            freeList.append(s)
            if isinstance(s, PropertySquare):
                colorname = game.board.color[game.board.collections.index(game.players[game.currentPlayer].getCollection(s, game.board))]
                color = Color.getColor(colorname)
            else:
                color = Color.getColor('F_LightBlue')
                
            print(f'{color} squares[{game.board.squares.index(s)}] : {s.address}')
    if len(freeList) == 0:
        print(f'    {Color.B_LightGray}{Color.F_Green}No more free properties{Color.F_Default}{Color.B_Default}')
        
    return freeList


def execCmd(choice, game, p):
    match choice:
        case 'L':
            game.board.listProperties(p)
        case 'P':
            p.printProperties(game.board)
        case 'B':
            i = int(input("  Property's index: "))
            p.buyHouses(game.board, game.board.squares[i], False)
        case 'H':
            i = int(input("  Property's index: "))
            p.buyHouses(game.board, game.board.squares[i])
        case 'O':
            i = int(input("  Property's index: "))
            p.buyHotel(game.board.squares[i])
        case 'E':
            p.exchangeProperties(game.board.squares)
        case 'F':
            listFree(game)
        case 'U':
            p.unmortgageProperty()
        case 'R':
            print('  ** TODO **')
        case 'S':
            print('  ** TODO **')
        case 'M':
            print(f'{Color.F_Magenta}  ** Cash = {p.cash}')
        case 'T':
            for c in game.board.chanceCards:
                print(f'Card[{c.ind}]: {c.content}')
            p.playCard(game, game.board.chanceCards[8], 0)
            p.attemptPurchase(game, game.board.squares[1])
            p.attemptPurchase(game, game.board.squares[3])
            p.attemptPurchase(game, game.board.squares[4])
            p.buyHouses(game.board, game.board.squares[3])
            print(f'{Color.B_Yellow}******************************************')
            print(f'*  {Color.B_Green}CONGRATULATIONS {game.players[0].name} YOU WON !!!{Color.B_Yellow}    *{Color.B_Default}')
            print(f'{Color.B_Yellow}******************************************{Color.B_Default}')
        case '':
            pass

def menu(game, p):
    choice=''
    while choice != 'C':
        print(f'{Color.F_Blue}\n    **** Menu')
        print(f'{Color.F_Green}         L: List all properties')
        print('         P: Own properties')
        print('         B: Buy house')
        print('         H: Buy houses')
        print('         O: Buy hotel')
        print('         E: Exchange properties')
        print('         F: Free properties')
        print('         U: Unmortgage property')
        print('         R: Mortgage property')
        print('         S: Sell houses')
        print('         M: Money')
        print('         T: Test')
        print('         C: Continue')
        choice = input(f'{Color.F_Red}      Choice: ')
        choice = choice.upper()
        print(f'{Color.F_Blue}        You chose: {Color.F_White}', choice)
        
        execCmd(choice, game, p)
   
def main():
    
    game = MonopolyGame()
    '''     
    print(f'{game.board.collections[0].color} {game.board.collections[0].properties[0]}')
    square = game.board.squares[1]
    for col in game.board.collections:
        if col.ownProperty(square):
            print(f'index = {game.board.collections.index(col)}')
            break
    print(f'Found = {game.board.collections[0].ownProperty(square)}')
    '''    
#    print(f'n squares {len(game.board.squares)}')
#    print(game.board.squares[0].address)

    p = game.players[0]
    loc = 0
    
    game.playerCount = len(game.players)
    while(game.playerCount != 1):
        print('===============')
        print(f'Player: {p.name}')
        print('_______________')
        menu(game, p)
        replay = True
        adv = game.cup.roll()
        while replay:
            if not game.cup.double():
                p.nbDoubles = 0
                replay = False
            elif p.inJail:
                replay = False
            else:
                replay = True
                p.nbDoubles += 1

            adv = p.takeTurn(game, adv)

            if adv != 0:
                loc = game.advance(p, loc, adv)
                if p.nbDoubles == 3:
                    p.nbDoubles = 0
                    break
            else:
                replay = False
                break
            
            square = game.board.squares[loc]
            if not p.playSquare(game, loc, square, adv):
                replay = False
               
            if p.inJail:
                replay = False
                break
            
            print(f'{Color.F_Magenta}Cash = {p.cash}{Color.F_White}')
            
            if replay:
                adv = game.cup.roll()
            else:
                p.nbDoubles = 0
                break

        p = game.nextPlayer()
        
    print(f'{Color.B_Yellow}**********************************************************')
    print(f'{Color.F_Green}*          CONGRATULATIONS {game.players[0].name} YOU WON !!!            *{Color.B_Default}')
    print(f'{Color.B_Yellow}**********************************************************{Color.B_Default}')
       
if __name__ == '__main__':
    main()
    
           