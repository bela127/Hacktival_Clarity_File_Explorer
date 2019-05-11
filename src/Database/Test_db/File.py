import persistent

class File(persistent.Persistent):
    def __init__(self, name, directory, tag_list):
        self.name = name
        self.directory = directory
        self.tag_list = tag_list

    