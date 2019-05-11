import typing
from storage_item import Storage_item
from folder_item import Folder_item
from file_item import File_item
from tag_item import Tag_item

class File_db():
    def __init__(self):
        self.stor_items: [Storage_item] = []        #list of storage_items

    # gets an item and a taglist and addes these tags to the item   
    def set_tags(self, item: Storage_item, tag_list: [Tag_item]):
        for i in self.stor_items:
            if item.name == self.stor_items[i].name:
                for j in tag_list:
                    if tag_list[j] in self.stor_items[i].tag:
                        continue
                    else:
                        if type(self.stor_items[i]) == type(Folder_item):
                            tag_list[j].used_in_folde_item.append(item)
                        else:
                            tag_list[j].used_in_file_item.append(item)
                        self.stor_items[i].tag_list.append(tag_list[j])
            return True
        return False

    # gets an storage_item and returns a list of tags that are related to this item
    def get_tags(self, item: Storage_item):
        for i in self.stor_items:
            if item == self.stor_items[i]:
                return self.stor_items[i].tag_list
        return[]

    