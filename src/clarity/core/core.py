if __name__ == "__main__":
    main()

def main():
    c = Core()
    c.run()

class Core():

    def __init__(self):
        self.last_tag = root_tag
        self.current_tags = [root_tag]
        pass

    def run(self):
        pass
    
    # List Tags with text
    
    def list_tags_start_with_text(self, text):
        pass
    
    def list_tags_with_text(self, text):
        pass

     # LIST items with tags
    
    def list_items_with_tags(self, tags):
        pass

    def list_tags_with_tags(self, tags):
        pass

    def list_files_with_tags(self, tags):
        pass

    def list_folders_with_tags(self, tags):
        pass

      # LIST Tags of item

    def list_tags_of_item(self, item):
        pass

    def list_tags_of_tag(self, tag):
        pass

    def list_tags_of_file(self, file):
        pass

    def list_tags_of_folder(self, folder):
        pass
    
    # SET Tags

    def set_item_tags(self, item, tags):
        pass

    def set_tag_tags(self, tag, tags):
        pass
    
    def set_file_tags(self, file, tags):
        pass
    
    def set_folder_tags(self, folder, tags):
        pass

   # ADD items

    def add_tag(self, tag, tags = []):
        pass

    def add_file(self, file, tags = []):
        pass

    def add_folder(self, folder, tags = []):
        pass

    #-------

    def index_item(self, name, directory, tags):
        pass
    
    def index_file(self, name, directory, tags):
        pass

    def index_folder(self, name, directory, tags):
        pass

    def create_tag(self, name, tags):
        pass

## SEARCH
    # SEARCH helpers

    def list_current_tags(self):
        return []

    def get_last_tag(self):
        return self.last_tag

    def change_search_tag(self, orginal_tag, new_tag):
        pass

    def replace_search_tag(self, orginal_tag, new_tag):
        pass

    # LIST predictions
    
    def list_tag_predictions(self):
        return []

    def list_file_predictions(self):
        return []

    def list_folder_predictions(self):
        return []

    # List Tags with querry

    def list_tags_with_querry(self, querry):
        pass

##

    # LIST all items

    def list_all_files(self):
        pass

    def list_all_folders(self):
        pass

    def list_all_tags(self):
        pass

    # LIST exact items
    
    def list_exact_files(self, tags):
        pass

    def list_exact_folders(self, tags):
        pass

    def list_exact_tags(self, tags):
        pass

    # MODULE stuff
    def list_all_modules(self):
        pass