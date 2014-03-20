import sys, ConfigParser, os

def get_config(config= ConfigParser.RawConfigParser(), file=None):
    try:
        try:
            if file is None:
                raise
            config.read(file)
        except:
            print "Falling back to default config.ini"
            config.read(os.path.dirname(os.path.abspath(__file__)) + "/../../config.ini")
            
        return config
    except:
        print "Config file is un-readable or not present.  Make sure you've created a config.ini (see config.ini.default for an example)"
        exit()