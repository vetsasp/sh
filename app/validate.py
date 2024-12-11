def validateCommand(cmd):
        '''
          takes in a command
          if command is valid, returns expected args
        ''' 
        cmds = {
            "exit": lambda args: not args or args[0].isdigit(),
            "echo": lambda _: True,
        }

        if cmd in cmds:
            return cmds[cmd]
        
        return None 