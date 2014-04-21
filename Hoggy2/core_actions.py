from abc import ABCMeta, abstractproperty, abstractmethod
from random import choice
import random, time, requests, praw, re
from time import gmtime
import Hoggy2.models.time as time_model
import Hoggy2.models.quote as quote

def get_adjusted_time(adjustment):
    adj = gmtime(time.time()+adjustment*60*60)
    return time.strftime("%a %H:%M", adj)

class ActionException(Exception):
    def __init__(self, message):
        super(ActionException, self).__init__(message)

class Action(object):
    __metaclass__ = ABCMeta
    actions = {}

    @abstractproperty
    def shortdesc(self):
        return "No help available."

    @abstractproperty
    def longdesc(self):
        return "No help available."

    @abstractmethod
    def execute(self, bot, user, channel, args):
        pass

class ping(Action):
    def shortdesc(self):
        return "Check if the bot is listening"

    def longdesc(self):
        return "Sometimes he likes to ignore people, or just straight up go away."

    def execute(self, bot, user, channel, args):
        return choice(["Hoozin'd it up.  Naw Just kidding. Pong.", "pong", "pang", "poong", "ping?", "pop", "pa-pong!", "kill yourse- sorry, pong", "ta-ping!", "Wasn't that Mulan's fake name?"])

class settime(Action):
    def shortdesc(self):
        return "Set your timezone"
    
    wanted = "!settime [UTC|GMT][+|-]hours"

    def longdesc(self):
        return wanted

    def execute(self, bot, user, channel, args):
        time = " ".join(args)

        if not time or not user:
            return
        reg = re.compile("^(ZULU|GMT|UTC)(\+|-)[0-9]{1,2}[:|\.]{0,1}[0-9]{0,2}$")
        if not reg.match(time):
            return "Hey, try the format: {0}".format(settime.wanted)
        dir = 1
        if '-' in time:
            dir = -1
        time = time[4:]
        if ':' in time:
            parts = time.split(':')
            if len(parts[1]) != 2:
                return "Two digits for minutes, thank you very muchly"
            hours = int(parts[0]) + (float(parts[1]) / 60.0)
        elif '.' in time:
            hours = float(time)
        else:
            hours = int(time)
        user = user.lower()
        hours *= dir

        time_to_change = time_model.Time.get_by_name(user)
        if not time_to_change:
            time_to_change = time_model.Time()
            time_to_change.name = user

        time_to_change.time = hours
        time_to_change.save()
        return "Your clock is now set at {0}".format(get_adjusted_time(hours))

class when(Action):
    def shortdesc(self):
        return "Gets the current time for the given user"
    
    def longdesc(self):
        return "Try !when <user>, requires that user to have done a !settime first"

    def execute(self, bot, user, channel, args):
        target = args[0]
        low = target.lower()

        if low == "hoggy":
            return "I am beyond both time and space, mortal"

        return_time = time_model.Time.get_by_name(low)
        if not return_time:
            raise ActionException("They don't appear to have set a time yet, sorry")
        return_time = get_adjusted_time(return_time.time)
        return "The local time in {0}-land is: {1}".format(target, return_time)

class urbandictionary(Action):
    def shortdesc(self):
        return "Get completely relevant and 100% accurate definition from Urban Dictionary"

    def longdesc(self):
        return "try !ud A-10 to get everyone in the chat to love you"

    def execute(self, bot, user, channel, args):
        r = requests.get("http://api.urbandictionary.com/v0/define?term={0}".format(" ".join(args)))
        json = r.json()
        defs = json['list']
        if not len(defs):
            return "No definintions found.  Try !eject."
        return "{0}: {1}".format(" ".join(args), defs[0]['definition'].encode('utf-8'))

class new(Action):
    def shortdesc(self):
        return "Update the subreddit header with something extremely thought-provoking or insightful."
    
    def longdesc(self):
        return "Now with added sidebar garbling!"

    def execute(self, bot, user, channel, args):
        #if args[0] == '!hoggy':
        #    if int(args[1]):
        #        header = hoggy.execute(args[1])
        #    else:
        #        return "Usage: !new hoggy 15"
        #else:
        header =  " ".join(args).replace("=","\=")

        manager = praw.Reddit("HoggyBot for /r/%s by /u/zellyman" % bot.config.get('reddit', 'subreddit'))
        manager.login(bot.config.get('reddit', 'username'), bot.config.get('reddit', 'password'))
        subreddit = manager.get_subreddit(bot.config.get('reddit', 'subreddit'))
        settings = subreddit.get_settings()
        template = "testing"
        new_desc = "### %s \n=\n\n" % header
        new_desc += template

        subreddit.set_settings(settings['title'], description=new_desc)

        return "Header Updated!"

class lightning(Action):
    def shortdesc(self):
        return "THUNDER STRIKE"

    def longdesc(self):
        return "http://www.youtube.com/watch?v=j_ekugPKqFw"

    def execute(self, bot, user, channel, args):
        target = args[0]
        return "LIGHTNING BOLT! %s takes %d damage" % (target, random.randint(0,9999))

class no(Action):
    def longdesc(self):
        return "For use in dire situations only."

    def shortdesc(self):
        return "For dire situations."

    def execute(self, *args):
        return "http://nooooooooooooooo.com/"

class blame(Action):
    def longdesc(self):
        return "No seriously, fuck that guy."

    def shortdesc(self):
        return "Fuck that guy."

    def execute(self, bot, user, channel, args):
        if not len(args):
            return "Usage: !blame <user>"
        if args[0].lower() == 'hoozin':
            return "^"
        elif args[0].lower() == 'hoggy':
            return "What'd I do?"
        messages = [
            "I concur, %s is absolutely responsible.",
            "Dammit, %s, now you've gone and Hoozin'ed it up."
        ]
        return choice(messages) % args[0]

class eject(Action):
    def shortdesc(self):
        return "Get the hell out of Dodge!"
    
    def longdesc(self):
        return "Leave the room in style."

    def execute(self, bot, user, channel, args):
        bot.kick(channel, user, 'Ejecting!')
        return "EJECT! EJECT! EJECT! {0} punched out!".format(user)

class hoggy(Action):
    """
    This Action is added to the actions dict in irc_bot.py.  Don't add it to the Action.actions dict yourself.
    It's added there so that the action key for this class can be the name of the bot itself.
    """
    def longdesc(self):
        return "With no arguments will display a random quote. [#] will display the quote with the specified ID. [add <quote>] will add the specified <quote> to the db. [search <string>] will look for that string in the db. [count] should show the number of quotes stored."

    def shortdesc(self):
        return "Display or add quotes"

    def execute(self, bot, user, channel, args):
        if len(args):
            command = args[0]
            if command.isdigit():
                return_quote = quote.Quote.get_quote(id=command)
                if return_quote is None:
                    return "Nothing found for %s" % command
                return "%s (%s)" % (return_quote.body, return_quote.id)

            if command == "add":
                return_quote = " ".join(args[1:])
                id = quote.Quote.add_quote(quote)
                return "Added %s (#%s)" % (quote, id)

            if command == "search":
                terms = " ".join(args[1:])
                return bot.config.get('hoggy', 'search_url') + "?query=%s" % terms

            if command == "remove":
                id = args[1]
                if not id.isdigit():
                    return "Usage: !%s remove <id>" % bot.nickname

                delete_quote = quote.Quote.get_quote(id=id)
                try:
                    delete_quote.delete()
                    return "Removed %s (#%s)" % (delete_quote.body, delete_quote.id)
                except:
                    raise ActionException("Error removing quote.")

        else:
            return_quote = quote.Quote.get_quote()
            return "%s (%s)" % (return_quote.body, return_quote.id)

class hug(Action):
    def shortdesc(self):
        return  "Hoggit is not responsible for any rape allegations that may arise from using this command"

    def longdesc(self):
        return  "It makes me cringe when I think about it"

    def execute(self, bot, user, channel, args):
        try:
            target = args[0]
        except:
            target = None

        if target is None:
            return "What, hug myself?"
        elif target.lower() == user.lower():
            return "Hugging yourself? Keep it clean!"
        else:
            return "%s gives %s a lingering hug. %s likes it. Likes it a lot...\nThey continue their embrace, %s gently stroking %s's face, and %s leans in for a kiss." % (user, target, target, target, user, user)

class roll(Action):
    def shortdesc(self):
        return "Roll them bones"
    
    def longdesc(self):
        return "Randomly generates some numbers given input in the format of <number of dice>d<number of sides> ie: 1d20 will roll a single 20 sided die. Maximum 10 dice and 100 sides"

    def execute(self, bot, user, channel, args):
        if len(args) != 1:
            return "Usage: !roll 1d20"
        try:
            darray = args[0].split("d")
            numdice = int(float(darray[0]))
            numsides = int(float(darray[1]))
            if numdice <= 0 or numdice > 10 or numsides <= 0 or numsides > 100 or (float(darray[0]) != int(darray[0])) or (float(darray[1]) != int(darray[1])) :
                return "You gotta throw at least 1 die, throw no more than 10, it needs at least 1 side, and no more than 100."

            dice = []
            total = 0
            for i in range(numdice):
                die = random.randint(1, numsides)
                dice.append(die)
                total += die
            if numdice > 1:
                return 'Go! Dice Roll! ' + ', '.join([str(x) for x in dice]) + ' (' + str(total) + ')'
            else:
                return ' '.join([str(x) for x in dice])
        except Exception, ex:
            raise ex

class choose(Action):
    def shortdesc(self):
        return "Chooses something"

    def longdesc(self):
        return "Picks a random string given input in the format <string> or <string> or <string>.... etc."

    def execute(self, bot, user, channel, args):
        if len(args) == 0:
            return "You gotta give me some choices!"

        temp = ' '.join([str(x) for x in args])
        return "Hmm, let's go with {0}".format(choice(temp.split("or")).strip())



class grab(Action):
    def shortdesc(self):
        return "Grab the last n lines of a specific user and create a quote"

    def longdesc(self):
        return "Usage: !grab <user> <number of lines>  number of lines defaults to 1"

    def execute(self,bot, user, channel, args):
        if len(args) == 1:
            num_lines = 1
        else:
            try:
                num_lines = int(args[1])
            except:
                num_lines = 0

        if num_lines < 1:
            return "{0}... Don't be a dipshit.".format(user)

        if args[0].lower() == 'hoggy':
            return "Got no time to be playing with myself..."

        quote = bot.grabber.grab(args[0], num_lines)
        h = hoggy()
        return h.execute(bot, user, channel, ["add", quote])


Action.actions = {
    "!ping": ping,
    "!when": when,
    "!settime": settime,
    "!ud": urbandictionary,
    #"!new": new,
    "!lightning": lightning,
    "!no": no,
    "!blame": blame,
    "!eject": eject,
    "!grab": grab,
    "!hug": hug,
    "!roll": roll,
    "!choose": choose
}

import Hoggy2.action_plugins