import Hoggy2
import Hoggy2.utils
from Hoggy2.utils.HoggyLogger import HoggyLogger

config = Hoggy2.utils.get_config()
log = HoggyLogger(__name__, config.get('hoggy', 'logfile'))

def main():
    Hoggy2.hoggy_web.debug = True
    Hoggy2.hoggy_web.run()

if __name__ == "__main__":
    main()