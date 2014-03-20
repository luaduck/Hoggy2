import sys, ConfigParser

def get_config(config= ConfigParser.RawConfigParser(), file=None):
    try:
        try:
            if file is None:
                raise
            config.read(file)
        except:
            print "Falling back to default config.ini"
            config.read("config.ini")
            
        return config
    except:
        print "Config file is un-readable or not present.  Make sure you've created a config.ini (see config.ini.default for an example)"
        exit()