from tag_item import Tag_item
from item import Item

class Tag_db():
    def __init__(self):
        self.tags: [Tag_item] = []      #list of tags
    
    # returns all tags that start with the string text
    def tags_start_with(self, text):
        tag_list = []
        for i in self.tags:
            if text.startswith(self.tags[i].name):
                tag_list.append(self.tags[i].name)
    
        return tag_list

    # returns all tags that contain the string text
    def tags_contain(self, text):
        tag_list = []
        for i in self.tags:
            if text in self.tags[i].name:
                tag_list.append(self.tags[i])
    
        return tag_list

    # returns a tag
    def tag(self, name):
        for i in self.tags:
            if name == self.tags[i].name:
                return self.tags[i]
        return None
    
    # gets a name and a taglist and creates a tag
    def add_tag(self, name, tags):
        new_tag = Tag_item(name, tags)
        self.tags.append(new_tag)
    
    # gets an item and returns a list of tags of this item
    def list_tags_of_item(self, item: Item):
        for i in self.tags:
            if item.name == self.tags[i].name:
                return self.tags[i].tag_list
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



    
    