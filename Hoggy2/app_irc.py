import Hoggy2.utils
from Hoggy2.utils.HoggyLogger import HoggyLogger
from irc_bot import HoggyBotFactory
from twisted.internet import reactor

config = Hoggy2.utils.get_config()
log = HoggyLogger(__name__, config.get('hoggy', 'logfile'))

def main():
    log.info("Hello! - Starting IRC Bot!")
    # create factory protocol and application
    f = HoggyBotFactory(config, log)
    # connect factory to this host and port
    reactor.connectTCP(config.get('irc', 'host'), int(config.get('irc', 'port')), f)   
    # run bot
    reactor.run()

if __name__ == "__main__":
    main()
