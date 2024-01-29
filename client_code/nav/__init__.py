from ._anvil_designer import navTemplate
from anvil import *
import anvil.server
from basicCNN import basicCNN
import plotly.express as px

class nav(navTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def BasicCNN_click(self, **event_args):
    self.flow_panel_1.clear()
    self.flow_panel_1.add_component(basicCNN())

  def ViTCNN_click(self, **event_args):
    data = anvil.server.call("history_all")
    
    
