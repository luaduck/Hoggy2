from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Hoggy2.app_irc import config

if config.get('hoggy', 'dbtype') == 'mysql':
    MSQLUname = config.get('hoggy', 'mysqlusername')
    MSQLPW = config.get('hoggy', 'mysqlpassword')
    MSQLHost = config.get('hoggy', 'mysqlhost')
    MSQLPort = config.get('hoggy', 'mysqlport')
    MSQLDB = config.get('hoggy', 'mysqldatabase')
    engine = create_engine('mysql://%s:%s@%s:%s/%s' % (MSQLUname, MSQLPW, MSQLHost, MSQLPort, MSQLDB))
else:
    SQLITEFILE = config.get('hoggy', 'dbfile') 
    engine = create_engine('sqlite:///%s' % SQLITEFILE)
    print 'sqlite:///%s' % SQLITEFILE

Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()