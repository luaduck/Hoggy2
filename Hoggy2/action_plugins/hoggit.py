# Stuff that only makes sense in the Hoggit community

from Hoggy2.core_actions import Action
import requests
from random import choice
 
class ron(Action):
    def shortdesc(self):
        return "Why the fuck would you use this command? It's a complete waste of time."

    def longdesc(self):
        return "Kill yourself"

    def execute(self, bot, user, channel, args):
        if (len(args)):
            target = args[0]
        else:
            target = None

        if target is not None:
            return "%s, you little fuck." % (target)
        else:
            messages = [
                "I would smack you in the mouth if I wouldn't feel bad for hitting a retard afterwards.",
                "If you project Excel, there better be fucking numbers in it somewhere.",
                "I would trade 3 of you for a talking version of Wikipedia or Wolfram Alpha. Seriously, don't get comfortable fucksticks.",
                "It's not rape if you yell out \"SURPRISE!\"",
                "Windows Vista was like a whore house when the ships come in",
                "\"Hush you I'm recalling the time Ron sent me cocaine via USPS\"",
                "\"\"Listen,\" he said, leaning closer, \"I\'m a fucking piranha in this pool. All these other socially awkward people, I eat them up. That\'s right, fucker,\" he added. \"That\'s just how I roll.\" He grabbed a woman seated to his right. A tattoo of a tree covered her back. George pointed. I looked. A small R.G. was nestled on one of the branches.  --RonUSMC\"",
                "Ron doesn\'t miss you, fuck you.",
                "Ron\'s a fucking piranha in this pool",
                "What\'s up, faggots? --Ron"
            ]
            return "%s" % (choice(messages))

Action.actions["!ron"] = ron

class backpedal(Action):
  def shortdesc(self):
    return "In case of major backpedal"
    
  def longdesc(self):
    return "NAH NAH NAH NAH-NAAAAAAAAAAAAAAAAAAAAA NAH."
    
  def execute(self, bot, user, channel, args):
    return "http://www.youtube.com/watch?v=ubU-dB8B-94"
    
Action.actions["!backpedal"] = backpedal

class thanks(Action):
  def shortdesc(self):
    return "For use by Canadians and their subsidiaries only"
    
  def longdesc(self):
    return "Like this ever gets any use"
    
  def execute(self, bot, user, channel, args):
	if (len(args)):
            target = args[0]
        else:
            target = None
    if target is not None:
            return "What about me?"
        else:
            return "No problem, %s" % (user)
    
Action.actions["!thanks"] = thanks



