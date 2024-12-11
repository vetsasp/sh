import sys 



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
        valid = self.validCommand(cmd)

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
            "exit": lambda x: sys.exit(int(x[0])),
        }

        cmds[cmd](args)

    def validCommand(self, cmd):
        '''
          takes in a command
          if command is valid, returns expected args
        ''' 
        cmds = {
            # "exit": lambda x: isinstance(x[0], int)
            "exit": lambda x: x[0].isdigit()
        }

        if cmd in cmds:
            return cmds[cmd]
        
        return None 