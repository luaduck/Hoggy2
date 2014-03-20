from flask import Flask, url_for, request
from twisted.words.protocols import irc
from twisted.internet import reactor
import time, os, logging, sys, Hoggy2.utils
from Hoggy2.utils.HoggyLogger import HoggyLogger
from irc_bot import HoggyBot, HoggyBotFactory
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
    thread = Thread(target = reactor.run, args=(False, ))
    thread.setDaemon(True)
    thread.start()

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    app.run()

if __name__ == "__main__":
    main()
