import file_db
import tag_item

class Tag_db():
    def __init__(self):
        self.tags = []      #list of tags
    
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
            if tag.name == self.tags[i].name:
                return self.tags[i]
        return None
    
    # gets a name a directory and a taglist and creates a tag
    def add_tag(self, name, directory, tags):
        new_tag = tag_item(name, directory, tags)
        self.tags.append(new_tag)
        
