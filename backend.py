from genesis.api import *
from genesis.utils import *
from genesis.com import *
from genesis import apis

class Host:
  def __init__(self):
    self.ip = '';
    self.name = '';
    self.aliases = '';
    
  class Config(Plugin):
    implements(IConfigurable)
    name = 'Hosts'
    iconfont = 'gen-screen'
    id = 'hosts'
    
    def list_files(self):
      return ['/etc/hosts']
    
    def read(self):
      ss = ConfManager.get().load('hosts', '/etc/hosts').split('\n')
      r = []
      
      for s in ss:
        if s != '' and s[0] != '#':
          try:
            s = s.split()
            h = Host()
            try:
              h.ip = s[0]
              h.name = s[1]
              for i in range(2, len(s)):
                h.aliases += '%s ' % s[i]
                h.aliases = h.aliases.rstrip();
          except:
            pass
            r.append(h)
          except:
            pass      
      return r

    def save(self, hh):
      d = ''
      for h in hh:
        d += '%s\t%s\t%s\n' % (h.ip, h.name, h.aliases)
        ConfManager.get().save('hosts', '/etc/hosts', d)
        ConfManager.get().commit('hosts')
        
    def gethostname(self):
      return self.app.get_backend(IHostnameManager).gethostname()
        
    def sethostname(self, hn):
      self.app.get_backend(IHostnameManager).sethostname(hn)

  class ArchHostnameManager(Plugin):
    implements(IHostnameManager)
    platform = ['arch', 'arkos']
    
    def gethostname(self):
      return open('/etc/hostname').read()
    
    def sethostname(self, hn):
      open('/etc/hostname', 'w').write(hn)
