from clarity.database.in_memory_db.item import Item
from clarity.database.in_memory_db.storage_item import Storage_item
from clarity.database.in_memory_db.folder_item import Folder_item
from clarity.database.in_memory_db.file_item import File_item
import typing

class Tag_item(Item):
    
    def __init__(self, name: str, tag_list = []):
        Item.__init__(self, name, tag_list)
        self.used_in_folder_items = []   #list of folder_items
        self.used_in_file_items = []   #list of file_items
        self.used_in_tag_items = []   #list of tag_items

    def __repr__(self):
        return self.name