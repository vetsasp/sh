import sys 



class Shell:
    def __init__(self):
        pass 

    def run(self):
        # prompt
        sys.stdout.write("$ ")

        cmd = input()

        cmds = {}

        if cmd not in cmds:
            sys.stdout.write(f"{cmd}: command not found\n")