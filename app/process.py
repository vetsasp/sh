import sys, subprocess 
from app.commands import Command 
from app.find import *

class Process:
    def __init__(self, cmd, args):
        self.cmd = cmd
        self.args = args
        self.c: Command = None
        
    def validate(self) -> bool:
        # Validate command and args
        try:
            self.c = Command(self.cmd, self.args)
            self.c.validate()
        except ValueError as e:
            sys.stderr.write(str(e))
            return False
        return True

    def run(self):
        # Run command
        c = self.c
        c.run() if c.builtin else subprocess.run([c.path] + c.args)