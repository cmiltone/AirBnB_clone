#!/usr/bin/python3
"""command interpreter entry point"""

# standard modules/packages
import cmd
import json

# custom packages/modules
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """a class for the console"""
    prompt = "(hbnb) "
    classes = [
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    ]

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
        if arg == "show":
            print("Show command prints string representation of an instance")
        if arg == "destroy":
            print("Destroy command deletes an instance")
        if arg == "all":
            print("All command prints string representation of all instances")

    def do_create(self, *args):
        if args[0] == "":
            print("** class name missing **")
        elif args[0] == "BaseModel":
            model = BaseModel()
            model.save()
            print(model.id)
        elif args[0] == "User":
            model = User()
            model.save()
            print(model.id)
        elif args[0] == "Place":
            model = Place()
            model.save()
            print(model.id)
        elif args[0] == "State":
            model = State()
            model.save()
            print(model.id)
        elif args[0] == "City":
            model = City()
            model.save()
            print(model.id)
        elif args[0] == "Amenity":
            model = Amenity()
            model.save()
            print(model.id)
        elif args[0] == "Review":
            model = Review()
            model.save()
            print(model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints string representation of instance"""
        args = arg.split()

        if args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == '':
            print("** instance id missing **")
        else:
            objs = storage.all()
            id = "{}.{}".format(args[0], args[1])
            obj = objs.get(id)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        """deletes an instance"""
        args = arg.split()

        if args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == '':
            print("** instance id missing **")
        else:
            objs = storage.all()
            id = "{}.{}".format(args[0], args[1])
            obj = objs.get(id)
            if obj is None:
                print("** no instance found **")
            else:
                objs.pop(id)
                storage.save()

    def do_all(self, arg):
        """prints all instance"""
        args = arg.split()

        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) > 0 and args[0] in self.classes:
            # print single class
            arr = []
            objs = storage.all()
            for k in objs:
                if args[0] in k:
                    arr.append("{}".format(objs[k]))
            print(arr)
        else:
            # print all classes
            arr = []
            objs = storage.all()
            for k in objs:
                arr.append("{}".format(objs[k]))
            print(arr)

    def do_update(self, arg):
        """updates an instance"""
        args = arg.split()

        if args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == '':
            print("** instance id missing **")
        elif len(args) < 3 or args[2] == '':
            print("** attribute name missing **")
        elif len(args) < 4 or args[3] == '':
            print("** value missing **")
        else:
            objs = storage.all()
            id = "{}.{}".format(args[0], args[1])
            obj = objs.get(id)
            if obj is None:
                print("** no instance found **")
            else:
                val = args[3]
                int_failed = False
                try:
                    val = int(val)
                except (ValueError):
                    int_failed = True
                if int_failed:
                    try:
                        val = float(val)
                    except (ValueError):
                        pass
                setattr(obj, args[2], val)
                obj.save()

    def default(self, arg):
        """
        command for:
            <class name>.all()
        """
        [model, args] = arg.split(".", 1)
        [command, params] = args.split("(")
        params = params.replace(")", "")

        if command == "all":
            self.do_all("{}".format(model))
        elif command == "count":
            params = params.replace("\"", "")
            count = 0
            objs = storage.all()
            if params:
                for k in objs:
                    if "{}.{}".format(model, params) in k:
                        count += 1
            else:
                for k in objs:
                    if model in k:
                        count += 1
            print(count)
        elif command == "show":
            params = params.replace("\"", "")
            self.do_show("{} {}".format(model, params))
        elif command == "destroy":
            params = params.replace("\"", "")
            self.do_destroy("{} {}".format(model, params))
        elif command == "update":
            if "{" in params and "}" in params:
                params = params.split(", ", 1)
            else:
                params = params.split(", ")
            if len(params) == 2:
                [id, json_str] = params
                data = json.loads(json_str)
                for k in data:
                    self.do_update("{} {} {} {}".format(model, id, k, data[k]))
            elif len(params) == 3:
                [id, field, value] = params
                id = id.replace("\"", "")
                field = field.replace("\"", "")
                value = value.replace("\"", "")
                self.do_update("{} {} {} {}".format(model, id, field, value))
            print(self.prompt)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
