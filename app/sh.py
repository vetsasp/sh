import sys 



class Shell:
    def __init__(self):
        self.cmds = {}

    def run(self):
        while True:
            self.runCommand()

    def runCommand(self):
        # prompt
        sys.stdout.write("$ ")

        cmd = input()

        if cmd not in self.cmds:
            sys.stdout.write(f"{cmd}: command not found\n")