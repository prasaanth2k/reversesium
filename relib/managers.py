from relib.arguments import Arguments
from relib.buildhelper import Environment

environ = Environment()

class Managers:

    def __init__(self,args:Arguments):
        self.args = args

        if args.hasCommands(['build']):
            if args.hasOptions(['--tag']) and args.hasOptions(['--path']):
                environ.build(tag=args.getOptionValue('--tag'),path=args.getOptionValue('--path'))
            else:
                environ.build(tag="reversesium:v1",path=".")

        if args.hasCommands(['startsession']):
            if args.hasOptions(['--session']) and args.hasOptions(['--host']) and args.hasOptions(['--network']) and args.hasOptions(['--username']):
                environ.start_session(sessionname=args.getOptionValue('--session'), hostname=args.getOptionValue('--host'),network=args.getOptionValue('--network'),username=args.getOptionValue('--username'))
            elif args.hasOptions(['--session']) and args.hasOptions(['--host']) and args.hasOptions(['--network']) and args.hasOptions(['--username']):
                environ.start_session(sessionname=args.getOptionValue('--session'), hostname=args.getOptionValue('--host'),network=args.getOptionValue('--network'),username=args.getOptionValue('--username'))
            else:
                print("\n[*] Missing options --session= --host= --network= --username")
        elif args.hasCommands(['shell']):
            if args.hasOptions(['--session']) and args.hasOptions(['--username']):
                environ.spawn_shell(sessionname=args.getOptionValue('--session'),username=args.getOptionValue('--username'))
            elif args.hasOptions(['--session']):
                environ.spawn_shell(sessionname=args.getOptionValue('--session'),username="root")
            else:
                print("\n[*] Missing option --session= ")

        elif args.hasCommands(['stopsession']):
            if args.hasOptions(['--session']):
                environ.stop_session(sessionname=args.getOptionValue('--session'))
            else:
                print("\n[*] Missing option --session= ")

        elif args.hasCommands(['currentsession']):
            environ.current_sessions()

        elif args.hasCommands(['trace']):
            if args.hasOptions(['--cmd']):
                environ.tracer(cmd=args.getOptionValue('--cmd'))
            else:
                print("\n[*] Missing option --cmd=")

        elif args.hasCommands(['hexbytes']):
            if args.hasOptions(['--value']):
                environ.hex_to_bytes(hex_value=args.getOptionValue('--value'))
            else:
                print("\n[*] Missing option --value=")