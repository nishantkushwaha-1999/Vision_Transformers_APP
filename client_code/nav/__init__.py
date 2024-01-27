from ._anvil_designer import navTemplate
from anvil import *
import anvil.server
from basicCNN import basicCNN

class nav(navTemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)



    # Any code you write here will run before the form opens.

  def BasicCNN_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.main.clear()
    self.main.add_component(basicCNN())
    
