from item import item
from tag_item import Tag_item
import typing

class Storage_item(item):
    def __init__(self, name: str, directory: str, tag_list: [Tag_item]):
        self.name = name
        self.directory = directory
        self.tag_list = tag_list