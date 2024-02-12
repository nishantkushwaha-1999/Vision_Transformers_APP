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
    print(anvil.server.call("get_history", 'basicCNN', 'val'))
    print(anvil.server.call("get_history", 'basicCNN', 'all'))
    print(anvil.server.call("get_history", 'ViT', 'val'))
    print(anvil.server.call("get_history", 'ViT', 'all'))

    print(anvil.server.call("evaluate", 'basicCNN'))
    print(anvil.server.call("evaluate", 'vit'))

    im = anvil.server.call("image", file)
    self.image_1.source = im

    print(anvil.server.call("predict", 'basicCNN'))
    print(anvil.server.call("predict", 'vit'))
    # result = anvil.server.call("predict_vit", file)
    # print('ViT', result)
    # except ValueError:
      
