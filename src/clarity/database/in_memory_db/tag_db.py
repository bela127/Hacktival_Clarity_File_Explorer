from clarity.database.in_memory_db.tag_item import Tag_item

class Tag_db():
    def __init__(self):
        self.root_tag = Tag_item("root")
        self.root_tag.used_in_tag_items.append(self.root_tag)

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
        remaining_folders = []

        if len(tag_list) > 0:
            vergleichs_tag = self.return_tag(tag_list[0].name)
            remaining_folders = vergleichs_tag.used_in_folder_items
            for tag in tag_list[1:]:
                vergleichs_tag = self.return_tag(tag.name)
                remaining_folders = [ selected_folder for selected_folder in remaining_folders if vergleichs_tag in selected_folder.tag_list]
        
        remaining_folders = sorted(remaining_folders,key=lambda tag: len(tag.used_in_folder_items) + len(tag.used_in_file_items))
        return remaining_folders

    def list_files_with_tags(self, tag_list):
        remaining_files = []

        if len(tag_list) > 1:

            vergleichs_tag = self.return_tag(tag_list[1].name)
            remaining_files = vergleichs_tag.used_in_file_items
            print(remaining_files)
            for tag in tag_list[2 :]:
                vergleichs_tag = self.return_tag(tag.name)
                print(vergleichs_tag)
                remaining_files = [ selected_file for selected_file in remaining_files if vergleichs_tag in selected_file.tag_list]
                print(remaining_files)
        remaining_files = sorted(remaining_files,key=lambda tag: len(tag.used_in_folder_items) + len(tag.used_in_file_items))
        print(remaining_files)
        return remaining_files

    def list_tags_with_tags(self, tag_list):
        remaining_tags = []

        if len(tag_list) > 0:
            vergleichs_tag = self.return_tag(tag_list[0].name)
            remaining_tags = vergleichs_tag.used_in_tags_items
            for tag in tag_list[1:]:
                vergleichs_tag = self.return_tag(tag.name)
                remaining_tags = [ selected_tag for selected_tag in remaining_tags if vergleichs_tag in selected_tag.tag_list]
        
        remaining_tags = sorted(remaining_tags,key=lambda tag: len(tag.used_in_tag_items))
        return remaining_tags

    def list_storage_items_with_tags(self, tag_list: [Tag_item]):
        tags = self.list_files_with_tags(tag_list)
        tags += self.list_folders_with_tags(tag_list)
        tags = list(set(tags))
        tags = sorted(tags,key=lambda tag: len(tag.used_in_folder_items) + len(tag.used_in_file_items))
        return tags

    # gets a tag and a taglist and adds the tags to the tag
    def set_tag_tags(self, tag: Tag_item, tag_list: [Tag_item]):
        tag = self.return_tag(tag.name)
        tags = tag.tag_list + tag_list
        tag.tag_list = list(set(tags))

    # removes a tag from the tag-list 
    def remove_tag(self, tag):
        for foi in tag.used_in_folder_items:
            foi.tag_list.remove(tag)
        for fii in tag.used_in_file_items:
            fii.tag_list.remove(tag)
        for tai in tag.used_in_tag_items:
            tai.tag_list.remove(tag)
        
        self.root_tag.used_in_tag_items.remove(tag)
    

    
    