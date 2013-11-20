from genesis.ui import *
from genesis.api import *
import backend

class HostsPlugin(CategoryPlugin):
  text = 'Hosts/Aliases'
  iconfont = 'gen-screen'
  folder = 'advanced'
  
  def on_init(self):
    be = backend.Config(self.app)
    self.hosts = be.read()
    self.hostname = be.gethostname()

  def on_session_start(self):
    self._editing = None
    self._editing_self = False
    
  def get_ui(self):
    ui = self.app.inflate('hosts:main')
    t = ui.find('list')
    return ui

  @event('button/click')
  def on_click(self, event, params, vars = None):
    if params[0] == 'add':
      self._editing = len(self.hosts)
      
  @event('dialog/submit')
  def on_submit(self, event, params, vars = None):
    if params[0] == 'dlgEdit':

