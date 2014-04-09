import Hoggy2
import Hoggy2.models.quote as quote
from random import randint
print "importing"
@Hoggy2.hoggy_web.route("/")
def index(self):
    return quote.Quote.get_quote().body