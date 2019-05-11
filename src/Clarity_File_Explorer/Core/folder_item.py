from item import item

class folder_item(item):

    def __init__(self, name, directory, tag_list):
        self.name = name
        self.directory = directory
        self.taglist = tag_list