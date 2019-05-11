from item import item
from storage_item import Storage_item
import typing

class Tag_item(item):

    def __init__(self, name: str, tag_list: [Tag_item]):
        self.name = name        #name of the tag
        self.tag_list = tag_list #list of tags
        self.used_in_item: [[Storage_item]] = []   #list of list of items