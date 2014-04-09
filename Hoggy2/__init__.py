import Hoggy2.utils
from Hoggy2.utils.HoggyLogger import HoggyLogger

config = Hoggy2.utils.get_config()
log = HoggyLogger(__name__, config.get('hoggy', 'logfile'))

from flask import Flask
hoggy_web = Flask(__name__)
