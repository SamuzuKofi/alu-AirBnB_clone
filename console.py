import cmd
import sys

class MyCommandLine(cmd.Cmd):
    intro = 'Welcome to MyCommandLine. Type help or ? to list commands.\n'
    prompt = '(mycli) '

    def do_greet(self, name):
        """Greet the person with the given name."""
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello!")

    def do_exit(self, arg):
        """Exit the command line."""
        print("Goodbye!")
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit."""
        print("Goodbye!")
        return True
