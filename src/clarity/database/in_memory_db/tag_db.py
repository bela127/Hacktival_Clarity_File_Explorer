from clarity.database.in_memory_db.tag_item import Tag_item

class Tag_db():
    def __init__(self):
        self.root_tag = Tag_item("root")
            
    # returns all tags that start with the string text
    def tags_start_with(self, text):
        tag_list = []
        for tag in self.root_tag.used_in_tag_items:
            if tag.name.startswith(text):
                tag_list.append(tag)
    
        return tag_list

    # returns all tags that contain the string text
    def tags_contain(self, text):
        return [tag for tag in self.root_tag.used_in_tag_items if text in tag.name]

    # returns a tag
    def return_tag(self, name):
        for tag in self.root_tag.used_in_tag_items:
            if name == tag.name:
                return tag
        return None
    
    # gets a name and a taglist and creates a tag
    def add_tag(self, name, tags):
        new_tag = Tag_item(name, tags)
        self.root_tag.used_in_tag_items.append(new_tag)
        for tag in tags:
            self.return_tag(tag.name).used_in_tag_items.append(new_tag)
    
    # gets an item and returns a list of tags of this item
    def list_tags_of_item(self, item):
        for tag in self.root_tag.used_in_tag_items:
            if item.name == tag.name:
                return tag.tag_list
        return[]

    # returns all existing tags
    def list_all_tags(self):
        return self.root_tag.used_in_tag_items

    # gets a list of tags and returns all folders where these tags are used 
    def list_folders_with_tags(self, tag_list):
        folders = set([folder for tag in tag_list for folder in tag.used_in_folder_items])
        folders = list(folders)
        return folders

    def list_files_with_tags(self, tag_list):
        files = [file for tag in tag_list for file in tag.used_in_file_items]
        files = list(set(files))
        return files

    def list_tags_with_tags(self, tag_list):
        tags = [tag for tag in tag_list for tag in tag.used_in_tag_items]
        tags = list(set(tags))
        return tags

    def list_storage_items_with_tags(self, tag_list: [Tag_item]):
        tags = self.list_files_with_tags(tag_list)
        tags += self.list_folders_with_tags(tag_list)
        return tags

    # gets a tag and a taglist and adds the tags to the tag
    def set_tag_tags(self, tag: Tag_item, tag_list: [Tag_item]):
        tag = self.return_tag(tag.name)
        tags = tag.tag_list + tag_list
        tag.tag_list = list(set(tags))


    
    