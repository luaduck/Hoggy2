import Hoggy2
import Hoggy2.models.quote as quote
from random import randint

@Hoggy2.hoggy_web.route("/")
def index(self):
    return quote.Quote.get_quote().body