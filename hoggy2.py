from flask import Flask, url_for, request
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
import time, os, logging, sys, utils
from utils import HoggyLogger

config = utils.get_config()
log = HoggyLogger(__name__, config.get('hoggy', 'logfile'))

class HoggyBot(irc.IRCClient):
    pass
