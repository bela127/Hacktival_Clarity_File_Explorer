from tag_item import tag_item
from folder_item import folder_item
from file_item import file_item
class item():

    def __init__(self, item_type):
        self.item_type = item_type
        if item_type == 1:
            self.item = tag_item()
        elif item_type == 2:
            self.item = file_item()
        elif item_type == 3:
            self.item = folder_item()
    
    