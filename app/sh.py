import sys, os

from app.process import Process



class Shell:
    def __init__(self):
        self.cmds = {"exit"}
        self.cwd = os.getcwd()

    def run(self):
        while True:
            self.acceptCommand()

    def acceptCommand(self):
        # prompt
        sys.stdout.write("$ ")

        cmd = input()

        # separate command from args
        cmd, *args = cmd.split(" ")

        # Create process 
        p = Process(self, cmd, args)
        if not p.validate():
            return 
        
        p.run()

    def getcwd(self):
        return self.cwd