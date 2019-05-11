from tag_item import Tag_item
from item import Item

class Tag_db():
    def __init__(self):
        root_tag = Tag_item("root")
        self.tags: [Tag_item] = [root_tag]      #list of tags
    
    # returns all tags that start with the string text
    def tags_start_with(self, text):
        tag_list = []
        for tag in self.tags:
            if tag.name.startswith(text):
                tag_list.append(tag)
    
        return tag_list

    # returns all tags that contain the string text
    def tags_contain(self, text):
        tag_list = []
        for tag in self.tags:
            if tag.name.contain(text):
                tag_list.append(tag)
    
        return tag_list

    # returns a tag
    def tag(self, name):
        for tag in self.tags:
            if name == tag.name:
                return self.tag
        return None
    
    # gets a name and a taglist and creates a tag
    def add_tag(self, name, tags):
        new_tag = Tag_item(name, tags)
        self.tags.append(new_tag)
    
    # gets an item and returns a list of tags of this item
    def list_tags_of_item(self, item: Item):
        for tag in self.tags:
            if item.name == tag.name:
                return tag.tag_list
        return[]

    # returns all existing tags
    def list_all_tags(self):
        return self.tags

    # gets a list of tags and returns all folders where these tags are used 
    def list_folders_with_tags(self, tag_list: [Tag_item]):
        folders = [folder for folder in tag.used_in_folder_items for tag in self.tags]
        folders = list(set(folders))
        return folders

    def list_files_with_tags(self, tag_list: [Tag_item]):
        files = [file for file in tag.used_in_file_items for tag in self.tags]
        files = list(set(files))
        return files

    def list_tags_with_tags(self, tag_list: [Tag_item]):
        tags = [tag for tag in tag.used_in_tag_items for tag in self.tags]
        tags = list(set(tags))
        return tags



    
    