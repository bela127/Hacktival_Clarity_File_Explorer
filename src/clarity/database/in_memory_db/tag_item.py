from item import item
from storage_item import Storage_item
from folder_item import Folder_item
from file_item import File_item
import typing

class Tag_item(item):
    
    def __init__(self, name: str, tag_list: [Tag_item]):
        super().__init__(self, name, tag_list)
        self.used_in_folder_item: [Folder_item] = []   #list of folder_items
        self.used_in_file_item: [File_item] = []   #list of file_items
        self.used_in_tag_item: [Tag_item] = []   #list of tag_items