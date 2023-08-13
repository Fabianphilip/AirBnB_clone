#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        save to the JSON file then prints the id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of an instance based on the
        class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                print(instances[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        then save the change to the JSON file)"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                del instances[key]
                storage.save()

    def do_all(self, arg):
        """Prints strings representation of all instances
        based or not on the class name"""
        args = arg.split()
        if len(args) == 0:
            instances = storage.all()
            for instance in instances.values():
                print(instance)
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            for instance in instances.values():
                if isinstance(instance, eval(args[0])):
                    print(instance)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute then save the changes into the JSON file"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(instances[key], args[2], eval(args[3]))
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
