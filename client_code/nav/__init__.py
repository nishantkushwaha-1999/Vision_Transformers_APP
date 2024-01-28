from ._anvil_designer import navTemplate
from anvil import *
import anvil.server
from basicCNN import basicCNN

class nav(navTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def BasicCNN_click(self, **event_args):
    self.main.clear()
    self.main.add_component(basicCNN())
    
