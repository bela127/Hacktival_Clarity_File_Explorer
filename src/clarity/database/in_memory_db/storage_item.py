from item import Item
from tag_item import Tag_item
import typing

class Storage_item(Item):
    def __init__(self, name: str, directory: str, tag_list: [Tag_item]):
        super().__init__(self, name, tag_list)
        self.directory = directory