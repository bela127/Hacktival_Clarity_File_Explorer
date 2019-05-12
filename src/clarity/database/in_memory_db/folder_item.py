from clarity.database.in_memory_db.storage_item import Storage_item
import typing

class Folder_item(Storage_item):

    def __init__(self, name: str, directory: str, tag_list):
        super().__init__(name, directory, tag_list)

    def __repr__(self):
        return self.name