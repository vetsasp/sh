import sys 

from app.validate import validateCommand



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
        valid = validateCommand(cmd)

        if not valid:
            sys.stdout.write(f"{cmd}: command not found\n")
            return 

        if not valid(args):
            sys.stdout.write(f"{cmd}: invalid arguments\n")
            return

        # Run command
        self.runCommand(cmd, args)


    def runCommand(self, cmd, args):
        cmds = {
            "exit": lambda args: sys.exit() if not args else sys.exit(int(args[0])),
            "echo": lambda args: sys.stdout.write(" ".join(args) + "\n"),
        }

        cmds[cmd](args)

    