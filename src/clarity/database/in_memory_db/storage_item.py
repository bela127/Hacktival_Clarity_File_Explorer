from item import item
from tag_item import Tag_item
import typing

class Storage_item(item):
    def __init__(self, name: str, directory: str, tag_list: [Tag_item]):
        super().__init__(self, name, tag_list)
        self.directory = directory