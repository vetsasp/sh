import sys 

from app.process import Process



class Shell:
    def __init__(self):
        self.cmds = {"exit"}

    def run(self):
        while True:
            self.acceptCommand()

    def acceptCommand(self):
        # prompt
        sys.stdout.write("$ ")

        cmd = input()

        # separate command from args
        cmd, *args = cmd.split(" ")

        # print(f"'{cmd}'", file=sys.stderr)  # DEBUG 
        # print(f"'{args}'", file=sys.stderr)  # DEBUG
        
        # Validate command and args
        # if not isCommand(cmd):
        #     sys.stdout.write(f"{cmd}: command not found\n")
        #     return 
        
        # if not validateCommand(cmd, args):
        #     sys.stdout.write(f"{cmd}: invalid arguments\n")
        #     return

        # Run command
        p = Process(cmd, args)
        if not p.validate():
            return 
        p.run()