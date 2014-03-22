import Hoggy2, Hoggy2.utils, Hoggy2.views
from Hoggy2.utils.HoggyLogger import HoggyLogger
from irc_bot import HoggyBotFactory
from twisted.words.protocols import irc
from twisted.internet import reactor
from threading import Thread

config = Hoggy2.utils.get_config()
log = HoggyLogger(__name__, config.get('hoggy', 'logfile'))

def main():
    log.info("Hello! - Starting IRC Bot!")

    # create factory protocol and application
    f = HoggyBotFactory(config, log)
    
    # connect factory to this host and port
    reactor.connectTCP(config.get('irc', 'host'), int(config.get('irc', 'port')), f)
    
    # run bot
    #thread = Thread(target = reactor.run, args=(False, ))
    #thread.setDaemon(True)
    #thread.start()
    reactor.run()
    #Hoggy2.hoggy_web.run()

if __name__ == "__main__":
    main()
