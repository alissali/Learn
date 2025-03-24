'''          
  My Monopoly
  TODO: Player knows game (players out of game?)
  TODO: payPlayer(), listOtherProperties, Property exchange (Done),
        CC card, buyHotel (menu and attemptPurchase option), Parking
        Adresses in Cards
        Property price
        rent in DB and initialisation
        Player.attemptPurchase : replace insert + sort with insertInSorted
        Use Square.ind instead of board.index()
        List Collection
        Register Playersc
'''

from Squares import *
from Cards import *
from mmysql import get_squares, get_chanceCards, wait_for_mysql_to_come_up

import random
from functools import cmp_to_key
import os

from flask import Flask, render_template, request, session, url_for, redirect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import text


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

        color = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Brown', 'Magenta', 'Rose']
        
        k = 0
        for i in range(0, 8):
            self.collections[i].color = color[i]
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
            print(f'i : {i}, {s}')
            if isinstance(s, PropertySquare):
                if s.owner:
                    print(f' ({s.owner.name}) --- {player.getCollection(s, self).color}')
            i += 1
        
class Piece:
    def __init__(self):
        self.loc = 0
   
    def isOn(s: Square):
        pass
        
class MonopolyGame:
    def __init__(self):
        nbPlayers = 4
        
        print('Creating MonopolyGame')
        self.board = Board()
        self.cup = Cup()
        self.players = []
        self.players.append(Player('Hassan', 2000))
        self.players.append(Player('Mamoun', 2000, True))
        self.players.append(Player('Rima', 2000))
        self.players.append(Player('Saleem', 2000))
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
            p.addCash(500)
        p.piece.loc = (p.piece.loc + distance) % 40

        return p.piece.loc
             
    def quit(self, p):
        p.sellAll()
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
    nh1 = p1.getnbHouses()
    nh2 = p2.getnbHouses()
    if nh1 > nh2:
      return 1
    elif nh1 < nh2:
      return -1
    return 0
      
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
        if self.inJail:
            if self.nbTurnsInJail == 3:
               self.nbTurnsInJail = 0
               self.reduceCash(50)
               self.inJail = False
               print('    Forced out of Jail, fine paid!')
               return dv
    
            self.nbTurnsInJail += 1
               
            self.answer = 'y'
            if m.cup.double():
                self.inJail = False
                self.nbTurnsInJail = 0
                print('    Double! Got out of Jail')
                return dv
            elif self.freeCard:
                if self.human:
                    self.answer = input('Use out-of-jail card ? ')
                    if self.answer.lower() == 'n':
                        return 0
                print('    Using out-of-jail card')
                self.freeCard = False
                self.inJail = False
                self.nbTurnsInJail = 0
                return dv
            else:
                self.answer = input('Pay fine ? ')
                if self.answer.lower() == 'y':
                    self.reduceCash(50)
                    self.nbTurnsInJail = 0
                    self.inJail = False
                    return dv                        
                else:
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
        
        return dv
        
    def reduceCash(self, pr):
        self.cash -= pr
        
    def printProperties(self, board):
        for p in self.properties:
            print(f'    Property[{board.squares.index(p)}]: {p}')
            if isinstance(p, PropertySquare):
                print(f'      Houses: {p.nbHouses}. Rent: {p.rent} ({self.getCollection(p, board).color})')

    def haveHouses(self):
        for p in self.properties:
            if isinstance(p, PropertySquare) and p.nbHouses != 0:
                return True
        return False
      
    def sellHouses(self, missedAmount):
        print('  ** Selling houses')
        props = [p for p in self.properties if isinstance(p, PropertySquare)]
        if props:
            props.sort(key=cmp_to_key(cmpHouses), reverse=True)
            i = 0
            saleAmount = 0
            while saleAmount < missedAmount and i < len(props):
                if i == len(props) and self.haveHouses():
                    i = 0
                if props[i].nbHouses > 0:
                    saleAmount += int(props[i].price[props[i].nbHouses] - 1 / 2)
                    props[i].nbHouses -= 1
                    props[i].setRent(props[i].getRent() - 50)
                i += 1
                
            print(f'  *** Sold for {saleAmount}.')
        
            return saleAmount
        else:
            return 0
    
    def doMortgage(self, missedAmount):
        return missedAmount - 1
    
    def sellAll(self):
        for p in self.properties:
            p.owner = None
        pass
    
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
                      menu(game, self)
        
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
        color = None
        for c in board.collections:
             for q in c.properties:
                 if isinstance (q, PropertySquare):
                    if p == q:
                        color = c.color
                        return c
                
        print(f'Color = {color}') 
        
        if not color:
            print('Color Error!')
            return None
    
                
    def buyHouse(self, board, s):
         
#        print(' ownCollection : {ownCollection(color, board.collections)}')
        if not isinstance(s, Square):
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
            s.addHouse()
            self.reduceCash(s.price[s.nbHouses])
            s.setRent(s.getRent() + 50)
            print(f'  *** Bought a house on {s}!')
            return True
        else:
            print('  *** Attempted to buy a house but not enough cash!')
            return False

    def exchangeProperties(self, squares):
        i = int(input('  * Property to exchange : '))
        j = int(input('  * Against : '))
        
        p = squares[i]
        q = squares[j]
        
        o = q.owner
        q.owner = self
        p.owner = o
        
        self.properties.append(q)
        o.properties.append(p)
        self.properties.remove(p)
        o.properties.remove(q)
        self.properties.sort(key=cmp_to_key(cmpProperties))
        o.properties.sort(key=cmp_to_key(cmpProperties))
      
        
        pd = int(input('  * Price difference : '))
        self.reduceCash(pd)
        o.addCash(pd)
           
    def payRent(self, p, r):
        if ( r > self.cash):
            print('  *** I have no more money!!!')
            if self.haveHouses():
                self.cash += self.sellHouses(r - self.cash)
                if ( r > self.cash):
                    self.cash += self.doMortgage(r - self.cash)
            else:
                print('  * I have no houses to sell, trying mortgage')
                self.cash += self.doMortgage(r - self.cash)
        if ( r <= self.cash):
            print(f'    Paying rent: {r}')
            self.reduceCash(r)
            p.addCash(r)
        else:
            print(f'**** I lost, quitting game')
            return False
            
        return True
            
    def addCash(self, pr):
        self.cash += pr
        
    def playSquare(self, game, loc, square, adv):
        rent = 0
        
        if isinstance(square, Square):
            print(f'  Square {loc} : {square.address}')
            if square.owner != None:
                print(f'  owner : {square.owner.name}')
        
        if isinstance(square, UtilitySquare):
            if square.owner != None:
                rent = square.getRent(adv)
                print(f'  UtilitySquare: rent = {rent}')
            elif square.canPurchase():
                print('  Can purchase')
                self.attemptPurchase(game, square)
                return True
            else:
                if self != square.owner:
                    rent = square.getRent(adv)
                    if not self.payRent(square.owner, rent):
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
                    square.rent = 50 * self.getRRCount()
                return True
            else:
                if isinstance(square, Square) and not square.owner == self:
                    rent = square.getRent()
                
        if rent != 0:
            if self != square.owner:
                print(f'  rent = {rent}')
                if not self.payRent(square.owner, rent):
                    game.quit(self)
                    return False
        return True

    def playCard(self, m, card, adv):
        print(f'  Chance card: {card.content}')
        
        match card.ind:
            case 0:
                self.piece.loc = 23
                square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 1:
                self.piece.loc = 0
                self.addCash(200)
            case 2:
                if self.piece.loc > 7:
                    self.addCash(200)
                self.piece.loc = 7
                square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 3:
                if self.piece.loc > 17:
                    self.addCash(200)
                self.piece.loc = 17
                square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 4:
                self.piece.loc = (self.piece.loc + 1) % 40
                square = m.board.squares[self.piece.loc]
                while(not isinstance(square, RRSquare)):
                    self.piece.loc = (self.piece.loc + 1) % 40
                    square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 5:
                self.piece.loc = (self.piece.loc + 1) % 40
                square = m.board.squares[self.piece.loc]

                while(not isinstance(square, UtilitySquare)):
                    self.piece.loc = (self.piece.loc + 1) % 40
                    square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 6:
                self.addCash(50)
            case 7:
                self.freeCard = True
            case 8:
                m.advance(self, self.piece.loc, -3)
                square = m.board.squares[self.piece.loc]
                if isinstance(square, PropertySquare) or isinstance(square, RRSquare) or isinstance(square, UtilitySquare):
                    print(f' Landed on {square.address}')
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
            case 9:
                self.piece.loc = 30
                self.inJail = True
            case 10:
                nbHouses = 0
                nbHotels = 0
                for p in self.properties:
                    if isinstance(p, PropertySquare):
                        nbHouses += p.nbHouses
                self.reduceCash(50 * nbHouses + 100 * nbHotels)
            case 11:
                self.reduceCash(15)
            case 12:
                if self.piece.loc > 35:
                    self.addCash(200)
                self.piece.loc = 35
                square = m.board.squares[self.piece.loc]
                self.playSquare(m, self.piece.loc, square, adv)
            case 13:
                for p in m.players:
                    p.addCash(50)
                    self.reduceCash(50)
            case 14:
                self.addCash(150)
         
        if len(m.board.chanceCards) == 0:
            m.board.chanceCards = m.board.usedChanceCards.copy()
            random.shuffle(m.board.chanceCards)
            m.board.usedChanceCards.clear()
              
    def playGoSquare(self, title, loc):
        print(f'  Square: {loc}. Got a go! : {title}')
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

def menu(game, p):
    choice=''
    while choice != 'C':
        print('    **** Menu')
        print('         L: List all properties')
        print('         P: Own properties')
        print('         B: Buy house')
        print('         E: Exchange properties')
        print('         F: Free properties')
        print('         M: Money')
        print('         T: Test')
        print('         C: Continue')
        choice = input('      Choice: ')
        choice = choice.upper()
        print('    You chose: ', choice)
        
        match choice:
            case 'L':
                game.board.listProperties(p)
            case 'P':
                p.printProperties(game.board)
            case 'B':
                i = int(input("  Property's index: "))
                p.buyHouse(game.board, game.board.squares[i])
            case 'E':
                p.exchangeProperties(game.board.squares)
            case 'F':
                for s in game.board.squares:
                    if isinstance(s, Square) and not s.owner:
                        print(f'squares[{game.board.squares.index(s)}] : {s.address}')
                        if isinstance(s, PropertySquare):
                            print(f'  ({p.getCollection(s, game.board).color})')
            case 'M':
                print(f'  ** Cash = {p.cash}')
            case 'T':
                for c in game.board.chanceCards:
                    print(f'Card[{c.ind}]: {c.content}')
                p.playCard(game, game.board.chanceCards[8], 0)
   
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
    
    while(True):
        print('_______________')
        print(f'Player : {p.name}')
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
            
            print(f'Cash = {p.cash}')
            
            if replay:
                adv = game.cup.roll()
            else:
                p.nbDoubles = 0
                break

        p = game.nextPlayer()
       
if __name__ == '__main__':
    main()
    
           