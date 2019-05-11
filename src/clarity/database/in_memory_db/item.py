from tag_item import Tag_item
import typing

class Item():

    def __init__(self, name: str, tag_list: [Tag_item]):
        self.name: str = name
        self.tag_list: [Tag_item] = tag_list