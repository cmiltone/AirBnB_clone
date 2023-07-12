#!/usr/bin/python3
"""command interpreter entry point"""

# standard modules/packages
import cmd

# custom packages/modules
from models.base_model import BaseModel
from models import storage

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

    def emptyline(self):
        """  """
        return False

    def do_help(self, *args):
        """shows how to use the console"""
        if args[0] == "":
            print("Documented commands (type help <topic>):")
            print("========================================")

        arg = args[0]

        if arg == "quit":
            print("Quit command to exit the program\n")
        if arg == "create":
            print("Create command creates a model instance and saves it")

    def do_create(self, *args):
        if args[0] == "":
            print("** class name missing **")
        elif args[0] == "BaseModel":
            model = BaseModel()
            model.save()
            print(model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, a):
        """prints string representation of instance"""
        classes = ["BaseModel"]
        args = a.split()

        if args[0] == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist ** ")
        elif len(args) == 1 or args[1] == '':
            print("** instance id missing **")
        else:
            objs = storage.all()
            id = "{}.{}".format(args[0], args[1])
            obj = objs.get(id)
            if obj is None:
                print("* no instance found **")
            else:
                print(obj)
                


if __name__ == '__main__':
    HBNBCommand().cmdloop()
