import sys, os
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
    # Check if command is a shell builtin
    if validateCommand(args[0]):
        sys.stdout.write(args[0] + " is a shell builtin\n")
        return 

    # Check if command is in PATH
    path_env = os.environ.get("PATH")

    paths = path_env.split(':')

    for path in paths:
        if os.path.exists(path + '/' + args[0]):
            sys.stdout.write(args[0] + " is " + path + '/' + args[0] + "\n")
            return

    sys.stdout.write(f"{args[0]}: not found\n")