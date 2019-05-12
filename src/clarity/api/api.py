# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:28:27 2019

@author: User
"""

from clarity.core.core import Core

class API:
    
    def __init__(self):
        self._core = Core()
    
    
    # List Tags with text
    
    def list_tags_start_with_text(self, text):
        return self._core.list_tags_start_with_text(text)
    
    def list_tags_with_text(self, text):
        return self._core.list_tags_with_text(text)

     # LIST items with tags

    def list_tags_with_tags(self, tags):
        return self._core.list_tags_with_tags(tags)

    def list_files_with_tags(self, tags):
        return self._core.list_files_with_tags(tags)

    def list_folders_with_tags(self, tags):
        return self._core.list_folders_with_tags(tags)

    def list_storage_items_with_tags(self, tags):
        return self._core.list_storage_items_with_tags(tags)

      # LIST Tags of item

    def list_tags_of_item(self, item):
        return self._core.list_tags_of_item(item)

    def list_tags_of_tag(self, tag):
        return self._core.list_tags_of_tag(tag)

    def list_tags_of_file(self, file):
        return self._core.list_tags_of_file(file)

    def list_tags_of_folder(self, folder):
        return self._core.list_tags_of_folder(folder)
    
    # SET Tags

    def set_tag_tags(self, tag, tags):
        self._core.set_tag_tags(tag, tags)
    
    def set_file_tags(self, file, tags):
        self._core.set_file_tags(file, tags)
    
    def set_folder_tags(self, folder, tags):
        self._core.set_folder_tags(folder, tags)

   # ADD items

    def add_tag(self, tag, tags = []):
        self._core.add_tag(tag, tags)

    def add_file(self, file, tags = []):
        self._core.add_file(file, tags)

    def add_folder(self, folder, tags = []):
        self._core.add_folder(folder, tags)

## SEARCH
    # SEARCH helpers

    def list_current_tags(self):
        return self._core.list_current_tags()

    def get_last_tag(self):
        return self._core.get_last_tag()

    def change_search_tag(self, tag_to_change, new_tag):
        self._core.change_search_tag(tag_to_change, new_tag)

    def replace_search_tag(self, tag_to_replace, new_tag):
        self._core.replace_search_tag(tag_to_replace, new_tag)

    # LIST predictions
    
    def list_tag_predictions(self):
        return self._core.list_tag_predictions()

    def list_file_predictions(self):
        return self._core.list_file_predictions()

    def list_folder_predictions(self):
        return self._core.list_folder_predictions()

    # List Tags with querry

    def list_tags_with_querry(self, querry):
        return self._core.list_tags_with_querry(querry)

##

    # LIST all items

    def list_all_files(self):
        return self._core.list_all_files()

    def list_all_folders(self):
        return self._core.list_all_folders()

    def list_all_tags(self):
        return self._core.list_all_tags()

    # LIST exact items
    
    def list_exact_files(self, tags):
        return self._core.list_exact_files(tags)

    def list_exact_folders(self, tags):
        return self._core.list_exact_folders(tags)

    def list_exact_tags(self, tags):
        return self.list_exact_tags(tags)

    # MODULE stuff
    def list_all_modules(self):
        return self._core.list_all_modules()

    # NOT SORTED YET
    def get_tag_by_name(self, text):
        return self._core.get_tag_by_name(text)
    
    def add_tag_to_search(self, tag):
        self._core.add_tag_to_search(tag)
    
    def remove_tag_from_search(self, tag):
        self._core.remove_tag_from_search(tag)