import typing
from clarity.database.in_memory_db.storage_item import Storage_item
from clarity.database.in_memory_db.folder_item import Folder_item
from clarity.database.in_memory_db.file_item import File_item
from clarity.database.in_memory_db.tag_item import Tag_item

class File_db():
    def __init__(self):
        self.stor_items = []        #list of storage_items

    # gets an item and a taglist and addes these tags to the item   
    def set_tags(self, item: File_item, tag_list: [Tag_item]):
        for i in self.stor_items:
            if item.name == self.stor_items[i].name:
                for j in tag_list:
                    if tag_list[j] in self.stor_items[i].tag:
                        continue
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

    # gets a file and a taglist and adds the tags to the file
    def set_file_tags(self, file: File_item, tag_list: [Tag_item]):
        tags = file.tag_list + tag_list
        file.tag_list = list(set(tags))
    
    # gets a folder and a taglist and adds the tags to the folder
    def set_folder_tags(self, folder: Folder_item, tag_list: [Tag_item]):
        tags = folder.tag_list + tag_list
        folder.tag_list = list(set(tags))
    
    # gets a name and a taglist and creates a file
    def add_file(self, name, directory, tags):
        new_file = File_item(name, directory, tags)
        self.stor_items.append(new_file)
        for tag in tags:
            tag.used_in_file_items.append(new_file)
    
    # gets a name and a taglist and creates a folder
    def add_folder(self, name, directory, tags):
        new_folder = Folder_item(name, directory, tags)
        self.stor_items.append(new_folder)
        for tag in tags:
            tag.used_in_folder_items.append(new_folder)

    # returns all files in the system
    def list_all_files(self):
        files: [File_item] = []
        for item in self.stor_items:
            if type(item) == type(File_item):
                files.append(item)
        return files

    # returns all folders in the system
    def list_all_folders(self):
        folders: [Folder_item] = [folder for folder in self.stor_items if type(folder) == type(Folder_item)]
        return folders
    
    # removes a file from the file-list 
    def remove_file(self, file):
        for tag in file.tag_list:
            tag.used_in_file_items.remove(file)
        
        self.stor_items.remove(file)
    
    # removes a folder from the file-list 
    def remove_folder(self, folder):
        for tag in folder.tag_list:
            tag.used_in_folder_items.remove(folder)
        
        self.stor_items.remove(folder)