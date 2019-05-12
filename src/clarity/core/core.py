import clarity.database.in_memory_db.file_db as fd
import clarity.database.in_memory_db.tag_db as td
from clarity.database.in_memory_db.tag_item import Tag_item
from clarity.database.in_memory_db.file_item import File_item
from clarity.database.in_memory_db.folder_item import Folder_item
from clarity.database.in_memory_db.initialize_data import Initialize_data



def main():
    c = Core()
    c.run()

class Core():

    def __init__(self):
        self.tagDB = td.Tag_db()
        self.fileDB = fd.File_db()
        init = Initialize_data()
        init.init_tags(self.tagDB)
        init.init_storage_items(self.fileDB, self.tagDB)

        root_tag = self.tagDB.return_tag("root")
        self.last_tag = root_tag
        self.current_tags = [root_tag]
        pass

    def run(self):
        pass
    
    # List Tags with text

    def get_tag_by_name(self, name):
        return self.tagDB.return_tag(name)
    
    def list_tags_start_with_text(self, text):
        tags = self.tagDB.tags_start_with(text)
        tags = sorted(tags,key=lambda tag: len(tag.used_in_folder_items) + len(tag.used_in_file_items))
        return tags
    
    def list_tags_with_text(self, text):
        tags = self.tagDB.tags_contain(text)
        tags = sorted(tags,key=lambda tag: len(tag.used_in_folder_items) + len(tag.used_in_file_items))
        return tags

     # LIST items with tags

    def list_tags_with_tags(self, tags):
        return self.tagDB.list_tags_with_tags(tags)

    def list_files_with_tags(self, tags):
        return self.tagDB.list_files_with_tags(tags)

    def list_folders_with_tags(self, tags):
        return self.tagDB.list_folders_with_tags(tags)

    def list_storage_items_with_tags(self, tags):
        return self.tagDB.list_folders_with_tags(tags) + self.tagDB.list_files_with_tags(tags)

      # LIST Tags of item

    def list_tags_of_item(self, item):
        return self.tagDB.list_tags_of_item(item)

    def list_tags_of_tag(self, tag):
        return self.tagDB.list_tags_of_item(tag)

    def list_tags_of_file(self, file):
        return self.tagDB.list_tags_of_item(file)

    def list_tags_of_folder(self, folder):
        return self.tagDB.list_tags_of_item(folder)
    
    # SET Tags of item

    def set_tag_tags(self, tag, tags):
        self.tagDB.set_tag_tags(tag, tags)
        
    def set_file_tags(self, file, tags):
        self.fileDB.set_file_tags(file, tags)
    
    def set_folder_tags(self, folder, tags):
        self.fileDB.set_folder_tags(folder, tags)

   # ADD items

    def add_tag(self, tag: str, tags):
        self.tagDB.add_tag(tag, tags)

    def add_file(self, file: str, directory: str, tags = []):
        self.fileDB.add_file(file, directory, tags)

    def add_folder(self, folder: str, directory: str, tags = []):
        self.fileDB.add_folder(folder, directory, tags)

## SEARCH
    # SEARCH helpers

    def add_search_term(self, text):
        self.search_term = text

    def remove_tag_from_search(self, tag):
        if tag not in self.current_tags:
            self.current_tags.remove(tag)

    def add_tag_to_search(self, tag):
        self.current_tags.append(tag)

    def list_current_tags(self):
        return self.current_tags

    def get_last_tag(self):
        return self.last_tag

    def change_search_tag(self, tag_to_change, new_tag):
        self.current_tags.insert(self.current_tags.index(tag_to_change), new_tag)
        self.current_tags.remove(tag_to_change)
        
    def replace_search_tag(self, tag_to_replace, new_tag):
        self.current_tags.insert(self.current_tags.index(tag_to_replace), new_tag)
        self.current_tags.remove(tag_to_replace)

    # LIST predictions
    
    def list_tag_predictions(self):
        #TODO hier sollte eigendlich eine prediction zu den tags anhand von search history kommen (sinvoll? schon vorhanden?)
        tags = self.list_tags_with_text(self.search_term)
        tags = sorted(tags,key=lambda tag: tag.name)
        return tags

    def list_file_predictions(self):
        return []

    def list_folder_predictions(self):
        return []

    # List Tags with querry
    #TODO dont do it now
    def list_tags_with_querry(self, querry):
        return []

##

    # LIST all items


    def list_all_files(self):
        return self.fileDB.list_all_files()

    def list_all_folders(self):
        return self.fileDB.list_all_folders()
    
    def list_all_tags(self):
        return self.tagDB.list_all_tags()

    # LIST items that match exactly with the tags
    
    def list_exact_files(self, tags):
        files = [file for file in self.tagDB.list_files_with_tags(tags) if len(file.tag_list) == len(tags)]
        return files

    def list_exact_folders(self, tags):
        folders = [folder for folder in self.tagDB.list_folders_with_tags(tags) if len(folder.tag_list) == len(tags)]
        return folders

    def list_exact_tags(self, tags):
        tags = [tag for tag in self.tagDB.list_tags_with_tags(tags) if len(tag.tag_list) == len(tags)]
        return tags

    # MODULE stuff
    def list_all_modules(self):
        return []

if __name__ == "__main__":
    main()