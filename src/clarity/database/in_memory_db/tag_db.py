class Tag_db():
    def __init__(self):
        self.name = []          #list of list of strings
        self.tags = []          #list of list of tags
        self.used_in_item = []  #list of list of items
    
    def tags_start_with(self, text):
        tag_list = []
        for i in self.name:
            if text.startswith(self.name[i]):
                tag_list.append(self.name[i])
    
        return tag_list

    def tags_contains(self, text):
        tag_list = []
        for i in self.name:
            if text in self.name[i]:
                tag_list.append(self.name[i])
    
        return tag_list

    def items_with(self, tag):
        for i in self.name:
            if tag.name == self.name[i]:
                return self.used_in_item[i]
        return []
        
    