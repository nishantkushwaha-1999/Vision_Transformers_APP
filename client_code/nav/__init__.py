from ._anvil_designer import navTemplate
from anvil import *
import anvil.server
from basicCNN import basicCNN
from try_all import try_all
from plotly import graph_objects as go
# from io import StringIO
# import pandas as pd

class nav(navTemplate):
  def __init__(self, **properties):
    plot = Plot()
    self.init_components(**properties)

  def BasicCNN_click(self, **event_args):
    self.flow_panel_1.clear()
    self.flow_panel_1.add_component(basicCNN())

  def ViTCNN_click(self, **event_args):
    data = anvil.server.call("get_history", "basicCNN", "all")
    print(data)

  def try_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.flow_panel_1.clear()
    self.flow_panel_1.add_component(try_all())

  def button_1_click(self, **event_args):
    data = anvil.server.call("evaluate_bCNN")
    print(data)
    
    
