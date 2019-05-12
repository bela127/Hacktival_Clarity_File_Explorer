from clarity.database.in_memory_db.item import Item

class Storage_item(Item):
    def __init__(self, name: str, directory: str, tag_list):
        super().__init__(name, tag_list)
        self.directory = directory

    def __repr__(self):
        return self.name