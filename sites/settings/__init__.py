SETTINGS = 'dev'
try:
    from pre import SETTINGS
except:
    pass
exec 'from %s import *' % SETTINGS
