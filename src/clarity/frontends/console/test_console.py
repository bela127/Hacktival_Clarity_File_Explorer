
import cmd, sys
import clarity.core.core


def main():
    Test_console().cmdloop()

class Test_console(cmd.Cmd):
    
    file = None

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Clarity   Type help or ? to list commands.\n'
        self.prompt = 'Clarity Input >> '

    # ----- basic function commands -----
    def do_help(self, arg):
        print("helpfull text")

    ## SEARCH
    # SEARCH helpers

    def do_list_current_tags(self, args):
        pass

    def do_get_last_tag(self, args):
        pass

    def do_change_search_tag(self, args):
        pass

    def do_replace_search_tag(self, args):
        pass

    # LIST predictions
    
    def do_list_tag_predictions(self,args):
        pass

    def do_list_file_predictions(self,args):
        pass

    def do_list_folder_predictions(self,args):
        pass
    
    # List Tags with text

    def do_list_tags_with_text(self, args):

        pass
    
    def do_list_tags_start_with_text(self, args):
        pass

    # List Tags with querry

    def do_list_tags_with_querry(self, args):
        pass

    ##

    # SET Tags

    def do_set_item_tag(self, args):
        pass

    def do_set_tag_tag(self, args):
        pass
    
    def do_set_file_tag(self, args):
        pass
    
    def do_set_folder_tag(self, args):
        pass

    # ADD items
    
    def do_add_tag(self, args):
        pass

    def do_add_file(self, args):
        pass

    def do_add_folder(self, args):
        pass

    # LIST items with tags

    def do_list_items_with_tags(self, args):
        pass

    def do_list_tags_with_tags(self, args):
        pass

    def do_list_files_with_tags(self, args):
        pass
    
    def do_list_folders_with_tags(self, args):
        pass

    # LIST items with tag

    def do_list_items_with_tag(self, args):
        pass

    def do_list_tags_with_tag(self, args):
        pass

    def do_list_files_with_tag(self, args):
        pass
    
    def do_list_folders_with_tag(self, args):
        pass

    # LIST items

    def do_list_all_files(self, args):
        pass

    def do_list_all_folders(self, args):
        pass

    def do_list_all_tags(self, args):
        pass

    # LIST exact items
    
    def do_list_exact_files(self, args):
        pass

    def do_list_exact_folders(self, args):
        pass

    def do_list_exact_tags(self, args):
        pass

    # LIST Tags

    def do_list_tags_of_item(self, args):
        pass

    def do_list_tags_of_tags(self, args):
        pass
    
    def do_list_tags_of_file(self, args):
        pass

    def do_list_tags_of_folder(self, args):
        pass

    # MODULE stuff
    def do_list_all_modules(self, args):
        pass

    def do_call_module(self, args):
        pass

    #TODO more module stuff... help etc

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
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == "__main__":
    main()
