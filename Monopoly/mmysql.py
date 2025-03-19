import pytest
import os
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker

from adapters import orm, repository

from Squares import *
from Cards import *

def get_mysql_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 3306 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "Allocation_123")
    user, db_name ="allocation", "monopoly" 
    return f"mysql://{user}:{password}@{host}:{port}/{db_name}"
'''    
@pytest.fixture(scope="session")
def mysql_session(mysql_db):
    start_mappers()
    yield sessionmaker(bind=mysql_db)()
    
    clear_mappers()
'''

def wait_for_mysql_to_come_up(engine):
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            return engine.connect()
        except OperationalError:
            time.sleep(0.5)
    pytest.fail("Mysql never came up")

if __name__ == "__main__":
    ms_url = get_mysql_uri()
    engine = create_engine(ms_url)
    print("Created engine : ", ms_url)
    wait_for_mysql_to_come_up(engine)
    get_session = sessionmaker(bind=create_engine(ms_url))
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)

def get_squares(session, squares):
    rows = session.execute(text(
        'SELECT * FROM squares'))

    n = len(squares)
    rent = 0
    p = 0
    price = [0 for i in range(5)]
    print(f'n = {n}')
    incRent = 0
    for r in rows:
        address = r[0]
        rent = r[1] + incRent
        price[0] = r[2]
        price[1] = r[3]
        price[2] = r[4]
        price[3] = r[5]
        price[4] = r[6]
        priceProperty = r[7]
        mortgage = r[8]
        res = str(f'{r[0]}').strip('[0-9]')
        incRent += 5

        while not isinstance(squares[p], Square) or isinstance(squares[p], RRSquare) or isinstance(squares[p], UtilitySquare):
            p += 1
            
        squares[p] = PropertySquare(res, rent, price, priceProperty, mortgage)
               
        p += 1
            
#        print(f'res = {res}')
    '''
    q = str('Adr')
    p = sq.Square(q)
    print(f'q = {q}, address = {p.address}')
    for s in squares:
        print(f's.address = {s.address}')
        print(f's = {s}')
    '''
      
    return squares
    
def get_chanceCards(session, chanceCards):
    rows = session.execute(text(
        'SELECT * FROM chanceCards'))
    
    i = 0
    for r in rows:
        chanceCards[i] = ChanceCard(r[0], i)
        i += 1
        
    return chanceCards
    
def get_tables(session):
    
    tables = session.execute(text(
        'SHOW TABLES'))
       
    return tables
