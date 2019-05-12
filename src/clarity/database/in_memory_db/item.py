import typing

class Item():

    def __init__(self, name: str, tag_list):
        self.name: str = name
        self.tag_list = tag_list