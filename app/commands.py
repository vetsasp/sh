import sys
from typing import Callable
from app.find import find


class Command:
    def __init__(self, proc, cmd, args = None):
        self.proc = proc 
        self.cmd = cmd
        self.args = args
        self.builtin: bool
        self.path: str
        self.do: Callable
        self.cmds = {
            "exit": (
                lambda args: sys.exit() if not args \
                    else sys.exit(int(args[0])), 
                lambda args: not args or args[0].isdigit()),
            "echo": (
                lambda args: sys.stdout.write(" ".join(args) + "\n"),
                lambda _: True),
            "type": (
                self.runType, 
                lambda args: len(args) == 1),
            "pwd": (None, None),
            "cd": (None, None), 
        }
  

    def validate(self):
        if not self.isBuiltin():
            self.isPath()
        # Validate args
        if self.builtin:
            validate = self.cmds[self.cmd][1]
            if not validate(self.args):
                raise ValueError(f"{self.cmd}: invalid arguments\n")
        elif not self.path:
            raise ValueError(f"{self.cmd}: command not found\n")

    def run(self):
        self.do(self.args)

    # def isCommand(self, cmd) -> bool:
    #     return cmd in self.cmds or self.isPath(cmd)

    def isBuiltin(self) -> bool:
        self.builtin = self.cmd in self.cmds
        if self.builtin:
            self.do = self.cmds[self.cmd][0]
        return self.builtin

    def isPath(self) -> bool: 
        self.path = find(self.cmd)
        return True if self.path else False

    def runType(self, args):
        c = Command(self.proc, args[0])
        # Check if command is a shell builtin
        if c.isBuiltin():
            sys.stdout.write(c.cmd + " is a shell builtin\n")
            return 

        # Check if command is in PATH
        elif c.isPath():
            sys.stdout.write(f"{c.cmd} is {c.path}\n")
            return

        sys.stdout.write(f"{c.cmd}: not found\n")