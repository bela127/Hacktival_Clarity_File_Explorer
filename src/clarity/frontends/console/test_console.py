
import cmd, sys
from clarity.database.in_memory_db.tag_item import Tag_item
from clarity.database.in_memory_db.storage_item import Storage_item
from clarity.database.in_memory_db.folder_item import Folder_item
from clarity.database.in_memory_db.file_item import File_item
from clarity.core.core import Core


def main():
    Test_console().cmdloop()

class Test_console(cmd.Cmd):
    
    file = None

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Clarity   Type help or ? to list commands.\n'
        self.prompt = 'Clarity Input >> '
        self.core = Core()

    # ----- basic function commands -----
    def do_help(self, arg):
        print("helpfull text")

    ## SEARCH
    # SEARCH helpers

    def do_list_current_tags(self, args):
        tags = self.core.list_current_tags()
        print(tags)

    def do_get_last_tag(self, args):
        tag = self.core.get_last_tag()
        print(tag)

    def do_change_search_tag(self, args):
        self.core.change_search_tag(tag_to_change, new_tag)

    def do_replace_search_tag(self, args):
        self.core.replace_search_tag(tag_to_replace, new_tag)

    # LIST predictions
    
    def do_list_tag_predictions(self,args):
        tags = self.core.list_tag_predictions()

    def do_list_file_predictions(self,args):
        files = self.core.list_file_predictions()

    def do_list_folder_predictions(self,args):
        folders = self.core.list_folder_predictions()
    
    # List Tags with text

    def do_list_tags_with_text(self, args):
        tags = self.core.list_tags_with_text(args)
    
    def do_list_tags_start_with_text(self, args):
        tags = self.core.list_tags_start_with_text(args)

    # List Tags with querry

    def do_list_tags_with_querry(self, args):
        tags = self.core.list_tags_with_querry(querry)

    ##

    # SET Tags

    def set_tag_tags(self, args):
        tokens = parse(args)
        tag = Tag_item(tokens[0])
        tags = [self.core.get_tag_by_name(name) for name in tokens[1:]]
        self.core.set_tag_tags(tag, tags)
    
    def set_file_tags(self, args):
        tokens = parse(args)
        file = File_item(tokens[0], tokens[1], [])
        tags = [self.core.get_tag_by_name(name) for name in tokens[2:]]
        self.core.set_file_tags(file, tags)
    
    def set_folder_tags(self, args):
        tokens = parse(args)
        folder = Folder_item(tokens[0], tokens[1], [])
        tags = [self.core.get_tag_by_name(name) for name in tokens[2:]]
        self.core.set_folder_tags(folder, tags)

    # ADD items
    
    def do_add_tag(self, args):
        tokens = parse(args)
        tag = Tag_item(tokens[0])
        tags = [self.core.get_tag_by_name(name) for name in tokens[1:]]
        self.core.add_tag(tag, tags)

    def do_add_file(self, args):
        tokens = parse(args)
        file = File_item(tokens[0], tokens[1], [])
        tags = [self.core.get_tag_by_name(name) for name in tokens[2:]]
        self.core.add_file(file, tags)

    def do_add_folder(self, args):
        tokens = parse(args)
        folder = Folder_item(tokens[0], tokens[1], [])
        tags = [self.core.get_tag_by_name(name) for name in tokens[2:]]
        self.core.add_folder(folder, tags)

    # LIST items with tags

    def do_list_tags_with_tags(self, args):
        tokens = parse(args)
        tags = [self.core.get_tag_by_name(name) for name in tokens[0:]]
        tags = self.core.list_tags_with_tags(tags)
        print(tags)

    def do_list_files_with_tags(self, args):
        tokens = parse(args)
        tags = [self.core.get_tag_by_name(name) for name in tokens[0:]]
        files = self.core.list_files_with_tags(tags)
    
    def do_list_folders_with_tags(self, args):
        tokens = parse(args)
        tags = [self.core.get_tag_by_name(name) for name in tokens[0:]]
        folders = self.core.list_folders_with_tags(tags)

    # LIST items with tag

    def do_list_items_with_tag(self, args):
        items = self.core.list_items_with_tags(tags)

    def do_list_tags_with_tag(self, args):
        tags = self.core.list_tags_with_tags(tags)

    def do_list_files_with_tag(self, args):
        files = self.core.list_files_with_tags(tags)
    
    def do_list_folders_with_tag(self, args):
        folders = self.core.list_folders_with_tags(tags)

    # LIST all items 

    def do_list_all_files(self, args):
        files = self.core.list_all_files()

    def do_list_all_folders(self, args):
        folders = self.core.list_all_folders()

    def do_list_all_tags(self, args):
        tags = self.core.list_all_tags()

    # LIST exact items
    
    def do_list_exact_files(self, args):
        files = self.core.list_exact_files(tags)

    def do_list_exact_folders(self, args):
        folders = self.core.list_exact_folders(tags)

    def do_list_exact_tags(self, args):
        tags = self.core.list_exact_tags(tags)

    # LIST Tags of item

    def do_list_tags_of_item(self, args):
        tags = self.core.list_tags_of_item(item)

    def do_list_tags_of_tag(self, args):
        tags = self.core.list_tags_of_tag(tag)
    
    def do_list_tags_of_file(self, args):
        tags = self.core.list_tags_of_file(file)

    def do_list_tags_of_folder(self, args):
        tags = self.core.list_tags_of_folder(folder)

    # MODULE stuff
    def do_list_all_modules(self, args):
        modules = self.core.list_all_modules()

    #TODO more module stuff... help etc

    #Console Stuff

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close(self):
        pass

    def default(self, line):
        print("The Command is not jet known: ", line)
        print("The Command is not jet known: ", line)

    def completedefault(self, text, line, begidx, endidx):
        print("used to complete empty lines")
        print(text, line, begidx, endidx)
        return []

    def preloop(self):
        print("Additional text befor start: ",end="")

    def postcmd(self, stop, line):
        print()
        print("Additional text after command >> ",end="")

    def postloop(self):
        print("good by")


def parse(arg):
    return tuple(arg.split())

if __name__ == "__main__":
    main()
