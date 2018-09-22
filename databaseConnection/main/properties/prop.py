import main.properties
from configparser import ConfigParser
from functools import partial
from itertools import chain


class dbProp(object):
    def __init__(self, section, file):
        self.readline = partial(next, chain(("[{0}]\n".format(section),), file, ("dbConnect.properties",)))

    def dbProp(self):
        try:
            cp = ConfigParser()
            cp.read("dbConnect.properties")
            cp.sections()
            cp.get('configFile', 'db.user')
            cp.items("configFile")
            cp.get("configFile", 'db.pass')
            print(cp.get("configFile", "db.url"))
            cp.get("configFile", 'db.url')
            cp.get("configFile", 'db.host')
            cp.get("configFile", 'db.port')

        except IOError as e:
            print("The exception is +", e)
#p=dbProp(section="",file="")
#p.dbProp()