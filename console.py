#!/usr/bin/python3
"""
class for the console and its commands
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"}

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the cmd """
        return True

    def emptyline(self):
        """ Overwrite default behavior to repeat last command"""
        pass

    def do_create(self, cls_model):
        """Create instance specified by user"""
        if not cls_model:
            print("** class name missing **")
        elif cls_model not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name = eval(cls_model)
            new_model = class_name()
            storage.save()
            print(new_model.id)

    def do_show(self, entry):
        """Print string representation: name and id"""
        if not entry:
            print("** class name missing **")
            return
        args = entry.split(" ")

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            name = "{}.{}".format(args[0], args[1])
            for key, val in objs.items():
                if key == name:
                    print(val)
                    return
            print("** no instance found **")

    def do_destroy(self, entry):
        """ Deletes an instance passed """
        if not entry:
            print("** class name missing **")
            return
        args = entry.split(" ")
        cls_name = args[0]

        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exits **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            objs = storage.all()
            name = "{}.{}".format(cls_name, obj_id)

            for key, val in objs.items():
                if key == name:
                    del objs[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, entry):
        """Print all objects or all objects of specified class"""

        args = entry.split(" ")
        objs = storage.all()
        list_of_objs = []

        if len(entry) == 0:
            for val in objs.values():
                list_of_objs.append(val.__str__())
            print(list_of_objs)
        elif args[0] in HBNBCommand.classes:
            for key, val in objs.items():
                name = val.__class__.__name__
                if name == args[0]:
                    list_of_objs.append(val.__str__())
            print(list_of_objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, entry):
        """
        Update if given exact object, exact attribute
        Usage:
        update <class name> <id> <attribute name> "<attribute value>"
        """
        if not entry:
            print("** class name missing **")
            return
        args = entry.split(" ")
        objs = storage.all()

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in objs.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_id = args[1]
            cls_name = args[0]
            name = "{}.{}".format(cls_name, obj_id)
            attr = args[2]
            value = args[3].strip("'").strip('"')

            for key, val in objs.items():
                if key == name:
                    setattr(val, attr, value)
                    storage.save()
                    return

    def do_count(self, cls_name):
        """ Displays number of instances of entered class """
        if cls_name in HBNBCommand.classes:
            counts = 0
            objs = storage.all()
            for key, val in objs.items():
                if cls_name in key:
                    counts += 1
            print(counts)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
