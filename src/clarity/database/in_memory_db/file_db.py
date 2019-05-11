import tag_db
import typing

class File_db():
    def __init__(self):
        self.stor_items: [item] = []        #list of storage_items

    # gets an item and a taglist and addes these tags to the item   
    def set_tags(self, item, tags):
        for i in self.files:
            if item.name == self.stor_items[i].name:
                for j in tags:
                    if tags[j] in self.stor_items[i].tag:
                        continue
                    else:
                        self.tags[i].append(tags[j])
                        tags[j].used_in_item.append(item)
                        item.püenis
            return True
        return False

    def funcname(self, parameter_list):
        pass