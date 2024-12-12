import sys, os, re

from app.process import Process



class Shell:
    def __init__(self):
        self.cmds = {"exit"}
        self.cwd = os.getcwd()

    def run(self):
        while True:
            self.acceptCommand()

    def acceptCommand(self):
        self.prompt()
        cmd = input()

        # separate command from args
        # cmd, *args = cmd.split(" ")
        cmd, args = self.parse(cmd)

        # print(f"cmd: {cmd}\nargs: {args}")

        if not cmd:
            return 
        
        # Check if command modifies shell
        shcmd = self.checkShellCommand(cmd, args)
        if shcmd:
            shcmd(args)
            return

        # Create process 
        p = Process(self, cmd, args)
        if not p.validate():
            return 
        
        p.run()
    
    def prompt(self):
        sys.stdout.write("$ ")

    def parse(self, cmd):
        # parse command and args
        # maintain quotes 
        parts = re.findall(
            r'(?:"[^"\\]*(?:\\.[^"\\]*)*"|\'[^\'\\]*(?:\\.[^\'\\]*)*\'|\\(?:[^\'"]|\\.)*|[^\s"\']+)',
              cmd)
        cmd = parts[0] if parts else ''
        args = parts[1:] if len(parts) > 1 else []

        # remove quotes
        cmd = cmd.strip('"').strip("'")
        args = [arg.strip('"').strip("'") for arg in args]
        return cmd, args

    def checkShellCommand(self, cmd, args):
        if cmd == "pwd" and len(args) == 0:
            return self.pwd
        if cmd == "cd" and len(args) <= 1:
            return self.cd
        return None 

    def getcwd(self):
        return self.cwd
    
    def pwd(self, _):
        sys.stdout.write(self.cwd + "\n")

    def cd(self, args):
        path = args[0] if len(args) > 0 else "~"

        # goto home 
        if path == "~":
            self.cwd = os.environ["HOME"]
            return

        #  if path is not absolute
        if path[0] != "/":
            path = os.path.join(self.cwd, path)

        # if path is a directory
        if os.path.isdir(path):
            self.cwd = os.path.abspath(path)
        else: 
            sys.stderr.write(f"cd: {path}: No such file or directory\n")