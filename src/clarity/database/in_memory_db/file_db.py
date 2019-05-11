import typing
from storage_item import Storage_item
from tag_item import Tag_item

class File_db():
    def __init__(self):
        self.stor_items: [Storage_item] = []        #list of storage_items

    # gets an item and a taglist and addes these tags to the item   
    def set_tags(self, item: Storage_item, tags: Tag_item):
        for i in self.stor_items:
            if item.name == self.stor_items[i].name:
                for j in tags:
                    if tags[j] in self.stor_items[i].tag:
                        continue
                    else:
                        self.stor_items[i].append(tags[j])
                        tags[j].used_in_item.append(item)
            return True
        return False

    # gets an storage_item and returns a list of tags that are related to this item
    def get_tags(self, item: Storage_item):
        for i in self.stor_items:
            if item == self.stor_items[i]:
                return self.stor_items[i].tag_list
        return[]

    