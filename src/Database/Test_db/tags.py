import persistent

class Tags(persistent.Persistent):
    def __init__(self, name, tag_list):
        self.name = name
        self.tag_list = tag_list
        self.used_in_item = []

    