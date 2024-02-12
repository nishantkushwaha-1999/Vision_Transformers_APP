from ._anvil_designer import try_allTemplate
from anvil import *
import anvil.server
# from io import StringIO

class try_all(try_allTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    # try:
    result = anvil.server.call("image", file)
    print('cnn', result)
    # result = anvil.server.call("predict_vit", file)
    # print('ViT', result)
    # except ValueError:
      
