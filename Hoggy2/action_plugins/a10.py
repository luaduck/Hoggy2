# A realistic simulation of an A10

from Hoggy2.core_actions import Action
import requests
from random import choice
import random

class guns(Action):
  def shortdesc(self):
    return "Strike down your target with great vengeance and furious anger."
    
  def longdesc(self):
    return "Seriously, great vengeance and furious anger."
    
  def execute(self, bot, user, channel, args):
    if (len(args)):
        target = args[0]
    else:
        target = None
    if target is None:
        return 'BBBRRRRRRRAAAAPPPPPPPPPP!!!!'
    try:
        message =  "%s sets up a gun run...\n" % (user)
        
        if random.randint(0,100) > 33:
            message += "BBBRRRRRRRAAAAPPPPPPPPPP!!!! \n"
            message += "%s pulverized %s with great vengeance and furious anger" % (user, target)
        elif random.randint(0,100) > 60:
            message += "%s screwed up their attack run, but managed to pull out." % (user)
        else: 
            message += "%s ignored the VMU's 'PULL UP' and smashed into %s" % (user, target)
            bot.kick('hoggit', user, 'Is no more.')
    except Exception, ex:
        print ex
        message = "%s screwed up their gun run, but managed to pull out. What a wimp." % (user)

    return message
    
Action.actions["!guns"] = guns

class rifle(Action):
  def shortdesc(self):
    return "Fire an AGM-65 at your enemy (or friend)"
    
  def longdesc(self):
    return "About as likely to hit as the real thing"
    
  def execute(self, bot, user, channel, args):
    if (len(args)):
        target = args[0]
    else:
        target = None
    if target is None:
        return '(M) BBBBEEEEEEPPPPPP!  EVERYONE FLIP THE FUCK OUT'
    try:
        message = '%s slews over to the burning hot flesh-sack that is %s with an AGM-65 seeker....\n' % (user, target)
        message += 'ONE - RIFLE.\n'
        message += '(M) BBBBEEEEEEPPPPPP!  EVERYONE FLIP THE FUCK OUT\n'
        if random.randint(0,100) > 33:
            message += '%s sent %s into the third world with a well aimed Maverick.' % (user, target)
        else:
            message += '%s missed, the seeker locked onto a nearby pelican in flight.' % user
    except Exception, ex:
        print ex
        message = '(M) BBBBEEEEEEPPPPPP!  EVERYONE FLIP THE FUCK OUT'

    return message
		
Action.actions["!rifle"] = rifle

class pickle(Action):
  def shortdesc(self):
    return "Release the bombs of peace onto the target of desperation"
    
  def longdesc(self):
    return "This command does not add pickles to your sandwich."
    
  def execute(self, bot, user, channel, args):
    if (len(args)):
        target = args[0]
    else:
        target = None
    if target is None:
        messages = [
            'dropped his bombs without looking, and demolished an elementary school.  The horror is etched into the minds of generations to come.',
            'dropped his bombs with no target and and destroyed the penguin exhibit at the local zoo.  The screams can still be heard to this day',
            'dropped his bombs without looking, inadvertanly starting a war with New Zealand.'
        ]

        message = messages[random.randint(0,2)]
        return user + ' ' + message
    elif target.lower() == user.lower():
        bot.kick(channel, user, 'Self-immolation is not the way forward')
        return "%s rolls 180 degrees and drops his bombs... before realising what a silly mistake he made" % user
    bombs = [
        'Mk. 82',
        'Mk. 84',
        'CBU-87',
        'CBU-97',
        'GBU-10',
        'GBU-12',
        'GBU-38',
        'GBU-31'
    ]
    types = [ 'CCIP', 'CCRP' ]
    message = '%s released a %s %s toward %s\n' % (user, choice(types), choice(bombs), target)
    if random.randint(0,100) > 33:
        message += '%s obliterated %s with a well aimed Drop.' % (user, target)
    else:
        message += '%s missed, read the 9-line noob!' % user

    return message
		
Action.actions["!pickle"] = pickle


class wire(Action):
  def shortdesc(self):
    return "Accurately simulates a Vikhir missile - kicks the target on success, but good luck with that."
    
  def longdesc(self):
    return "Good luck"
    
  def execute(self, bot, user, channel, args):
    if (len(args)):
        target = args[0]
    else:
        target = None
    if target is None:
        messages = [
            "launches a Vikhir at empty space. Can't be worse than aiming at something."
        ]
        return "%s %s" % (user, choice(messages))
    elif target.lower() == user.lower():
        messages = [
            "manages to fire a Vikhir at themself. Lasers aren't for pointing into cockpits. Doesn't matter much though, it still missed."
        ]
        return "%s %s" % (user, choice(messages)) 
    else:
        if random.randint(0,100) < 2:
            # lol this is probably OP
            bot.kick(channel, target, 'You got Vikhir\'d, congrats!')
            return '%s actually hit %s using some kind of divine intervention!' % (user, target)
        else:
            messages = [
                "but they crashed for no good reason",
                "but it plowed into the ground",
                "but it overshot the target",
                "but it undershot the target",
                "but it veered to the right",
                "but it veered to the left",
                "but it hit an orphanage instead",
                "but their laser burned out",
                "however their tail fell off",
                "but their autopilot flipped out",
                "but their trim reset",
                "and it hit the target! .... nah",
                "but it fell in love with a passing Hind and they embraced awkwardly"
            ]
            return "%s launches a Vikhir at %s, %s." % (user, target, choice(messages))
    
Action.actions["!wire"] = wire