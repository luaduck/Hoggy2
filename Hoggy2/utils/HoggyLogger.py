import logging

class HoggyLogger(object):
    def __init__(self, name, logfile):
        try:
            log = logging.getLogger(name)
            log.setLevel(logging.DEBUG)
            fh = logging.FileHandler(logfile)
            fh.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')
            fh.setFormatter(formatter)

            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)

            log.addHandler(sh)
            log.addHandler(fh)

            self.log = log
        except ConfigParser.NoSectionError:
            raise Exception("Config file is un-readable or not present.  Make sure you've created a config.ini (see config.ini.default for an example)")

    def debug(self, message):
        self.log.debug(message)
    
    def info(self, message):
        self.log.info(message)

    def error(self, message):
        self.log.error(message)