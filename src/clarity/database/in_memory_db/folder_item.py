from storage_item import Storage_item
from tag_item import Tag_item
import typing

class Folder_item(Storage_item):

    def __init__(self, name: str, directory: str, tag_list: [Tag_item]):
        super().__init__(self, name, directory, tag_list)