import os

def find(target) -> str:
    # Check if command is in PATH
    path_env = os.environ.get("PATH")

    if not path_env:
        raise ValueError("PATH environment variable not found")
    paths = path_env.split(':')

    for path in paths:
        if os.path.exists(path + '/' + target):
            return path + '/' + target
    
    return ""