from clarity.database.in_memory_db.item import Item

class Storage_item(Item):
    def __init__(self, name: str, directory: str, tag_list):
        super().__init__(self, name, tag_list)
        self.directory = directory