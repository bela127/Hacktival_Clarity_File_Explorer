from item import item
import String

class tag_item(item):

    def __init__(self, name: String, tag_list):
        self.name = name        #name of the tag
        self.tag_list = tag_list #list of tags
        self.used_in_item = []   #list of list of items