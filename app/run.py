import sys
from app.validate import validateCommand

def runCommand(cmd, args):
        cmds = {
            "exit": lambda args: sys.exit() if not args \
                else sys.exit(int(args[0])),
            "echo": lambda args: sys.stdout.write(" ".join(args) + "\n"),
            "type": runType, 
        }

        cmds[cmd](args)

def runType(args):
    if validateCommand(args[0]):
        sys.stdout.write(args[0] + " is a shell builtin\n")
    else:
        sys.stdout.write(f"{args[0]}: not found\n")