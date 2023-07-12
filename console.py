#!/usr/bin/python3
"""command interpreter entry point"""
import cmd


class HBNBCommand(cmd.Cmd):
    """a class for the console"""
    prompt = "(hbnb) "
    def do_quit(self, *args):
        """exits the console"""
        return True

    def do_EOF(self, *args):
        """exits the console"""
        print()
        return True

    def do_help(self, *args):
        """shows how to use the console"""
        if len(args) == 0:
            print("Documented commands (type help <topic>):")
            print("========================================")

        arg = args[0]

        if arg == "quit":
            print("Quit command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
