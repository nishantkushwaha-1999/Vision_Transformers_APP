from ._anvil_designer import basicCNNTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go

class basicCNN(basicCNNTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.plot_1.data = [
      go.Bar(
        x = [1, 2, 3],
        y = [3, 1, 6],
        name = 'Bar Chart Example'
      )
    ]
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
