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
        return []
    
    def list_tags_with_text(self, text):
        return []

     # LIST items with tags

    def list_tags_with_tags(self, tags):
        return []

    def list_files_with_tags(self, tags):
        return []

    def list_folders_with_tags(self, tags):
        return []

    def list_storage_items_with_tags(self, tags):
        return []

      # LIST Tags of item

    def list_tags_of_item(self, item):
        return []

    def list_tags_of_tag(self, tag):
        return []

    def list_tags_of_file(self, file):
        return []

    def list_tags_of_folder(self, folder):
        return []
    
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

## SEARCH
    # SEARCH helpers

    def list_current_tags(self):
        return self.current_tags

    def get_last_tag(self):
        return self.last_tag

    def change_search_tag(self, tag_to_change, new_tag):
        pass

    def replace_search_tag(self, tag_to_replace, new_tag):
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
        return []

##

    # LIST all items

    def list_all_files(self):
        return []

    def list_all_folders(self):
        return []

    def list_all_tags(self):
        return []

    # LIST exact items
    
    def list_exact_files(self, tags):
        return []

    def list_exact_folders(self, tags):
        return []

    def list_exact_tags(self, tags):
        return []

    # MODULE stuff
    def list_all_modules(self):
        return []