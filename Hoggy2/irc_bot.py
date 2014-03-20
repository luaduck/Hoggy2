from twisted.words.protocols import irc
from twisted.internet import protocol, reactor
import time

class HoggyBot(irc.IRCClient):
    def __init__(self, config, log, *args, **kwargs):
        self.nickname = config.get("irc", "nick")
        self.password = config.get("irc", "password")
        self.log = log
        self.config = config

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        self.log.info("Connected at %s" % time.asctime(time.localtime(time.time())))

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        self.log.info("Disconnected at %s" % time.asctime(time.localtime(time.time())))


    # callbacks for events
    def signedOn(self):
        """Called when bot has succesfully signed on to server."""
        self.log.debug("Joining %s" % self.config.get("irc", "channel"))
        self.join(self.config.get("irc", "channel"))

    def joined(self, channel):
        pass

    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        user = user.split('!', 1)[0]

        # Check to see if they're sending me a private message
        if channel == self.nickname:
            msg = "It isn't nice to whisper!  Play nice with the group."
            self.msg(user, msg)
            return

        # Otherwise check to see if it is a message directed at me
        if msg.startswith(self.nickname + ":"):
            msg = "%s: I am a log bot" % user
            self.msg(channel, msg)

    def action(self, user, channel, msg):
        """This will get called when the bot sees someone do an action."""
        user = user.split('!', 1)[0]

    # irc callbacks

    def irc_NICK(self, prefix, params):
        """Called when an IRC user changes their nickname."""
        old_nick = prefix.split('!')[0]
        new_nick = params[0]


    # For fun, override the method that determines how a nickname is changed on
    # collisions. The default method appends an underscore.
    def alterCollidedNick(self, nickname):
        """
        Generate an altered version of a nickname that caused a collision in an
        effort to create an unused related name for subsequent registration.
        """
        return nickname + '^'

class HoggyBotFactory(protocol.ClientFactory):
    """A factory for HoggyBots.
    A new protocol instance will be created each time we connect to the server.
    """

    def __init__(self, config, log):
        self.config = config
        self.log = log
        self.channel = config.get("irc","channel")

    def buildProtocol(self, addr):
        p = HoggyBot(self.config, self.log)
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        reactor.stop()