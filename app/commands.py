import sys
from app.find import find


class Command:
    def __init__(self, cmd, args = None):
        self.cmd = cmd
        self.args = args
        self.builtin = isBuiltin(self.cmd)
        self.path = find(self.cmd) if not self.builtin else None
        self.do = cmds[self.cmd][0] if self.builtin else None      

    def validate(self):
        # Validate args
        if self.builtin:
            validate = cmds[self.cmd][1]
            if not validate(self.args):
                raise ValueError(f"{self.cmd}: invalid arguments\n")
        elif not self.path:
            raise ValueError(f"{self.cmd}: command not found\n")

    def run(self):
        self.do(self.args)

def isCommand(cmd) -> bool:
    return cmd in cmds or isPath(cmd)

def isBuiltin(cmd) -> bool:
    return cmd in cmds

def isPath(cmd) -> bool: 
    return True if find(cmd) else False

def runType(args):
    c = Command(args[0])
    # Check if command is a shell builtin
    if c.builtin:
        sys.stdout.write(c.cmd + " is a shell builtin\n")
        return 

    # Check if command is in PATH
    if c.path:
        sys.stdout.write(f"{c.cmd} is {c.path}\n")
        return

    sys.stdout.write(f"{c.cmd}: not found\n")


cmds = {
    "exit": (
        lambda args: sys.exit() if not args \
            else sys.exit(int(args[0])), 
        lambda args: not args or args[0].isdigit()),
    "echo": (
        lambda args: sys.stdout.write(" ".join(args) + "\n"),
        lambda _: True),
    "type": (
        runType, 
        lambda args: len(args) == 1),
}
